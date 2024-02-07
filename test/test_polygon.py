import unittest
from src.point import Point
from src.polygon import Polygon


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Point(7.0, 4.0)
        self.p2 = Point(3.0, 8.0)
        self.p3 = Point(2.0, 1.0)
        self.p4 = Point(3.0, 3.0)
        self.p5 = Point(3.0, 0.0)
        self.list_of_3points = [self.p1, self.p2, self.p3]
        self.polygon1 = Polygon(self.list_of_3points)

    def test_get_points(self):
        self.assertEqual(self.polygon1.get_points(), self.list_of_3points)

    def test_add_points(self):
        self.polygon1.add_points([self.p4, self.p5])
        self.assertEqual(self.polygon1.get_points(), [self.p1, self.p2, self.p3, self.p4, self.p5])
        self.polygon1.add_points([self.p5])
        self.assertEqual(self.polygon1.get_points(), [self.p1, self.p2, self.p3, self.p4, self.p5])
        p6 = Point(3.0, 0.0)
        self.polygon1.add_points([p6])
        self.assertEqual(self.polygon1.get_points(), [self.p1, self.p2, self.p3, self.p4, self.p5])

    def test_supp_points(self):
        self.polygon1.add_points([self.p4, self.p5])
        self.assertEqual(self.polygon1.get_points(), [self.p1, self.p2, self.p3, self.p4, self.p5])
        self.polygon1.supp_points([self.p5])
        self.assertEqual(self.polygon1.get_points(), [self.p1, self.p2, self.p3, self.p4])

if __name__ == '__main__':
    unittest.main()
