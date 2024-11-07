import random
import sys

import pygame
from pygame.locals import *

from Entity import Entity
from Cat import Cat
from Labyrinth import Labyrinth
from Scene import Scene
import copy

pygame.init()
gameClock = pygame.time.Clock()

tile_width, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

scene = Scene((tile_width, tile_height), (tile_width_px, tile_height_px))

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

labyrinth = Labyrinth((tile_width, tile_height))

#mouse = Entity('./res/mouse.png', (1, 1), scene, labyrinth, 'mouse')

cat = Cat('./res/cat.png', (10, 5), scene, copy.deepcopy(labyrinth.maze))


# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update
    #pygame.time.wait(25)

    # Draw
    labyrinth.draw(screen)
    cat.move((10,8))
    cat.draw(screen)

    pygame.display.flip()
    gameClock.tick(1)
