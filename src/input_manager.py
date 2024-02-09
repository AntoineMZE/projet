import pygame
from pygame import Vector2


class _InputManager():
    _keystate: dict[int, int]
    _buttonstate: dict[int, int]
    _mousepos: Vector2

    def __init__(self):
        self._keystate = {}
        self._buttonstate = {}
        self._mousepos = Vector2(0, 0)

    def update(self, event: pygame.event.Event):
        if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
            self._keystate[event.dict["key"]] = event.type

        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
            self._buttonstate[event.dict["button"]] = event.type

        if event.type == pygame.MOUSEMOTION:
            self._mousepos = Vector2(event.dict["pos"][0], event.dict["pos"][1])

    def get_axis(self, key_pos: int, key_neg: int) -> int:
        return int(self.is_key_down(key_pos)) - int(self.is_key_down(key_neg))

    def is_key_up(self, key: int) -> bool:
        return self._keystate.get(key, pygame.KEYUP) == pygame.KEYUP

    def is_key_down(self, key: int) -> bool:
        return self._keystate.get(key, pygame.KEYUP) == pygame.KEYDOWN

    def is_button_down(self, button: int) -> bool:
        return self._buttonstate.get(button, pygame.MOUSEBUTTONUP) == pygame.MOUSEBUTTONDOWN

    def is_button_up(self, button: int) -> bool:
        return self._buttonstate.get(button, pygame.MOUSEBUTTONUP) == pygame.MOUSEBUTTONUP
    def get_mouse_pos(self) -> Vector2:
        return self._mousepos


# Unique instance of _InputManager
InputManager = _InputManager()
