class Polygone:

    def __init__(self, points):
        self.points = points[:]
        self.length = len(points)

    def get_points(self):
        return self.points

    def add_points(self, points_list):
        for point in points_list:
            for polygone_points in self.points:
                if point.equals_to(polygone_points):
                    self.points.append(point)
