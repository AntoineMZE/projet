class Polygon:

    def __init__(self, points):
        self.points = points[:]
        self.length = len(points)

    def get_points(self):
        return self.points

    def add_points(self, points_list):
        same_point_in_list = []
        for point in points_list:
            for polygon_point in self.points:
                same_point_in_list.append(point.equals_to(polygon_point))
            if True not in same_point_in_list:
                self.points.append(point)

    def supp_points(self, points_list):
        for point in points_list:
            if point in self.get_points():
                self.points.remove(point)
