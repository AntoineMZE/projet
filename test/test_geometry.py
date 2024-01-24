import unittest

from src.geometry import calculate_vector


class MyTestCase(unittest.TestCase):
    def test_calculate_vector(self):
        coord_1 = (0, 0)
        coord_2 = (2, 2)
        result_1 = (2, 2)
        self.assertEqual(calculate_vector(coord_1, coord_2), result_1)

        coord_3 = (-3, 6)
        coord_4 = (4, -1)
        self.assertEqual(calculate_vector(coord_3, coord_4), (7, -7))


if __name__ == '__main__':
    unittest.main()
