import math

import pygame
import point
import polygon
from input_manager import InputManager


class Modelisation:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Modélisation algorithme de visibilité")
        self.p1 = point.Point(10, 20)
        self.p2 = point.Point(200, 100)
        self.p3 = point.Point(150, 250)
        self.point_list = [(self.p1.x, self.p1.y), (self.p2.x, self.p2.y), (self.p3.x, self.p3.y)]
        self.t1 = polygon.Polygon(self.point_list)
        self.cercle = pygame.image.load('image/white-circle-free-png.png').convert_alpha()
        self.rect = self.cercle.get_rect()

    def number_of_points(self):
        # Ici sera mis à jour le nombre de cotes du polygon chosis par le joueur
        pass

    def polygon_value(self):
        # Ici sera créé le polygon en fonction de son nombre de coté
        pass

    def create_polygon(self):
        # Ici sera créé un nombre de polygon équidistant les uns des autres avec le bon nombre de côté
        pass

    def update(self):
        # Cette boucle for permet de prendre tous les evenements de pygame, et nous permet
        # de sélectionner celui qu'on a besoin pour une action. Ici pygame.QUIT sert à enlever la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                InputManager.update(event)  # met à jour le dictionnaire des touches et boutons suivant les evenements

    def draw(self):
        cercle_pos = pygame.Vector2(400, 400)
        cercle_offset = pygame.Vector2(self.cercle.get_width(), self.cercle.get_height()) * .5
        cercle_selected = False
        mouse_down = False
        # C'est ici que se passe toute la modélisation sur la fenêtre de jeu
        while self.running:
            self.update()
            # efface l'ecran
            self.screen.fill((0, 0, 0))
            # Ici tant qu'on a pas appuyé sur la croix pour fermé la fenêtre, on crée un polygon avec une
            # liste de points définies dans init. On update ensuite la fenêtre pour que cela s'affiche correctement
            pygame.draw.polygon(self.screen, color="white", points=self.t1.get_points())

            # bouge le cercle
            if InputManager.is_button_down(pygame.BUTTON_LEFT):
                dist = (InputManager.get_mouse_pos() - cercle_pos).length()
                if dist < self.cercle.get_width() * .5:
                    cercle_selected = True
            elif InputManager.is_button_up(pygame.BUTTON_LEFT) and cercle_selected:
                cercle_selected = False
            if cercle_selected:
                cercle_pos = InputManager.get_mouse_pos()
            self.screen.blit(self.cercle, cercle_pos - cercle_offset)

            pygame.display.update()
        self.clock.tick(60)

        # fin de pygame
        pygame.quit()

if __name__ == "__main__":
    theApp = Modelisation()
    theApp.draw()
