import sys

import pygame
from pygame.locals import QUIT

from Cat import Cat
from Environnement import Environnement
from Menu import Menu
from Mouse import Mouse
from Scene import Scene
from Enums import EntityState

pygame.init()
pygame.display.set_caption("Cat & Mouse")
gameClock = pygame.time.Clock()

tile_width_nb, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

game_speed = 200 #en ms

margin_right = 250

scene = Scene((tile_width_nb, tile_height), (tile_width_px, tile_height_px), margin_right)

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

menu = Menu(screen.get_width(), screen.get_height(), margin_right, game_speed)

environnement = Environnement((tile_width_nb, tile_height))
mouse = Mouse('./res/mouse.png', environnement.get_position_of('E'), scene)
cat = Cat('./res/cat.png', environnement.get_random_empty_position(), scene, str(environnement.m))

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
        environnement = Environnement((tile_width_nb, tile_height))
        scene.set_environnement(environnement)
        mouse = Mouse('./res/mouse.png', environnement.get_position_of('E'), scene)
        cat = Cat('./res/cat.png', environnement.get_random_empty_position(), scene, str(environnement.m))
        menu.restarted = False
        menu.paused = True
        menu.ended = False
        last_action_time = pygame.time.get_ticks()
        current_turn = "cat"

    environnement.draw(screen, margin_right)
    menu.draw(screen)

    current_time = pygame.time.get_ticks()  # Temps actuel en millisecondes

    if not menu.ended and not menu.paused:
        # Gérer l'action alternée entre chat et souris
        if current_time - last_action_time >= menu.speed_slider.value:
            if current_turn == "cat":
                cat.process()
                if cat.state == EntityState.WIN:
                    print("chat a gagné")
                    menu.ended = True
                    continue
                current_turn = "mouse"  # Passe à la souris pour le prochain tour
            else:
                mouse.process()
                if mouse.state == EntityState.WIN:
                    print("souris a gagné")
                    menu.ended = True
                    continue
                current_turn = "cat"  # Passe au chat pour le prochain tour

            last_action_time = current_time  # Réinitialise le temporisateur

    cat.draw(screen)
    mouse.draw(screen)

    pygame.display.flip()
    gameClock.tick(120)
