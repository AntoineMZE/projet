import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

    def equals_to(self, other_point):
        return self.x == other_point.x and self.y == other_point.y
