import sys

import pygame
from pygame.locals import *

from Cat import Cat
from Labyrinth import Labyrinth
from Menu import Menu
from Mouse import Mouse1, Mouse2
from Scene import Scene

pygame.init()
gameClock = pygame.time.Clock()

tile_width, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

game_speed = 10

margin_right = 250

scene = Scene((tile_width, tile_height), (tile_width_px, tile_height_px), margin_right)

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

labyrinth = Labyrinth((tile_width, tile_height))

menu = Menu(screen.get_width(), screen.get_height(), margin_right, game_speed)

mouse = Mouse1('./res/mouse.png', labyrinth.get_random_empty_position(), scene,  str(labyrinth.m))

cat = Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))

# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            menu.handle_event(event)

    labyrinth.draw(screen, margin_right)
    menu.draw(screen)

    if menu.restarted:
        labyrinth = Labyrinth((tile_width, tile_height))
        cat = Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
        mouse = Mouse1('./res/mouse.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
        menu.restarted = False
        menu.paused = True
        menu.ended = False

    if not menu.ended and not menu.paused:
        cat.move((mouse.tile_x, mouse.tile_y))
        if (cat.tile_x, cat.tile_y) == (mouse.tile_x, mouse.tile_y):
            print("chat a gagné")
            menu.ended = True
            continue

        # mouse.see(labyrinth)
        # mouse.action(labyrinth)
        mouse.move()
        if (mouse.tile_x, mouse.tile_y) in labyrinth.exits:
            print("souris a gagné")
            menu.ended = True
            continue


    cat.draw(screen)
    mouse.draw(screen)

    pygame.display.flip()
    gameClock.tick(menu.game_speed)
