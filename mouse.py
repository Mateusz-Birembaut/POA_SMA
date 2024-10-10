import pygame

import Scene


class Mouse:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene):
        self.image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(self.image, (scene.tile_width_px, scene.tile_height_px))
        self.scene = scene
        self.tile_x = position[0]
        self.tile_y = position[1]

    def draw(self, screen, tile_width_px, tile_height_px):
        screen.blit(self.image, (self.tile_x * tile_width_px, self.tile_y * tile_height_px))

    def move(self, new_position):
        self.tile_x = max(0, min(new_position[0], self.scene.tile_width-1))
        self.tile_y = max(0, min(new_position[1], self.scene.tile_height-1))
