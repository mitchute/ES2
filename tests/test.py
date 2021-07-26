import unittest

from src.functions import add, get_cp, mult


class TestClass(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_mult(self):
        self.assertEqual(mult(3, 4), 12)

    def test_get_cp(self):
        self.assertAlmostEqual(get_cp(20), 4183.99, delta=1E-2)
