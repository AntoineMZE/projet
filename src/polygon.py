from math import *
import pygame

DEBUG = False


class Polygon:

    def __init__(self, points):
        self.points = points[:]
        self.length = len(points)

    @staticmethod
    def create_regular_polygon(n_faces, width=1, height=1, angle=0, pos=(0, 0)):
        points = []
        a_step = 2 * pi / n_faces
        a = angle
        px, py = pos
        for i in range(n_faces):
            x = px + cos(a) * width
            y = py + sin(a) * height
            points.append((x, y))
            a += a_step
        return Polygon(points)

    def get_points(self):
        # Renvoie la liste de points du polygon
        return self.points

    def add_points(self, points_list):
        # Ajoute un ou plusieurs points dans la liste déjà existante si ces derniers n'y sont pas déjà
        same_point_in_list = []
        for point in points_list:
            for polygon_point in self.points:
                same_point_in_list.append(point.equals_to(polygon_point))
            if True not in same_point_in_list:
                self.points.append(point)

    def supp_points(self, points_list):
        # Supprime un ou plusieurs dans la liste déjà existante si ces derniers existent dans la liste
        for point in points_list:
            if point in self.get_points():
                self.points.remove(point)

    def get_center(self):
        """Retourne le centre sur la moyenne des positions"""
        x_sum = 0
        y_sum = 0
        for x, y in self.points:
            x_sum += x
            y_sum += y
        return x_sum / len(self.points), y_sum / len(self.points)

    def distance_from_edge(self, x, y, debug_ctx=None):
        """Retourne la distance la plus proche à un segment du polygone"""
        centerx, centery = self.get_center()
        closest = sqrt((x - centerx) ** 2 + (y - centery) ** 2)  # distance au centre naive
        inside = True
        for i, pa in enumerate(self.get_points()):
            pb = self.points[(i + 1) % len(self.points)]
            segment = pygame.Vector2(pb[0] - pa[0], pb[1] - pa[1])  # fin - debut = vec2(a b)
            normal = pygame.Vector2(segment.y, -segment.x).normalize()  # vec2(b -a)
            distance = normal.dot((x - pa[0], y - pa[1]))

            # debug utility
            if debug_ctx is not None and DEBUG:
                segment_middle_point = pygame.Vector2((pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2)
                end_pos = segment_middle_point + normal * 50
                pygame.draw.line(debug_ctx, "white", segment_middle_point, end_pos, width=1)
                pygame.draw.circle(debug_ctx, "red", segment_middle_point + normal * distance, 3)

            # distance check
            inside = inside and (distance < 0)
            if 0 < distance < closest:
                closest = distance
        if inside:
            return -1  # ignore distance
        return closest

    def intersects(self, p1: pygame.Vector2, p2: pygame.Vector2) -> pygame.Vector2 | None:
        for i, pa in enumerate(self.get_points()):
            pb = self.points[(i + 1) % len(self.points)]
            p3 = pygame.Vector2(pb[0], pb[1])
            p4 = pygame.Vector2(pa[0], pa[1])

            normal = pygame.Vector2(p4.y - p3.y, -(p4.x - p3.x)).normalize()
            if normal.dot((p2 - p1).normalize()) > 0:
                continue

            # D: slope.x * x + slope.y * y + origin = 0
            # slope_a = pygame.Vector2((p2.y - p1.y), (p2.x - p1.x))
            # origin_a = (slope_a.y / slope_a.x) * p1.x - p1.y
            # slope_b = pygame.Vector2((p4.y - p3.y), (p4.x - p3.x))
            # origin_b = (slope_b.y / slope_b.x) * p3.x - p3.y
            #
            x_0 = (p1.y - p3.y)
            x_1 = (p4.y - p3.y)
            x_2 = (p1.x - p3.x)
            x_3 = (p2.x - p1.x)
            x_4 = (p2.y - p1.y)
            x_5 = (p4.x - p3.x)

            s = ((x_5 * x_0 - x_1 * x_2) / (x_1 * x_3 - x_5 * x_4))
            p = pygame.Vector2(p1.x + s * x_3, p1.y + s * x_4)

            minx = min(p3.x, p4.x)
            maxx = max(p3.x, p4.x)
            miny = min(p3.y, p4.y)
            maxy = max(p3.y, p4.y)
            if minx <= p.x <= maxx and miny <= p.y <= maxy:
                return p
        return pygame.Vector2(0, 0)
