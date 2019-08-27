""" Decorators and other utilities for dummy code"""
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)


def dummy(func):
    """Dummy decorator for @dummy-flagged code"""

    def dummy_wrap(self, *args, **kwargs):
        """ Decorates to a dummy function """
        print("Calling dummy for %s" % func.__str__())
        func(self, *args, **kwargs)
    return dummy_wrap
