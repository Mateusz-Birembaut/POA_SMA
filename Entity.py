import random

import numpy
import pygame

import Scene


class Entity:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, m):
        self.image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(self.image, (scene.tile_width_px, scene.tile_height_px))
        self.tile_x = position[0]
        self.tile_y = position[1]
        self.scene = scene
        self.maze = []

        line = []
        for char in str(m):
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
                self.maze.append(line)
                line = []
        self.maze.append(line)

        self.maze[self.tile_x][self.tile_y] = 0
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
            tile_index = self.maze[y][x]
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

        if self.maze[self.tile_y][self.tile_x] >= 0:  # petite verif pour voir si c'est pas un mur
            self.maze[self.tile_y][self.tile_x] += 1  # on se déplace

        self.check_if_dead_end()  # regarder autour pour voir si il y a des culs-de-sac

    def check_if_dead_end(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            found_wall = False
            i = 1  # commence a 1 pour tester les cases adjacentes
            while not found_wall:
                x = self.tile_x + coord[0] * i
                y = self.tile_y + coord[1] * i

                # si que (x, y) est dans les limites
                if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
                    tile_index = self.maze[y][x]

                    if tile_index == -1:  # si un mur est trouvé
                        found_wall = True
                        is_dead_end = True
                        index = 1
                        while index < i:
                            x = self.tile_x + coord[0] * index
                            y = self.tile_y + coord[1] * index

                            if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):

                                # Verifie les cases adjactentes pour verifier si c'est un couloir

                                if coord[0] != 0:
                                    # check les cases en fonction de si on est dans un mvt horizontale ou vertical
                                    if (y + 1 < len(self.maze) and self.maze[y + 1][x] != -1) or \
                                            (y - 1 >= 0 and self.maze[y - 1][x] != -1):
                                        is_dead_end = False
                                        break
                                else:
                                    if (x + 1 < len(self.maze[0]) and self.maze[y][x + 1] != -1) or \
                                            (x - 1 >= 0 and self.maze[y][x - 1] != -1):
                                        is_dead_end = False
                                        break

                            index += 1

                        # si ce couloir est un cul de sac, j'incrémente les valeurs de ce chemin de +10 pour pas y aller
                        if is_dead_end:
                            index = 1
                            while index < i:
                                x = self.tile_x + coord[0] * index
                                y = self.tile_y + coord[1] * index
                                self.maze[y][x] += 10
                                index += 1
                else:
                    break  # si on est hors limite on dit que non

                i += 1

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
