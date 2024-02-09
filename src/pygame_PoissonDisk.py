import pygame


class PygamePoissonDisk:
    def __init__(self, width, height):
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

    def draw_points(self, points):
        self.screen.fill(self.bg_color)
        for point in points:
            pygame.draw.circle(self.screen, self.point_color, (int(point.x), int(point.y)), self.point_radius)
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
