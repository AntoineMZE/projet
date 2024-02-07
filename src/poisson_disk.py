import math
import random

from src.point import Point


class PoissonDisk:
    def __init__(self, cell_height, cell_width, nb_points, radius):
        self.dimension = 2
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.nb_points = nb_points
        self.radius = radius
        self.radius2 = radius ** 2
        self.queue = []
        self.queue_size = 0
        self.sample_size = 0
        self.cellSize = radius / math.sqrt(2)
        self.grid = [None] * (self.cell_height * self.cell_width)

        def return_function():
            if not self.sample_size:
                return sample(random.random() * self.cell_width, random.random() * self.cell_height)

            # Pick a random existing sample and remove it from the queue.
            while self.queue_size < self.nb_points:
                i = random.randrange(0, self.queue_size)
                s = self.queue[i]

                # Make a new candidate between [radius, 2 * radius] from the existing sample.
                for j in range(i + 1, self.nb_points):
                    a = 2 * math.pi * random.random()
                    r = math.sqrt(random.random() * (3 * self.radius2) + self.radius2)
                    x = s[0] + r * math.cos(a)
                    y = s[1] + r * math.sin(a)

                    # Reject candidates that are outside the allowed extent,
                    # or closer than 2 * radius to any existing sample.
                    if 0 <= x < self.cell_width and 0 <= y < self.cell_height and far(x, y):
                        return sample(x, y)

                self.queue[i] = self.queue[--self.queue_size]

        def far(x, y):
            i = x / self.cellSize | 0
            j = y / self.cellSize | 0
            i0 = max(i - 2, 0)
            j0 = max(j - 2, 0)
            i1 = min(i + 3, self.cell_width)
            j1 = min(j + 3, self.cell_height)
            s = Point(x, y)

            for j in range(j0, j1):
                o = j * self.cell_width
                for i in range(i0, i1):
                    if s == self.grid[o + i]:
                        dx = s[0] - x
                        dy = s[1] - y
                        if dx * dx + dy * dy < self.radius2:
                            return False

        def sample(x, y):
            new_point = Point(x, y)
            self.queue.append(new_point)
            self.sample_size += 1
            self.queue_size += 1
            return new_point
