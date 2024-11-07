import random
import sys

import pygame
from pygame.locals import *

from Entity import Entity
from Cat import Cat
from Labyrinth import Labyrinth
from Scene import Scene
from Menu import Menu
import copy

pygame.init()
gameClock = pygame.time.Clock()

tile_width, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

margin_right = 250

scene = Scene((tile_width, tile_height), (tile_width_px, tile_height_px), margin_right)

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

labyrinth = Labyrinth((tile_width, tile_height))

menu = Menu(screen.get_width(), screen.get_height(), margin_right)

mouse = Entity('./res/mouse.png', labyrinth.get_random_empty_position(), scene,  copy.deepcopy(labyrinth.maze))

cat = Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, copy.deepcopy(labyrinth.maze))


# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print("Event: ", event)
            menu.handle_event(event)

    labyrinth.draw(screen, margin_right)
    menu.draw(screen)

    if menu.restarted:
        cat = Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, copy.deepcopy(labyrinth.maze))
        mouse = Entity('./res/mouse.png', labyrinth.get_random_empty_position(), scene,  copy.deepcopy(labyrinth.maze))
        menu.restarted = False

    if not menu.paused:
        cat.move((mouse.tile_x , mouse.tile_y))

    cat.draw(screen)
    mouse.draw(screen)

    pygame.display.flip()
    gameClock.tick(60)
