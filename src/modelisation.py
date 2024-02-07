import pygame
import point
import polygon



class Modelisation:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 800))

    def draw(self):

        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     self.running= False


pygame.quit()

if __name__ == "__main__" :
    theApp = Modelisation()
    theApp.draw()