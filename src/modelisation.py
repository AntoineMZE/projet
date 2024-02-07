import pygame
import point
import polygon


class Modelisation:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 800))
        self.p1 = point.Point(10, 20)
        self.p2 = point.Point(300, 600)
        self.p3 = point.Point(100, 250)

    def draw(self):

        while self.running:
            pygame.Surface.set_at(self.screen, (self.p1.x, self.p1.y), "white")
            pygame.Surface.set_at(self.screen, (self.p2.x, self.p2.y), "white")
            pygame.Surface.set_at(self.screen, (self.p3.x, self.p3.y), "white")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


pygame.quit()

if __name__ == "__main__":
    theApp = Modelisation()
    theApp.draw()
