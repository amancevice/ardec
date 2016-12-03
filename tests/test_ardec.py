from datetime import datetime
from datetime import timedelta

import ardec


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


def test_migration():
    assert example_migration() is True


def test_stage():
    assert example_stage() is True
