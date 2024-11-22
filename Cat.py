import random

import numpy

import Scene
from Agent import Agent
from Enums import EntityState


class Cat(Agent):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, m):
        Agent.__init__(self, img_url, position, scene)
        self.state = EntityState.SEARCH
        self.lastSeenMousePosition = (-5, -5)
        self.runningSpeed = 2
        self.old_position = None
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
        self.memory[self._Agent__tile_x][self._Agent__tile_y] = 0

    def process(self):
        self.check_mouse()  # regarde si il voit la souris autour
        if self.state == EntityState.CHASE:  # si on a vu la souris
            self.move_towards_last_seen_position()  # se déplacer vers la position vue
        else:
            self.move()
        if self.state != EntityState.WIN:
            self.check_mouse()

    def check_mouse(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            x = self._Agent__tile_x + coord[0]
            y = self._Agent__tile_y + coord[1]
            while self.memory[y][x] >= 0:
                if self.scene.env.get_tile((x, y)) == 'M':
                    self.lastSeenMousePosition = (x, y)
                    self.state = EntityState.CHASE
                    return
                x = x + coord[0]
                y = y + coord[1]
        if self.lastSeenMousePosition != (-5, -5):
            self.state = EntityState.CHASE
            return

        self.state = EntityState.SEARCH

    def move_towards_last_seen_position(self):
        x = self._Agent__tile_x
        y = self._Agent__tile_y
        # direction vers laquelle la souris a été vu en dernier
        direction = tuple(numpy.subtract(self.lastSeenMousePosition, (x, y)))
        for i in range(self.runningSpeed):  # vitesseRunning = nb de cases max par tours
            if abs(direction[0]) > abs(direction[1]):
                x += numpy.sign(direction[0])  # ajoute 1 ou -1 selon la direction
            else:
                y += numpy.sign(direction[1])  # ajoute 1 ou -1 selon la direction

            self.memory[y][x] += 1  # dans le maze du chat on est passé par la

            if self.lastSeenMousePosition == (x, y):  # si on est arrivé à la dernière position connu on stop
                self.lastSeenMousePosition = (-5,-5)
                break

        self._Agent__tile_x = x
        self._Agent__tile_y = y
        if self.scene.env.get_tile((self._Agent__tile_x, self._Agent__tile_y)) == 'M':
            self.state = EntityState.WIN
        self.scene.env.change_agent_pos((self._Agent__tile_x, self._Agent__tile_y), 'C')

    def move(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        smallest_index = 1000
        movements_possibles = []
        for coord in to_test:
            x = self._Agent__tile_x + coord[0]
            y = self._Agent__tile_y + coord[1]
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

        self.old_position = [self._Agent__tile_x, self._Agent__tile_y]  # ancienne position = position actuelle

        self._Agent__tile_x += movement[0]
        self._Agent__tile_y += movement[1]
        if self.scene.env.get_tile((self._Agent__tile_x, self._Agent__tile_y)) == 'M':
            self.state = EntityState.WIN
            return
        self.scene.env.change_agent_pos((self._Agent__tile_x, self._Agent__tile_y), 'C')

        if self.memory[self._Agent__tile_y][self._Agent__tile_x] >= 0:  # petite verif pour voir si c'est pas un mur
            self.memory[self._Agent__tile_y][self._Agent__tile_x] += 1  # on se déplace

        self.check_if_dead_end()  # regarder autour pour voir si il y a des culs-de-sac

    # retourne l'indice de la différence entre position ancienne et actuelle
    # si pas trouvé on retourne None
    def index_of_old_position(self, movement_possible):
        index = 0
        if self.old_position is not None:
            # direction vers laquelle la souris a été vu en dernier
            direction = tuple(numpy.subtract(self.old_position, (self._Agent__tile_x, self._Agent__tile_y)))
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
                x = self._Agent__tile_x + coord[0] * i
                y = self._Agent__tile_y + coord[1] * i

                # si que (x, y) est dans les limites
                if 0 <= x < len(self.memory[0]) and 0 <= y < len(self.memory):
                    tile_index = self.memory[y][x]

                    if tile_index == -1:  # si un mur est trouvé
                        found_wall = True
                        is_dead_end = True
                        index = 1
                        while index < i:
                            x = self._Agent__tile_x + coord[0] * index
                            y = self._Agent__tile_y + coord[1] * index

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
                                x = self._Agent__tile_x + coord[0] * index
                                y = self._Agent__tile_y + coord[1] * index
                                self.memory[y][x] += 10
                                index += 1
                else:
                    break  # si on est hors limite on dit que non

                i += 1
