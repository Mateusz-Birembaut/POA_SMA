import random
import sys

import pygame
from pygame.locals import *

from Scene import Scene
from labyrinth import Maze
from mouse import Mouse

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

tile_width, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

scene = Scene((tile_width, tile_height), (tile_width_px, tile_height_px))

labyrinthe = Maze(tile_width, tile_height)

width, height = (tile_width * 2 + 1) * tile_width_px, (tile_height * 2 + 1) * tile_height_px
screen = pygame.display.set_mode((width, height))

mouse_x, mouse_y = 0, 0
mouse = Mouse('./res/mouse.png', (mouse_x, mouse_y), scene)


# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update
    print(pygame.time.get_ticks())
    pygame.time.wait(100)
    mouse_x += int(random.random()*2)
    mouse_y += int(random.random()*2)
    print(mouse_x, mouse_y)
    # Draw
    labyrinthe.draw(screen)
    mouse.move((mouse_x, mouse_y))
    mouse.draw(screen, tile_width_px, tile_height_px)

    pygame.display.flip()
    fpsClock.tick(fps)
