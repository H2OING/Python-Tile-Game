from typing import List

import pygame


class ComponentButton:
    def __init__(self, rect: pygame.Rect, text: str, color):
        self.button_rect = rect
        self.text = text
        self.color = color
        self.button_up = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)

        pygame.draw.rect(
            self.button_up,
            color=(50, 50, 50),
            rect=pygame.Rect(0, 0, rect.width, rect.height)
        )

        pygame.draw.rect(
            self.button_up,
            color=(255, 255, 170),
            rect=pygame.Rect(2, 2, rect.width - 4, rect.height - 4)
        )

        self.listeners_click: List[callable] = []

    def draw(self, surface: pygame.Surface):
        surface.blit(
            self.button_up,
            (self.button_rect.x, self.button_rect.y)
        )

        if self.text != '':
            font = pygame.font.SysFont('italic', 40)
            text = font.render(self.text, True, (0, 0, 0))
            surface.blit(text, (
                self.button_rect.x + (self.button_rect.width / 2 - text.get_width() / 2),
                self.button_rect.y + (self.button_rect.height / 2 - text.get_height() / 2)))

    def mouse_is_over(self, mouse_position):
        if self.button_rect.x < mouse_position[0] < self.button_rect.x + self.button_rect.width:
            if self.button_rect.y < mouse_position[1] < self.button_rect.y + self.button_rect.height:
                return True

        return False

    def trigger_mouse(self, mouse_position, mouse_button):
        if any(mouse_button):
            if self.button_rect.x < mouse_position[0] < self.button_rect.x + self.button_rect.width:
                if self.button_rect.y < mouse_position[1] < self.button_rect.y + self.button_rect.height:
                    for listener in self.listeners_click:
                        listener()

    def add_listener_click(self, func_on_click):
        if func_on_click not in self.listeners_click:
            self.listeners_click.append(func_on_click)

    def remove_listener_click(self, func_on_click):
        if func_on_click not in self.listeners_click:
            self.listeners_click.append(func_on_click)


pygame.init()
