import math
from typing import Tuple


##class Geometry:
def calculate_vector(coord_1: Tuple, coord_2: Tuple):
    """
            Calculate Vector between two points in 2D space.

            :param coord_1: Tuple -- (x, y) coords of first point
            :param coord_2: Tuple -- (x, y) coords of second p
            :return: Tuple -- Vector between two points
        """
    vector = (coord_2[0] - coord_1[0], coord_2[1] - coord_1[1])
    return vector


def calculate_norm(vect_1: Tuple):
    return math.sqrt(vect_1[0] ** 2 + vect_1[1] ** 2)
