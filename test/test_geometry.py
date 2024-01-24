import unittest


class MyTestCase(unittest.TestCase):
    def test_distance(self):
        coord_1 = (0, 0)
        coord_2 = (2, 2)
        self.assertEqual(distance(coord_1,coord_2), (2, 2))

        coord_3 = (-3, 6)
        coord_4 = (4, -1)
        self.assertEqual(distance(coord_3, coord_4), (7, -7))



if __name__ == '__main__':
    unittest.main()
