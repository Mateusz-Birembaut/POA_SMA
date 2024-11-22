import pygame

import Scene
from Enums import EntityState


class Agent:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene):
        image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(image, (scene.tile_width_px, scene.tile_height_px))
        self.__tile_x = position[0]
        self.__tile_y = position[1]
        self.scene = scene
        self.state = EntityState.SEARCH

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.__tile_x * self.scene.tile_width_px, self.__tile_y * self.scene.tile_height_px))

    def process(self):
        # méthode d'action de l'agent
        # là où il prend compte de l'environnement pour décider de sa prochaine action
        pass

    def move(self):
        # méthode de mouvement de l'agent
        # là où il prend compte de l'environnement pour décider de sa prochaine action
        pass
