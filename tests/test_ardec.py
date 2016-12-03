import ardec


@ardec.migration('Example Migration')
def example_migration():
    return True


@ardec.stage('example_stage')
def example_stage():
    return True


def test_migration():
    assert example_migration()


def test_stage():
    assert example_stage()
