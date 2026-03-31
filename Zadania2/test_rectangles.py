import unittest
from rectangles import Rectangle
from points import Point


class TestRectangle(unittest.TestCase):

    def test_str(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(str(r), "[(0, 0), (4, 3)]")

    def test_repr(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(repr(r), "Rectangle(0, 0, 4, 3)")

    def test_equality(self):
        r1 = Rectangle(0, 0, 4, 3)
        r2 = Rectangle(0, 0, 4, 3)
        r3 = Rectangle(1, 1, 4, 3)

        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_inequality(self):
        r1 = Rectangle(0, 0, 4, 3)
        r2 = Rectangle(1, 1, 4, 3)

        self.assertTrue(r1 != r2)
        self.assertFalse(r1 != Rectangle(0, 0, 4, 3))

    def test_center(self):
        r = Rectangle(0, 0, 4, 2)
        self.assertEqual(r.center(), Point(2.0, 1.0))

    def test_area(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(r.area(), 12)

    def test_move(self):
        r = Rectangle(0, 0, 4, 3)
        r.move(2, 1)
        self.assertEqual(r, Rectangle(2, 1, 6, 4))

    def test_describe(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(
            r.describe(),
            "This is a geometric shape. This is a rectangle."
        )


if __name__ == "__main__":
    unittest.main()
