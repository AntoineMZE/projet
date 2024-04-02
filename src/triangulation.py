from typing import List, Tuple
from point import Point


class Triangulation:
    def __init__(self, points: List[Point]):
        self.points = points

    @staticmethod
    def orientation(p1: Point, p2: Point, p3: Point) -> int:
        val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
        if abs(val) < 1e-9:  # Utiliser une petite valeur seuil
            return 0
        elif val > 0:
            return 1
        else:
            return -1

    @staticmethod
    def convex_hull(points: List[Point]) -> List[Point]:
        n = len(points)
        if n < 3:
            return []

        hull = []

        l = min(points)
        hull.append(l)

        p = l
        while True:
            q = points[0]  # Initialiser q avec le premier point dans la liste
            for i in range(n):
                if points[i] == p:
                    continue
                if Triangulation.orientation(p, points[i], q) == -1:
                    q = points[i]
            p = q
            if p == hull[0]:
                break
            hull.append(p)
        return hull

    @staticmethod
    def point_inside_triangle(p: Point, p1: Point, p2: Point, p3: Point) -> bool:
        def sign(pt1: Point, pt2: Point, pt3: Point) -> float:
            return (pt1.x - pt3.x) * (pt2.y - pt3.y) - (pt2.x - pt3.x) * (pt1.y - pt3.y)

        b1 = sign(p, p1, p2) < 0.0
        b2 = sign(p, p2, p3) < 0.0
        b3 = sign(p, p3, p1) < 0.0

        return (b1 == b2) and (b2 == b3)

    def triangulate(self) -> List[Tuple[Point, Point, Point]]:
        convex_hull_points = self.convex_hull(self.points)
        triangles = []
        for i in range(len(convex_hull_points) - 2):
            p1 = convex_hull_points[i]
            p2 = convex_hull_points[i + 1]
            p3 = convex_hull_points[i + 2]
            for p in self.points:
                if p != p1 and p != p2 and p != p3 and self.orientation(p1, p2,
                                                                        p3) == -1 and self.point_inside_triangle(p, p1,
                                                                                                                 p2,
                                                                                                                 p3):
                    triangles.append((p1, p2, p3))
                    break  # Sortir de la boucle dès qu'un triangle est trouvé
        return triangles
