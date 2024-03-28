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
