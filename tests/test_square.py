import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square_area(0)
        self.assertEqual(res, -2)

    def test_simple_area(self):
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_negative_area(self):
        res = square_area(-6)
        self.assertEqual(res, -1)

    def test_zero_perimeter(self):
        res = square_perimeter(0)
        self.assertEqual(res, -2)

    def test_simple_perimeter(self):
        res = square_perimeter(9)
        self.assertEqual(res, 36)

    def test_negative_perimeter(self):
        res = square_perimeter(-9)
        self.assertEqual(res, -1)

if __name__ == "__main__":
    unittest.main()