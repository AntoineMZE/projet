import unittest
import math
from src.point import Point


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Point(7.0, 4.0)
        self.p2 = Point(3.0, 8.0)

    # end of initialisation
    def test_getX(self):
        self.assertEqual(self.p1.x, 7.0)
        self.assertEqual(self.p2.x, 3.0)

    def test_getY(self):
        self.assertEqual(self.p1.y, 4.0)
        self.assertEqual(self.p2.y, 8.0)

    def test_distance(self):
        self.assertEqual(self.p1.distance(self.p2), math.sqrt(32))
        self.assertEqual(self.p2.distance(self.p1), math.sqrt(32))

    def test_move_point(self):
        self.p1.move(5, 0)
        self.assertEqual(self.p1.x, 5)
        self.assertEqual(self.p1.y, 0)

    def test_equals_to(self):
        self.assertFalse(self.p1.equals_to(self.p2))
        p3 = Point(7.0, 4.0)
        self.assertTrue(self.p1.equals_to(p3))


if __name__ == '__main__':
    unittest.main()
