import sys

import pygame
from pygame.locals import *

from Entity import Entity
from Labyrinth import Labyrinth
from Mouse import Mouse
from Scene import Scene

pygame.init()
gameClock = pygame.time.Clock()

tile_width, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

scene = Scene((tile_width, tile_height), (tile_width_px, tile_height_px))

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

labyrinth = Labyrinth((tile_width, tile_height))

mouse = Mouse('./res/mouse.png', labyrinth.get_entrance(), scene)

cat = Entity('./res/cat.png', (19, 1), scene)


# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update

    # new_mouse_x, new_mouse_y = mouse.tile_x, mouse.tile_y
    #
    # can_move_x, can_move_y = False, False
    # if labyrinth.attempt_move((new_mouse_x+1, mouse.tile_y)):
    #     can_move_x = True
    # if labyrinth.attempt_move((mouse.tile_x, new_mouse_y+1)):
    #     can_move_y = True
    #
    # if can_move_x and can_move_y:
    #     if random.random() > .5:
    #         new_mouse_x += 1
    #     else:
    #         new_mouse_y += 1
    # elif (not can_move_x) and (not can_move_y):
    #     new_mouse_x = 1
    #     new_mouse_y = 1
    # else:
    #     new_mouse_x += can_move_x * 1
    #     new_mouse_y += can_move_y * 1

    # Draw
    labyrinth.draw(screen)
    mouse.see(labyrinth)
    mouse.action(labyrinth)
    # mouse.move((new_mouse_x, new_mouse_y))
    mouse.draw(screen)
    # cat.move((cat_x, cat_y))
    cat.draw(screen)

    pygame.display.flip()
    gameClock.tick(100)
    # input('>')
