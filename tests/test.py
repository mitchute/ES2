import os
import unittest

from enstore.core.utilities.functions import add

if "GITHUB_ACTIONS" in os.environ:
    skip_tests = True
else:
    skip_tests = False


@unittest.skipIf(skip_tests, "Skip these tests")
class TestClass(unittest.TestCase):

    def test_placeholder(self):
        assert 3 == 3

    def test_placeholder_2(self):
        assert 4 == 4

    def test_add(self):
        assert add(1, 1) == 2
