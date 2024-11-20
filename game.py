import sys

import pygame
from pygame.locals import QUIT

from Cat import Cat
from Labyrinth import Labyrinth
from Menu import Menu
from Mouse import Mouse, Mouse2
from Scene import Scene

pygame.init()
gameClock = pygame.time.Clock()

tile_width_nb, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

game_speed = 200 #en ms

margin_right = 250

scene = Scene((tile_width_nb, tile_height), (tile_width_px, tile_height_px), margin_right)

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

menu = Menu(screen.get_width(), screen.get_height(), margin_right, game_speed)

labyrinth = Labyrinth((tile_width_nb, tile_height))
mouse = Mouse2('./res/mouse.png', labyrinth.get_entrance(), scene, str(labyrinth.m))
cat = Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))

last_action_time = 0
current_turn = "cat"

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type in {pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION}:
            menu.handle_event(event)

    if menu.restarted:
        labyrinth = Labyrinth((tile_width_nb, tile_height))
        scene.set_labyrinth(labyrinth)
        if menu.algo_m:
            mouse = Mouse('./res/mouse.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
        else:
            mouse = Mouse2('./res/mouse.png', labyrinth.get_entrance(), scene, str(labyrinth.m))
        cat = Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
        menu.restarted = False
        menu.paused = True
        menu.ended = False
        last_action_time = pygame.time.get_ticks()
        current_turn = "cat"

    labyrinth.draw(screen, margin_right)
    menu.draw(screen)

    current_time = pygame.time.get_ticks()  # Temps actuel en millisecondes

    if not menu.ended and not menu.paused:
        # Gérer l'action alternée entre chat et souris
        if current_time - last_action_time >= menu.speed_slider.value:
            if current_turn == "cat":
                cat.process((mouse.tile_x, mouse.tile_y))
                if (cat.tile_x, cat.tile_y) == (mouse.tile_x, mouse.tile_y):
                    print("chat a gagné")
                    menu.ended = True
                    continue
                current_turn = "mouse"  # Passe à la souris pour le prochain tour
            else:
                mouse.process()
                if (mouse.tile_x, mouse.tile_y) in labyrinth.exits:
                    print("souris a gagné")
                    menu.ended = True
                    continue
                current_turn = "cat"  # Passe au chat pour le prochain tour

            last_action_time = current_time  # Réinitialise le temporisateur

    cat.draw(screen)
    mouse.draw(screen)

    pygame.display.flip()
    gameClock.tick(120)
