from math import *
from typing import Tuple, Any, Dict
## K_ESCAPE
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
        self.selected_taille = None
        self.selected_polygon = None
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((800, 800))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption("Modélisation algorithme de visibilité")
        self.p1 = point.Point(100, 100)
        self.p2 = point.Point(50, 200)
        self.p3 = point.Point(150, 200)
        self.point_list = [(self.p1.x, self.p1.y), (self.p2.x, self.p2.y), (self.p3.x, self.p3.y)]
        ## self.t1 = polygon.Polygon.create_regular_polygon(3)
        self.cercle = pygame.image.load('image/white-circle-free-png.png').convert_alpha()
        self.rect = self.cercle.get_rect()
        self.poisson_disk = PoissonDisk(800, 800, 150, 50)
        self.poisson_disk.poisson_disk_sampling()

    def game_start(self):
        return self.running

    def number_of_points(self, selected: Tuple, value: Any) -> [str, int]:
        # Ici sera mis à jour le nombre de cotes du polygon chosis par le joueur
        print(f'Le nombre de cotés du polygon sera de {selected[0]} ({value})')
        select = selected[0]
        val = value
        return select, val

    def polygon_value(self, selected: Tuple, value: Any) -> None:
        # Mise à jour de la valeur sélectionnée sans dessiner le triangle immédiatement
        self.selected_polygon = value
        return value

    def taille_value(self, selected: Tuple, value: Any) -> None:
        # Mise à jour de la valeur sélectionnée sans dessiner le triangle immédiatement
        self.selected_taille = value
        return value

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
        menu = pygame_menu.Menu('Main Menu Of Visibility Algorithm', self.width / 1.5, self.height / 1.5,
                                theme=pygame_menu.themes.THEME_SOLARIZED)
        menu.add.button('Play', self.on_play_button_click)
        menu.add.selector('Type de polygone: ',
                          [('Triangle', 3), ('Quadrilatère', 4), ('Pentagone', 5), ('Hexagone', 6)],
                          onchange=self.polygon_value)
        menu.add.selector('Taille du polygone :',
                          [('25', 25), ('50', 50), ('75', 75), ('100', 100), ('125', 125), ('150', 150), ('175', 175),
                           ('200', 200)], onchange=self.taille_value)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def escape_menu(self):
        menu = pygame_menu.Menu('Escape Menu', self.width / 1.5, self.height / 1.5,
                                theme=pygame_menu.themes.THEME_SOLARIZED)
        ## menu.add.button('Return to menu', self.menu_generator)
        menu.add.button('Quit', pygame_menu.events.EXIT)

    def update_polygon(self):
        if self.selected_polygon == 3:
            t1 = polygon.Polygon.create_regular_polygon(3, self.selected_taille, self.selected_taille, pos=(200, 200))
            pygame.draw.polygon(self.screen, color='white', points=t1.get_points())
        elif self.selected_polygon == 4:
            t1 = polygon.Polygon.create_regular_polygon(4, self.selected_taille, self.selected_taille, pos=(200, 200))
            pygame.draw.polygon(self.screen, color='white', points=t1.get_points())
        elif self.selected_polygon == 5:
            t1 = polygon.Polygon.create_regular_polygon(5, self.selected_taille, self.selected_taille, pos=(200, 200))
            pygame.draw.polygon(self.screen, color='white', points=t1.get_points())
        elif self.selected_polygon == 6:
            t1 = polygon.Polygon.create_regular_polygon(6, self.selected_taille, self.selected_taille, pos=(200, 200))
            pygame.draw.polygon(self.screen, color='white', points=t1.get_points())
        # Ajoutez d'autres conditions pour les autres valeurs si nécessaire

    def on_play_button_click(self):
        self.play_button_clicked = True
        if self.selected_polygon is not None:
            self.update_polygon()  # Actualisez la valeur du menu

        cercle_pos = pygame.Vector2(400, 400)
        cercle_offset = pygame.Vector2(self.cercle.get_width(), self.cercle.get_height()) * .5
        cercle_selected = False
        mouse_down = False
        # C'est ici que se passe toute la modélisation sur la fenêtre de jeu
        while self.game_start():

            self.update()
            if InputManager.is_key_down(27):
                self.escape_menu()

            # efface l'ecran
            self.screen.fill((0, 0, 0))
            self.draw_points(self.poisson_disk.samples)
            self.update_polygon()
            # Ici tant qu'on a pas appuyé sur la croix pour fermé la fenêtre, on crée un polygon avec une
            # liste de points définies dans init. On update ensuite la fenêtre pour que cela s'affiche correctement
            # pygame.draw.polygon(self.screen, color="white", points=self.t1.get_points())

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
