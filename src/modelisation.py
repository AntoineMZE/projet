import math
from typing import Tuple, Any

import pygame
import pygame_menu
import point
import polygon
from input_manager import InputManager
from src import poisson_disk
from src.pygame_PoissonDisk import PygamePoissonDisk
from src.poisson_disk import PoissonDisk



class Modelisation:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((800, 800))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption("Modélisation algorithme de visibilité")
        self.p1 = point.Point(10, 20)
        self.p2 = point.Point(200, 100)
        self.p3 = point.Point(150, 250)
        self.point_list = [(self.p1.x, self.p1.y), (self.p2.x, self.p2.y), (self.p3.x, self.p3.y)]
        self.t1 = polygon.Polygon(self.point_list)
        self.cercle = pygame.image.load('image/white-circle-free-png.png').convert_alpha()
        self.rect = self.cercle.get_rect()
        self.poisson_disk = PoissonDisk(800, 800, 150, 50)
        self.poisson_disk.poisson_disk_sampling()

    def game_start(self):
        return self.running

    def number_of_points(self, selected: Tuple, value: Any) -> None:
        # Ici sera mis à jour le nombre de cotes du polygon chosis par le joueur
        print(f'Le nombre de cotés du polygon sera de {selected[0]} ({value})')

    def polygon_value(self):
        # Ici sera créé le polygon en fonction de son nombre de coté
        pass

    def create_polygon(self):
        # Ici sera créé un nombre de polygon équidistant les uns des autres avec le bon nombre de côté
        pass

    def draw_points(self, points):
        # self.screen.fill("black")
        for point in points:
            pygame.draw.circle(self.screen, "white", (int(point.x), int(point.y)), 2)
        # pygame.display.flip()

    def update(self):
        # Cette boucle for permet de prendre tous les evenements de pygame, et nous permet
        # de sélectionner celui qu'on a besoin pour une action. Ici pygame.QUIT sert à enlever la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                InputManager.update(event)  # met à jour le dictionnaire des touches et boutons suivant les evenements

    def menu_generator(self):
        menu = pygame_menu.Menu('Hello', self.width / 1.5, self.height / 1.5,
                                theme=pygame_menu.themes.THEME_SOLARIZED)
        menu.add.button('Play', self.on_play_button_click)
        menu.add.selector('Type de polygone: ', [('Triangle', 3), ('Carré', 4)], onchange=self.number_of_points)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def on_play_button_click(self):
        cercle_pos = pygame.Vector2(400, 400)
        cercle_offset = pygame.Vector2(self.cercle.get_width(), self.cercle.get_height()) * .5
        cercle_selected = False
        mouse_down = False
        # C'est ici que se passe toute la modélisation sur la fenêtre de jeu
        while self.game_start():

            self.update()
            # efface l'ecran
            self.screen.fill((0, 0, 0))
            self.draw_points(self.poisson_disk.samples)
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
    theApp.menu_generator()
    theApp.on_play_button_click()
