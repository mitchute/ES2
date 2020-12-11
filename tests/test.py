import unittest

from enstore.core.functions import add


class TestClass(unittest.TestCase):

    def test_placeholder(self):
        assert 3 == 3

    def test_placeholder_2(self):
        assert 4 == 4

    def test_add(self):
        assert add(1, 1) == 2
