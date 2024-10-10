import pygame

import Labyrinth
import Scene


class Entity:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, labyrinth: Labyrinth, name: str):
        self.image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(self.image, (scene.tile_width_px, scene.tile_height_px))
        self.tile_x = position[0]
        self.tile_y = position[1]
        self.scene = scene
        self.labyrinth = labyrinth
        self.name = name

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.tile_x * self.scene.tile_width_px, self.tile_y * self.scene.tile_height_px))

    def move(self, new_position: tuple[int, int]):
        self.labyrinth.attempt_move("cat", new_position)
        self.tile_x = max(0, min(new_position[0], self.scene.tile_width-1))
        self.tile_y = max(0, min(new_position[1], self.scene.tile_height-1))
