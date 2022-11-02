import unittest
from implem3 import in_set

class InSetTesting(unittest.TestCase):
    def test_in(self):
        self.assertTrue(in_set(3, {2, 4, 7, 3, 9}))
        self.assertTrue(in_set(4, {5, 7, 9, 4, 3}))

    def test_not_in(self):
        self.assertFalse(in_set(2, {8, 9, 6, 4}))
        self.assertFalse(in_set(5, {8, 7, 6, 1}))


if __name__ == "__main__":
    unittest.main()

