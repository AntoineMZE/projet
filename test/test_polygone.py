import unittest
from src.point import Point
from src.polygone import Polygone


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Point(7.0, 4.0)
        self.p2 = Point(3.0, 8.0)
        self.p3 = Point(2.0, 1.0)
        self.p4 = Point(3.0, 3.0)
        self.p5 = Point(3.0, 0.0)
        self.list_of_3points = [self.p1, self.p2, self.p3]
        self.polygone1 = Polygone(self, self.list_of_3points)

    def test_get_points(self):
        self.assertEqual(self.polygone1.get_points, self.list_of_3points)  # add assertion here

    def test_add_points(self):
        self.polygone1.add_points([self.p4, self.p5])
        self.assertEqual(self.polygone1.get_points, [self.p1, self.p2, self.p3, self.p4, self.p5])
        p6 = Point(3.0, 0.0)
        self.polygone1.add_points(p6)
        self.assertEqual(self.polygone1.get_points, [self.p1, self.p2, self.p3, self.p4, self.p5])


if __name__ == '__main__':
    unittest.main()
