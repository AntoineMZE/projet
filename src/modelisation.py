import pygame
import point
import polygon


class Modelisation:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Modélisation algorithme de visibilité")
        self.p1 = point.Point(10, 20)
        self.p2 = point.Point(600, 600)
        self.p3 = point.Point(400, 750)
        self.point_list = [(self.p1.x, self.p1.y), (self.p2.x, self.p2.y), (self.p3.x, self.p3.y)]
        self.t1 = polygon.Polygon(self.point_list)

    def number_of_points(self):
        # Ici sera mis à jour le nombre de cotes du polygon chosis par le joueur
        pass

    def polygon_value(self):
        # Ici sera créé le polygon en fonction de son nombre de coté
        pass

    def create_polygon(self):
        # Ici sera créé un nombre de polygon équidistant les uns des autres avec le bon nombre de côté
        pass

    def draw(self):
        # C'est ici que se passe toute la modélisation sur la fenêtre de jeu
        while self.running:
            # Ici tant qu'on a pas appuyé sur la croix pour fermé la fenêtre, on crée un polygon avec une
            # liste de points définies dans init. On update ensuite la fenêtre pour que cela s'affiche correctement
            pygame.draw.polygon(self.screen, color="white", points=self.t1.get_points())
            pygame.display.update()
            # Cette boucle for permet de prendre tous les evenements de pygame, et nous permet
            # de sélectionner celui qu'on a besoin pour une action. Ici pygame.QUIT sert à enlever la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


pygame.quit()

if __name__ == "__main__":
    theApp = Modelisation()
    theApp.draw()
