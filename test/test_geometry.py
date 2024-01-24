import unittest
import math
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

    def test_norm(self):
        vect_1 = (4, 5)
        self.assertEqual(calculate_norm(vect_1), math.sqrt(41))
        vect_2 = (7, 4)
        self.assertEqual(calculate_norm(vect_2), math.sqrt(65))


if __name__ == '__main__':
    unittest.main()
