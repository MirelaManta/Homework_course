import unittest
from implem1 import max_value
from math import sqrt

class TestDigitCount(unittest.TestCase):
    def test_positive_int(self):
        self.assertEqual(max_value(12, 5, 29), 29, 'Expected 29.')
        self.assertEqual(max_value(2, 15, 9), 15, 'Expected 15.')

    def test_negative_int(self):
        self.assertEqual(max_value(-5, -7, -12), -5)
        self.assertEqual(max_value(-6, -100, -3), -3, 'Expected -3')

    def test_real_nums(self):
        self.assertEqual(max_value(3.5, 5.25, 7.2), 7.2)
        self.assertEqual(max_value(sqrt(60), 8.5, 10.5), 10.5)


if __name__ == "__main__":
    unittest.main()

