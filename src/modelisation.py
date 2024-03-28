import math
from math import *
from typing import Tuple, Any, Dict
import pygame
import pygame_menu
import point
import polygon
from input_manager import InputManager
from src import poisson_disk
from src.pygame_PoissonDisk import PygamePoissonDisk
from src.poisson_disk import PoissonDisk

CERCLE_RADIUS = 10


class Modelisation:

    def __init__(self):
        self.poisson_disk = None
        self.is_in_menu = None
        self.y = 200
        self.x = 200
        self.selected_taille = 75
        self.selected_polygon = 3
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 10)
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = pygame.display.set_mode((1300, 800))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption("Modélisation algorithme de visibilité")
        self.p1 = point.Point(100, 100)
        self.p2 = point.Point(50, 200)
        self.p3 = point.Point(150, 200)
        self.point_list = [(self.p1.x, self.p1.y), (self.p2.x, self.p2.y), (self.p3.x, self.p3.y)]
        # self.t1 = polygon.Polygon.create_regular_polygon(3)
        self.cercle = pygame.image.load('image/white-circle-free-png.png').convert_alpha()
        self.rect = self.cercle.get_rect()
        self.play_button_clicked = False

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

    def set_running(self, running: bool) -> None:
        self.running = running

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
        menu = pygame_menu.Menu('Main Menu Of Visibility Algorithm', self.width / 1.25, self.height / 1.5,
                                theme=pygame_menu.themes.THEME_SOLARIZED)
        menu.add.button('Play', self.on_play_button_click)
        menu.add.selector('Type de polygone: ',
                          [('Triangle', 3), ('Quadrilatère', 4), ('Pentagone', 5), ('Hexagone', 6)],
                          onchange=self.polygon_value)
        menu.add.selector('Taille du polygone :',
                          [('75', 75), ('100', 100), ('125', 125), ('150', 150), ('175', 175), ('200', 200)],
                          onchange=self.taille_value)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def escape_menu(self):
        """Menu echap"""
        return
        # FIXME: menu doesn't work
        menu = pygame_menu.Menu('Pause Menu', self.width / 1.25, self.height / 1.5,
                                theme=pygame_menu.themes.THEME_SOLARIZED)
        menu.add.button('Resume', self.on_play_button_click)
        menu.add.button('Return to menu', self.menu_generator)

        def _exit():
            self.running = False
            pygame_menu.events.EXIT()

        menu.add.button('Quit', _exit)
        menu.draw(self.screen)

    def generer_grille_polygones(self, nombre_cotes, taille_polygone):
        positions = []
        rayon = int(taille_polygone * 1.25)
        espacement_entre_polygones = int(taille_polygone * 5)  # Ajustez selon vos préférences

        for x in range(rayon, self.screen.get_width(), espacement_entre_polygones):
            for y in range(rayon, self.screen.get_height(), espacement_entre_polygones):
                positions.append((x, y))
        return positions

    def _draw_visibility(self, light: pygame.Vector2, polygons: list):
        """
        Calculate the angles where walls begin or end.
        Cast a ray from the center along each angle.
        Fill in the triangles generated by those rays.
        """
        # sort clockwise order polygons
        def polygon_angle(polygon):
            x, y = polygon.get_center()
            return math.atan2(light.y - y, light.x - x) * 180 / math.pi
        polygons_cw = sorted(polygons, key=polygon_angle)

        # loop troughts all points
        wall_angles_start_stop = []
        for pi, polygon in enumerate(polygons_cw):
            x, y = polygon.get_center()
            ray_center = pygame.Vector2(x - light.x, y - light.y)
            points = polygon.get_points()

            id_surf = self.font.render(str(pi), False, (0,0,0))
            self.screen.blit(id_surf, (x, y))

            for i, pa in enumerate(points):
                pb = points[(i + 1) % len(points)]
                # cast to pygame Vector 2
                pa = pygame.Vector2(pa[0], pa[1])
                pb = pygame.Vector2(pb[0], pb[1])

                # calculate
                segment = (pb - pa).normalize()
                normal = pygame.Vector2(segment.y, -segment.x)

                # backface
                if normal.dot(ray_center) > 0:
                    continue

                # wall visible (large check)
                p_angle = polygon_angle(polygon)
                visible = True
                for wi, (start_a, end_a, start_d, end_d) in enumerate(wall_angles_start_stop):
                    if start_a < p_angle < end_a:
                        # wall is behind
                        if ray_center.length() < min(start_d, end_d):
                            visible = False
                        # wall is in front
                        else:
                            wall_angles_start_stop.pop(wi)
                            break

                if visible:
                    # edges
                    ray_a = (pa - light).normalize()
                    distance_from_point_a = (pa - light).length()
                    ray_a_angle = math.atan2(ray_a.y, ray_a.x) * 180 / math.pi
                    ray_b = (pb - light).normalize()
                    distance_from_point_b = (pb - light).length()
                    ray_b_angle = math.atan2(ray_b.y, ray_b.x) * 180 / math.pi

                    # more precise
                    for wi, (start_a, end_a, start_d, end_d) in enumerate(wall_angles_start_stop):
                        if start_a < ray_a_angle < end_a:
                            visible = False
                            if distance_from_point_a < min(start_d, end_d):
                                ray_a_angle = start_a
                                distance_from_point_a = start_d
                            else:
                                wall_angles_start_stop[wi] = (start_a, end_a, distance_from_point_a, end_d)
                        if start_a < ray_b_angle < end_a:
                            visible = False
                            if distance_from_point_b < min(start_d, end_d):
                                ray_b_angle = end_a
                                distance_from_point_b = end_d
                            else:
                                wall_angles_start_stop[wi] = (start_a, end_a, start_d, distance_from_point_b)

                    if visible:
                        wall_angles_start_stop.append(
                            (ray_a_angle, ray_b_angle, distance_from_point_a, distance_from_point_b))

            # draw lines to visible walls
            for start_a, end_a, start_dist, end_dist in wall_angles_start_stop:
                ray_a = light + pygame.Vector2(math.cos(start_a * math.pi / 180), math.sin(start_a * math.pi / 180)) * start_dist
                ray_b = light + pygame.Vector2(math.cos(end_a * math.pi / 180), math.sin(end_a * math.pi / 180)) * end_dist
                pygame.draw.line(self.screen, "white", light, ray_a)
                pygame.draw.line(self.screen, "white", light, ray_b)

                # triangles
                # pygame.draw.polygon(self.screen, (255, 255, 255), [light, ray_a, ray_b])

    def on_play_button_click(self):
        self.play_button_clicked = True
        # generation des polygones d'apres poisson
        self.poisson_disk = PoissonDisk(1300, 800, self.selected_taille * 2, 150)
        self.poisson_disk.poisson_disk_sampling()
        polygons = []
        for sample in self.poisson_disk.samples:
            vertices = polygon.Polygon.create_regular_polygon(self.selected_polygon,
                                                              self.selected_taille, self.selected_taille,
                                                              angle=180, pos=(sample.x, sample.y))
            polygons.append(vertices)

        # lampe
        cercle_pos = pygame.Vector2(self.screen.get_width() * .5, self.screen.get_height() * .5)
        cercle_selected = False
        self.is_in_menu = False
        was_pressed = False
        # C'est ici que se passe toute la modélisation sur la fenêtre de jeu
        while self.game_start():
            self.update()
            if not was_pressed and InputManager.is_key_down(pygame.K_ESCAPE):
                self.is_in_menu = not self.is_in_menu
            was_pressed = InputManager.is_key_down(pygame.K_ESCAPE)

            # efface l'écran
            self.screen.fill((0, 0, 0))
            # dessiner les polygons + poisson
            self.draw_points(self.poisson_disk.samples)
            circle_collide = False
            for vertices in polygons:
                if vertices.distance_from_edge(cercle_pos.x, cercle_pos.y, debug_ctx=self.screen) < 0:
                    pygame.draw.polygon(self.screen, "red", vertices.get_points())
                    circle_collide = True
                else:
                    pygame.draw.polygon(self.screen, "aqua", vertices.get_points())
            # visibilité
            self._draw_visibility(cercle_pos, polygons)

            # dessiner le cercle
            pygame.draw.circle(self.screen, ((200, 0, 0) if circle_collide else "white"), (cercle_pos.x, cercle_pos.y),
                               radius=CERCLE_RADIUS)
            # menu
            if self.is_in_menu:
                cercle_selected = False
                pygame.event.wait(pygame.K_ESCAPE)
                self.escape_menu()
            else:
                # deplacer le cercle
                if InputManager.is_button_down(pygame.BUTTON_LEFT):
                    dist = (InputManager.get_mouse_pos() - cercle_pos).length()
                    if dist < CERCLE_RADIUS:
                        cercle_selected = True
                elif InputManager.is_button_up(pygame.BUTTON_LEFT) and cercle_selected:
                    cercle_selected = False
                if cercle_selected:
                    cercle_pos = InputManager.get_mouse_pos()

            pygame.display.update()
        self.clock.tick(60)

        # fin de pygame
        pygame.quit()


if __name__ == "__main__":
    theApp = Modelisation()
    theApp.menu_generator()
