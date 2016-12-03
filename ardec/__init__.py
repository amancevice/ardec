"""
ActiveRecord-style decorators

Wrap functions in decorators to log output like an ActiveRecord migration.
"""

from datetime import datetime
try:
    from contextlib import ContextDecorator
except ImportError:
    from contextlib2 import ContextDecorator

__version__ = '0.0.1'


# pylint: disable=invalid-name,too-few-public-methods
class migration(ContextDecorator):
    """ Decorator for migrations. """
    def __init__(self, name):
        self.name = name
        self.start = self.label = None

    def __enter__(self):
        self.start = datetime.utcnow()
        self.label = self.start.strftime("%Y%m%d%H%M%S")
        # pylint: disable=superfluous-parens
        print("== {} {} ".format(self.label, self.name).ljust(79, "="))
        return self

    def __exit__(self, *exc):
        # pylint: disable=superfluous-parens
        print("== {} {} ({}s) "
              .format(self.label, self.name, self.delta())
              .ljust(79, "=") + "\n")
        return False

    def delta(self):
        """ Helper to get time delta. """
        start = self.start or datetime.utcnow()
        return round((datetime.utcnow() - start).total_seconds(), 4)


# pylint: disable=invalid-name,too-few-public-methods
class stage(migration):
    """ Decorator for migration stages. """
    def __enter__(self):
        self.start = datetime.utcnow()
        # pylint: disable=superfluous-parens
        print("-- {}".format(self.name))
        return self

    def __exit__(self, *exc):
        # pylint: disable=superfluous-parens
        print("   -> {}s".format(self.delta()))
        return False
