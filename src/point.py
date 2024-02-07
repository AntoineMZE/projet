import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        # Permet de faire bouger des points à un autre endroit en changeant leur valeur
        self.x = x
        self.y = y

    def distance(self, other_point):
        # Calcule la distance entre 2 points
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

    def equals_to(self, other_point):
        # Vérifie si les 2 points sont les mêmes ou non
        return self.x == other_point.x and self.y == other_point.y
