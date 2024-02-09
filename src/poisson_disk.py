import math
import random
import point


class PoissonDisk:
    def __init__(self, width, height, radius, k):
        self.width = width
        self.height = height
        self.radius = radius
        self.radius2 = radius * radius
        self.k = k
        self.R = 3 * self.radius2
        self.cellSize = self.radius / math.sqrt(2)
        self.gridWidth = math.ceil(width / self.cellSize)
        self.gridHeight = math.ceil(height / self.cellSize)
        self.grid = {i: {} for i in range(self.gridWidth * self.gridHeight)}
        self.queue = []
        self.samples = []

    def far(self, x, y):
        i = int(x / self.cellSize)
        j = int(y / self.cellSize)
        i0 = max(i - 2, 0)
        j0 = max(j - 2, 0)
        i1 = min(i + 3, self.gridWidth)
        j1 = min(j + 3, self.gridHeight)

        for jj in range(j0, j1):
            for ii in range(i0, i1):
                if self.grid[jj * self.gridWidth + ii]:
                    for s in self.grid[jj * self.gridWidth + ii].values():
                        dx = s.x - x
                        dy = s.y - y
                        if dx * dx + dy * dy < self.radius2:
                            return False
        return True

    def sample(self, x, y):
        new_point = point.Point(x, y)
        self.samples.append(new_point)
        cell_x = int(x / self.cellSize)
        cell_y = int(y / self.cellSize)
        cell_index = cell_y * self.gridWidth + cell_x
        if cell_index not in self.grid:
            self.grid[cell_index] = {}
        self.grid[cell_index][len(self.grid[cell_index])] = new_point
        self.queue.append(new_point)

    def generate_candidates(self):
        if not self.queue:
            return
        i = random.randrange(len(self.queue))
        s = self.queue[i]
        for _ in range(self.k):
            a = 2 * math.pi * random.random()
            r = math.sqrt(random.random() * self.R + self.radius2)
            x = s.x + r * math.cos(a)
            y = s.y + r * math.sin(a)
            if 0 <= x < self.width and 0 <= y < self.height and self.far(x, y):
                self.sample(x, y)
        self.queue.pop(i)

    def poisson_disk_sampling(self):
        x = random.random() * self.width
        y = random.random() * self.height
        self.sample(x, y)
        while self.queue:
            self.generate_candidates()
