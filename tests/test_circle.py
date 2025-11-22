import unittest
import math
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_simple_area(self):
        res = circle_area(5)
        self.assertEqual(res, 25 * math.pi) 
        
    def test_negative_area(self):
        res = circle_area(-3)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_simple_perimeter(self):
        res = circle_perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_negative_perimeter(self):
        res = circle_perimeter(-5)
        self.assertEqual(res, 0)
    
if __name__ == "__main__":
    unittest.main()
