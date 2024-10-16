import pygame

import Labyrinth
import Scene


class Entity:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, symbol: str):
        self.image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(self.image, (scene.tile_width_px, scene.tile_height_px))
        self.tile_x = position[0]
        self.tile_y = position[1]
        self.scene = scene
        self.symbol = symbol
        self.maze_memory = []
        # **-****
        # *---***
        # *-*-***
        # ---****
        # *-*****                                                         ->[z]
        # *******                                                 |>[zzd] ->[ds]
        # mémoire -> un arbre, une branche par intersection, [dd] ->[d]
        # self.visibility = 5 / inf                               |>[s]

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.tile_x * self.scene.tile_width_px, self.tile_y * self.scene.tile_height_px))

    def move(self, new_position: tuple[int, int]):
        # if new_position == (self.tile_x, self.tile_y): return
        self.tile_x = max(0, min(new_position[0], self.scene.tile_width-1))
        self.tile_y = max(0, min(new_position[1], self.scene.tile_height-1))

    def see(self, maze: list[str]):
        # regarde les self.visibility tuiles devant lui et l'enregistre dans sa mémoire
        # pour chat -> inf   souris -> 5
        pass

    def action(self):
        # se déplace ou pas en fonction de la mémoire et de l'objectif
        pass

    def next(self):
        pass
