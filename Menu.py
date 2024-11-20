import sys

import pygame

from Button import Button
from Slider import Slider


class Menu:
    def __init__(self, width, height, margin_right, speed):
        self.width = width
        self.height = height
        self.margin_right = margin_right
        self.surface = pygame.Surface((margin_right, height))

        self.font = pygame.font.Font(None, 36)
        self.menu_items = ["Play / Pause", "Restart", "Change algo", "Exit"]

        self.buttons = []  # liste des boutons
        for index, item in enumerate(self.menu_items):
            pos = (self.margin_right // 2, 50 + index * 40)
            button = Button(item, pos, self.font)
            self.buttons.append(button)

        self.game_speed = speed
        self.speed_slider = Slider("Delay (ms)", self.font, 20, height - 50, margin_right - 40, 10, 1, 1000, speed)

        self.paused = True
        self.restarted = True
        self.ended = False
        self.algo_m = False

    def draw(self, screen):
        self.surface.fill((150, 150, 150))
        for button in self.buttons:
            button.draw(self.surface)

        self.speed_slider.draw(self.surface)

        screen.blit(self.surface, (self.width - self.margin_right, 0))

    def handle_event(self, event):
        mouse_x, mouse_y = event.pos
        # Ajuster la position de la souris pour correspondre aux coordonnées du menu
        mouse_x -= self.width - self.margin_right
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.speed_slider.is_clicked((mouse_x, mouse_y)):
                self.speed_slider.handle_event(event, mouse_x)
                return

            for button in self.buttons:
                if button.is_clicked((mouse_x, mouse_y)):
                    self.handle_action(button.text)
                    return
        if event.type in {pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP}:
            self.speed_slider.handle_event(event, mouse_x)
            return


    def handle_action(self, button_text):
        if button_text == "Play / Pause":
            self.paused = not self.paused

        elif button_text == "Restart":
            self.restarted = True

        elif button_text == "Change algo":
            print('algo changé')
            self.algo_m = not self.algo_m

        elif button_text == "Exit":
            pygame.quit()
            sys.exit()
