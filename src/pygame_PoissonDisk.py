import pygame
from typing import List, Tuple
from src.triangulation import *
from src.poisson_disk import PoissonDisk



class PygamePoissonDisk:
    def __init__(self, width, height, debug=False):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.bg_color = (0, 0, 0)
        self.point_color = (255, 255, 255)
        self.point_radius = 2
        self.running = True
        self.debug = debug

    def draw_points(self, points):
        self.screen.fill(self.bg_color)
        for point in points:
            pygame.draw.circle(self.screen, self.point_color, (int(point.x), int(point.y)), self.point_radius)
        pygame.display.flip()

    def draw_triangles(self, triangles):
        for triangle in triangles:
            pygame.draw.polygon(self.screen, (255, 0, 0), [(p.x, p.y) for p in triangle],
                                1)  # Dessine le triangle en rouge
            if self.debug:
                print("Triangle:", [(p.x, p.y) for p in triangle])  # Afficher les coordonnées du triangle
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def clear_screen(self):
        self.screen.fill(self.bg_color)

    def update_display(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)

    @staticmethod
    def close():
        pygame.quit()

    @staticmethod
    def triangulate_points(points: List[Tuple[float, float]]) -> List[
        Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]]]:
        """
        Triangule un ensemble de points en utilisant la classe Triangulation.
        """
        triangulation = Triangulation(points)
        return triangulation.triangulate()

    @staticmethod
    def convex_hull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        # Si vous avez besoin de redéfinir la méthode convex_hull ici pour quelque raison, vous pouvez le faire
        pass

    def run(self):
        poisson_disk = PoissonDisk(self.width, self.height, 50, 30)
        poisson_disk.poisson_disk_sampling()

        while self.running:
            self.handle_events()

            self.clear_screen()
            self.draw_points(poisson_disk.samples)

            # Trianguler et afficher les triangles
            triangles = self.triangulate_points(poisson_disk.samples)
            self.draw_triangles(triangles)

            self.update_display()

        self.close()


if __name__ == "__main__":
    pygame_renderer = PygamePoissonDisk(800, 600, debug=True)
    pygame_renderer.run()
