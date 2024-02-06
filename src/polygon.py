class Polygon:

    def __init__(self, points):
        self.points = points[:]
        self.length = len(points)

    def get_points(self):
        return self.points

    def add_points(self, points_list):
        for point in points_list:
<<<<<<< HEAD
            if point not in self.get_points():
                self.points.append(point)
=======
            for polygon_points in self.points:
                if point.equals_to(polygon_points):
                    self.points.append(point)
>>>>>>> 14e7302 (correction git)
