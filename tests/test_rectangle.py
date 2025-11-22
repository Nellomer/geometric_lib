import unittest
from rectangle import * 

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, -2)

    def test_square_area(self):
        res = rectangle_area(20, 20)
        self.assertEqual(res, 400)

    def test_simple_area(self):
        res = rectangle_area(3,9)
        self.assertEqual(res, 27)

    def test_float_area(self):
        res = rectangle_area(2.5, 4.2)
        self.assertEqual(res, 10.5)

    def test_negative_area(self):
        res = rectangle_area(-2, -7)
        self.assertEqual(res, -1)

    def test_allzero_perimeter(self):
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, -2)
    
    def test_onezero_perimeter(self):
        res = rectangle_perimeter(5, 0)
        self.assertEqual(res, -2)

    def test_simple_perimeter(self):
        res = rectangle_perimeter(10, 6)
        self.assertEqual(res, 32)

    def test_negative_perimeter(self):
        res = rectangle_perimeter(-10, 5)
        self.assertEqual(res, -1)

if __name__ == "__main__":
    unittest.main()