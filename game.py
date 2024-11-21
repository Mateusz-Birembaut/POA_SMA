import sys

import pygame
from pygame.locals import QUIT

from Cat import Cat
from Labyrinth import Labyrinth
from Menu import Menu
from Mouse import Mouse2, Mouse
from Scene import Scene

pygame.init()
gameClock = pygame.time.Clock()

tile_width_nb, tile_height = 30, 30
tile_width_px, tile_height_px = 10, 10

game_speed = 200  # en ms
number_of_mouse = 40
num_cats = 4
margin_right = 250

scene = Scene((tile_width_nb, tile_height), (tile_width_px, tile_height_px), margin_right)

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

menu = Menu(screen.get_width(), screen.get_height(), margin_right, game_speed)

labyrinth = Labyrinth((tile_width_nb, tile_height))


cats = [
    Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
    for _ in range(num_cats)
]
mouses = [
    Mouse2('./res/mouse.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
    for _ in range(number_of_mouse)
]


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
            mouses = [
                Mouse('./res/mouse.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
                for _ in range(number_of_mouse)
            ]
        else:
            mouses = [
                Mouse2('./res/mouse.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
                for _ in range(number_of_mouse)
            ]
        cats = [
            Cat('./res/cat.png', labyrinth.get_random_empty_position(), scene, str(labyrinth.m))
            for _ in range(num_cats)
        ]

        menu.restarted = False
        menu.paused = True
        menu.ended = False
        last_action_time = pygame.time.get_ticks()
        current_turn = "cat"

    labyrinth.draw(screen, margin_right)
    menu.draw(screen)

    current_time = pygame.time.get_ticks()

    if not menu.ended and not menu.paused:

        if current_time - last_action_time >= menu.speed_slider.value:
            if current_turn == "cat":
                for cat in cats:
                    if not mouses:
                        print("Les chats ont gagné")
                        menu.ended = True
                        continue
                    closest_mouse = min(
                        mouses,
                        key=lambda m: abs(cat.tile_x - m.tile_x) + abs(cat.tile_y - m.tile_y)
                    )
                    cat.process((closest_mouse.tile_x, closest_mouse.tile_y))

                    for mouse in mouses[:]:
                        if (cat.tile_x, cat.tile_y) == (mouse.tile_x, mouse.tile_y):
                            mouses.remove(mouse)
                            print("Un chat a attrapé une souris")
                            break

                if not mouses:
                    print("Les chats ont gagné")
                    menu.ended = True
                    continue

                current_turn = "mouse"
            else:
                for mouse in mouses[:]:
                    mouse.process()
                    if (mouse.tile_x, mouse.tile_y) in labyrinth.exits:
                        print("souris ont gagné")
                        menu.ended = True
                        break

                if menu.ended:
                    continue
                current_turn = "cat"
                last_mouse_time = current_time

            last_action_time = current_time

    # Dessiner les entités
    for cat in cats:
        cat.draw(screen)
    for mouse in mouses:
        mouse.draw(screen)

    pygame.display.flip()
    gameClock.tick(120)
