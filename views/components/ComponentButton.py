from typing import List

import pygame


class ComponentButton:
    def __init__(self, rect: pygame.Rect, text: str):
        self.button_rect = rect
        self.button_up = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(
            self.button_up,
            color=(0, 0, 0),
            rect=pygame.Rect(0, 0, rect.width, rect.height)
        )
        pygame.draw.rect(
            self.button_up,
            color=(255, 255, 255),
            rect=pygame.Rect(2,2, rect.width-4, rect.height-4)
        )
        self.listeners_click: List[callable] = []

    def draw(self, surface: pygame.Surface):
        surface.blit(
            self.button_up,
            (self.button_rect.x, self.button_rect.y)
        )

    def trigger_mouse(self, mouse_position, mouse_button_state):
        if any(mouse_position):
            if self.button_rect.x < mouse_position[0] < self.button_rect.x + self.button_rect.width:
                if self.button_rect.y < mouse_position[1] < self.button_rect.y + self.button_rect.height:
                    for listener in self.listeners_click:
                        listener()

    def add_listener_click(self, func_on_click):
        pass

    def remove_listener_click(self, func_on_click):
        pass