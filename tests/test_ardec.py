from datetime import datetime
from datetime import timedelta

import ardec
import mock


@ardec.migration('Example Migration')
def example_migration():
    return True


@ardec.stage('example_stage')
def example_stage():
    return True


def test_delta():
    mig = ardec.migration('pytest')
    mig.start = datetime.utcnow() - timedelta(seconds=3)
    assert round(mig.delta(), 3) == 3.000


@mock.patch('ardec.migration.__exit__')
@mock.patch('ardec.migration.log')
def test_migration_enter(mock_log, mock_exit):
    example_migration()
    mock_log.assert_called_with(
        '== {} Example Migration '
        .format(datetime.utcnow().strftime('%Y%m%d%H%M%S'))
        .ljust(79, '=') + "\n")


@mock.patch('ardec.migration.__enter__')
@mock.patch('ardec.migration.delta')
@mock.patch('ardec.migration.log')
def test_migration_exit(mock_log, mock_delta, mock_enter):
    mock_delta.return_value = 1.2345
    example_migration()
    mock_log.assert_called_with(
        '== {} Example Migration ({}s) '
        .format(datetime.utcnow().strftime('%Y%m%d%H%M%S'), 1.2345)
        .ljust(79, '=') + "\n\n")


@mock.patch('ardec.stage.__exit__')
@mock.patch('ardec.stage.log')
def test_stage_enter(mock_log, mock_exit):
    example_stage()
    mock_log.assert_called_with('-- example_stage\n')


@mock.patch('ardec.stage.__enter__')
@mock.patch('ardec.stage.delta')
@mock.patch('ardec.stage.log')
def test_stage_exit(mock_log, mock_delta, mock_enter):
    mock_delta.return_value = 1.2345
    example_stage()
    mock_log.assert_called_with('   -> 1.2345s\n')


def test_log():
    assert example_migration()
    assert example_stage()
