class Polygon:

    def __init__(self, points):
        self.points = points[:]
        self.length = len(points)

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
