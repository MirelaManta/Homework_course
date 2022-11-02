import unittest
from implem2 import compare
from math import sqrt

class ComparisonTests(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(compare(8, 2), 1, 'Expected 1 (mai mare).')
        self.assertEqual(compare(4, 9), -1, 'Expected -1 (mai mic).')
        self.assertEqual(compare(10, 10), 0, 'Expected 0 (egale).')

    def test_neg(self):
        self.assertEqual(compare(-9, -6,), -1, 'Expected -1 (mai mic).')
        self.assertEqual(compare(-2, -7), 1, 'Expected 1 (mai mare).')
        self.assertEqual(compare(-3, -3), 0, 'Expected 0 (egale.')

    def test_complex(self):
        self.assertEqual(compare(pow(2, 4), sqrt(256)), 0)
        self.assertTrue(compare(sqrt(60), 7.5) == 1)


if __name__ == "__main__":
        unittest.main()
