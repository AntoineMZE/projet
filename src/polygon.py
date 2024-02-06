class Polygon:

    def __init__(self, points):
        self.points = points[:]
        self.length = len(points)

    def get_points(self):
        return self.points

    def add_points(self, points_list):
        for point in points_list:
            if point not in self.get_points():
                self.points.append(point)

    def supp_points(self, points_list):
        for point in points_list:
            if point in self.get_points():
                self.points.remove(point)
