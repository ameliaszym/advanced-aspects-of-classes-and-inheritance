import unittest
from triangles import Triangle
from points import Point


class TestTriangle(unittest.TestCase):

    def test_str(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertEqual(str(t), "[(0, 0), (4, 0), (0, 3)]")

    def test_repr(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertEqual(repr(t), "Triangle(0, 0, 4, 0, 0, 3)")

    def test_equality(self):
        t1 = Triangle(0, 0, 4, 0, 0, 3)
        t2 = Triangle(0, 0, 4, 0, 0, 3)
        t3 = Triangle(0, 0, 4, 0, 1, 3)

        self.assertTrue(t1 == t2)
        self.assertFalse(t1 == t3)

    def test_inequality(self):
        t1 = Triangle(0, 0, 4, 0, 0, 3)
        t2 = Triangle(0, 0, 4, 0, 1, 3)

        self.assertTrue(t1 != t2)
        self.assertFalse(t1 != Triangle(0, 0, 4, 0, 0, 3))

    def test_center(self):
        t = Triangle(0, 0, 6, 0, 0, 3)
        self.assertEqual(t.center(), Point(2.0, 1.0))

    def test_area(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertEqual(t.area(), 6.0)

    def test_move(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        t.move(1, 2)
        self.assertEqual(t, Triangle(1, 2, 5, 2, 1, 5))

    def test_describe(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertEqual(
            t.describe(),
            "This is a geometric shape. This is a triangle."
        )


if __name__ == "__main__":
    unittest.main()
