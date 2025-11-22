import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle_area(4, 0)
        self.assertEqual(res, -2)

    def test_simple_area(self):
        res = triangle_area(13, 6)
        self.assertEqual(res, 39)

    def test_negative_area(self):
        res = triangle_area(-13, 6)
        self.assertEqual(res, -1)

    def test_zero_perimeter(self):
        res = triangle_perimeter(0, 4, 3)
        self.assertEqual(res, -2)

    def test_simple_perimeter(self):
        res = triangle_perimeter(9, 10, 14)
        self.assertEqual(res, 33)

    def test_negative_perimeter(self):
        res = triangle_perimeter(5, 4, -14)
        self.assertEqual(res, -1)

if __name__ == "__main__":
    unittest.main()