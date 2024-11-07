import pygame

from Labyrinth import Labyrinth
import Scene


class Entity:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, maze):
        self.image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(self.image, (scene.tile_width_px, scene.tile_height_px))
        self.tile_x = position[0]
        self.tile_y = position[1]
        self.scene = scene
        self.maze = maze
        self.maze[self.tile_x][self.tile_y] = 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.tile_x * self.scene.tile_width_px, self.tile_y * self.scene.tile_height_px))


