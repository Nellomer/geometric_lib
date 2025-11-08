import unittest
import math
from rectangle import * 
from circle import *
from square import *
from triangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = rectangle_area(20, 20)
        self.assertEqual(res, 400)

    def test_simple_area(self):
        res = rectangle_area(3,9)
        self.assertEqual(res, 27)

    def test_float_area(self):
        res = rectangle_area(2.5, 4.2)
        self.assertEqual(res, 10.5)

    def test_allzero_perimeter(self):
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_onezero_perimeter(self):
        res = rectangle_perimeter(5, 0)
        self.assertEqual(res, 0)

    def test_simple_perimeter(self):
        res = rectangle_perimeter(10, 6)
        self.assertEqual(res, 32)

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_simple_area(self):
        res = circle_area(5)
        self.assertEqual(res, 25 * math.pi)

    def test_zero_perimeter(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_simple_perimeter(self):
        res = circle_perimeter(10)
        self.assertEqual(res, 20 * math.pi)
    
class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_simple_area(self):
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_zero_perimeter(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_simple_perimeter(self):
        res = square_perimeter(9)
        self.assertEqual(res, 36)
    
class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle_area(4, 0)
        self.assertEqual(res, 0)

    def test_simple_area(self):
        res = triangle_area(13, 6)
        self.assertEqual(res, 39)

    def test_zero_perimeter(self):
        res = triangle_perimeter(0, 4, 3)
        self.assertEqual(res, 0)

    def test_simple_perimeter(self):
        res = triangle_perimeter(9, 10, 14)
        self.assertEqual(res, 33)

unittest.main()