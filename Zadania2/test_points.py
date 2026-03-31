import unittest
from points import Point
import math


class TestPoint(unittest.TestCase):

    def test_init_and_str(self):
        p = Point(2, 3)
        self.assertEqual(str(p), "(2, 3)")

    def test_repr(self):
        p = Point(2, 3)
        self.assertEqual(repr(p), "Point(2, 3)")

    def test_equality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(2, 3)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_inequality(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertTrue(p1 != p2)
        self.assertFalse(p1 != Point(1, 2))

    def test_addition(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 + p2
        self.assertEqual(result, Point(4, 6))

    def test_subtraction(self):
        p1 = Point(5, 7)
        p2 = Point(2, 3)
        result = p1 - p2
        self.assertEqual(result, Point(3, 4))

    def test_dot_product(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 * p2
        self.assertEqual(result, 11)

    def test_length(self):
        p = Point(3, 4)
        self.assertEqual(p.length(), 5)

    def test_length_float(self):
        p = Point(1, 1)
        self.assertAlmostEqual(p.length(), math.sqrt(2))


if __name__ == "__main__":
    unittest.main()
