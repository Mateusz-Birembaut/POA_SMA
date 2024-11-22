import random

import numpy
import pygame

import Scene
from Enums import EntityState


class Agent:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, m: str):
        image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(image, (scene.tile_width_px, scene.tile_height_px))
        self.tile_x = position[0]
        self.tile_y = position[1]
        self.scene = scene
        self.symbol = ''
        self.state = EntityState.SEARCH
        self.memory = []

        line = []
        for char in m:
            if char != '\n':
                integer = 0
                if char == '#':
                    integer = -1
                elif char == 'E':
                    integer = -2
                elif char == 'S':
                    integer = -3
                line.append(integer)
            else:
                self.memory.append(line)
                line = []
        self.memory.append(line)

        self.memory[self.tile_x][self.tile_y] = 0
        self.old_position = None

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.tile_x * self.scene.tile_width_px, self.tile_y * self.scene.tile_height_px))

    def move(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        smallest_index = 1000
        movements_possibles = []
        for coord in to_test:
            x = self.tile_x + coord[0]
            y = self.tile_y + coord[1]
            tile_index = self.memory[y][x]
            if 0 <= tile_index <= smallest_index:
                if tile_index == smallest_index:
                    movements_possibles.append(coord)
                else:
                    smallest_index = tile_index
                    movements_possibles = [coord]

        # recup l'index de la difference entre la position actuelle et precedente
        index_old_position = self.index_of_old_position(movements_possibles)

        if len(movements_possibles) > 1:  # si on a plusieurs mouvement possible
            if index_old_position is not None:  # si la différence est présent dans les mouvements possible
                movements_possibles.pop(index_old_position)  # la supprimer

        index = random.randint(0, len(movements_possibles) - 1)  # prendre un index random
        movement = movements_possibles[index]  # aller dans la direction choisit aléatoirement

        self.old_position = [self.tile_x, self.tile_y]  # ancienne position = position actuelle

        self.tile_x += movement[0]
        self.tile_y += movement[1]

        if self.memory[self.tile_y][self.tile_x] >= 0:  # petite verif pour voir si c'est pas un mur
            self.memory[self.tile_y][self.tile_x] += 1  # on se déplace

        self.check_if_dead_end()  # regarder autour pour voir si il y a des culs-de-sac

    # retourne l'indice de la différence entre position ancienne et actuelle
    # si pas trouvé on retourne None
    def index_of_old_position(self, movement_possible):
        index = 0
        if self.old_position is not None:
            # direction vers laquelle la souris a été vu en dernier
            direction = tuple(numpy.subtract(self.old_position, (self.tile_x, self.tile_y)))
            direction = list(direction)
            for coord in movement_possible:
                if direction == coord:
                    return index
                index = index + 1

        return None  # pas trouvé

    def check_if_dead_end(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            found_wall = False
            i = 1  # commence a 1 pour tester les cases adjacentes
            while not found_wall:
                x = self.tile_x + coord[0] * i
                y = self.tile_y + coord[1] * i

                # si que (x, y) est dans les limites
                if 0 <= x < len(self.memory[0]) and 0 <= y < len(self.memory):
                    tile_index = self.memory[y][x]

                    if tile_index == -1:  # si un mur est trouvé
                        found_wall = True
                        is_dead_end = True
                        index = 1
                        while index < i:
                            x = self.tile_x + coord[0] * index
                            y = self.tile_y + coord[1] * index

                            if 0 <= x < len(self.memory[0]) and 0 <= y < len(self.memory):

                                # Verifie les cases adjactentes pour verifier si c'est un couloir

                                if coord[0] != 0:
                                    # check les cases en fonction de si on est dans un mvt horizontale ou vertical
                                    if (y + 1 < len(self.memory) and self.memory[y + 1][x] != -1) or \
                                            (y - 1 >= 0 and self.memory[y - 1][x] != -1):
                                        is_dead_end = False
                                        break
                                else:
                                    if (x + 1 < len(self.memory[0]) and self.memory[y][x + 1] != -1) or \
                                            (x - 1 >= 0 and self.memory[y][x - 1] != -1):
                                        is_dead_end = False
                                        break

                            index += 1

                        # si ce couloir est un cul de sac, j'incrémente les valeurs de ce chemin de +10 pour pas y aller
                        if is_dead_end:
                            index = 1
                            while index < i:
                                x = self.tile_x + coord[0] * index
                                y = self.tile_y + coord[1] * index
                                self.memory[y][x] += 10
                                index += 1
                else:
                    break  # si on est hors limite on dit que non

                i += 1

    def see(self):
        # regarde les self.visibility tuiles devant lui et l'enregistre dans sa mémoire
        # pour chat -> inf   souris -> 5
        pass

    def action(self):
        # se déplace ou pas en fonction de la mémoire et de l'objectif
        pass

    def move2(self, new_position: tuple[int, int]) -> bool:
        # todo donner seulement X ou Y en entrée et calculer new_pos
        if new_position == (self.tile_x, self.tile_y): return False
        if self.scene.lab.attempt_move(new_position):
            self.tile_x = max(0, min(new_position[0], self.scene.tile_width_nb - 1))
            self.tile_y = max(0, min(new_position[1], self.scene.tile_height_nb - 1))
            return True
        return False
