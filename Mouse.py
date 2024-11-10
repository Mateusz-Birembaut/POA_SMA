import random

import numpy

from Branch import Branch
from Entity import Entity
from Enums import EntityState, EntityMove
from Scene import Scene


class Mouse(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, m: str):
        Entity.__init__(self, img_url, position, scene, m)
        self.exitLocation = None
        self.sawExit = False

    def process(self):
        if self.sawExit:
            self.move_to_exit()
        else:
            super().move()
            self.check_exit()

    def move_to_exit(self):
        x = self.tile_x
        y = self.tile_y
        # direction vers laquelle la souris a été vu en dernier
        direction = tuple(numpy.subtract(self.exitLocation, (x, y)))

        if abs(direction[0]) > abs(direction[1]):
            x += numpy.sign(direction[0])  # ajoute 1 ou -1 selon la direction
        else:
            y += numpy.sign(direction[1])  # ajoute 1 ou -1 selon la direction

        self.maze[y][x] += 1  # dans le maze de la souris on est passé par la

        # if self.exitLocation == (x, y): # si la souris est dans sur la sortie
        # ici mettre fin au jeu ?

        self.tile_x = x
        self.tile_y = y

    def check_exit(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            x = self.tile_x + coord[0]
            y = self.tile_y + coord[1]
            while self.maze[y][x] >= 0:
                x = x + coord[0]
                y = y + coord[1]

            if self.maze[y][x] == -3 or self.maze[y][x] == -2:
                self.sawExit = True
                self.exitLocation = (x, y)


class Mouse2(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, m: str):
        Entity.__init__(self, img_url, position, scene, m)
        self.visibility = 5
        self.maze_memory: Branch = Branch()
        self.symbol = 'M'
        self.next_move_possible: list[EntityMove] = []

    def process(self):
        self.see()
        self.action()

    def see(self):
        self.next_move_possible = []

        if self.state != EntityState.SEARCH: return

        for direction in [EntityMove.UP, EntityMove.DOWN, EntityMove.LEFT, EntityMove.RIGHT]:
            # on ignore là d'où on vient
            if self.maze_memory.get_last_value().value * -1 == direction.value:
                continue

            adjacent_tile = self.scene.lab.get_tile((self.tile_x + direction.value[0], self.tile_y + direction.value[1]))
            if adjacent_tile != '':
                if adjacent_tile == ' ':  # espace = chemin
                    self.next_move_possible.append(direction)
                    # todo regarde les self.visibility tuiles devant et l'enregistrer dans sa mémoire
                    # for i in range(self.visibility):
                    #     next_tile = lab.get_tile((self.tile_x + (i+2)*direction.value[0], self.tile_y + (i+2)*direction.value[1]))
                    #     if next_tile == 'C':  # C = le chat
                    #         self.state = EntityState.FLEE
                    #         break
                elif adjacent_tile == 'S':
                    self.next_move_possible = [direction]
                    break

        # plusieurs choix = intersection
        if len(self.next_move_possible) > 1:
            # on créer les branches seulement si elles ne sont pas déjà créées
            if not self.maze_memory.get_children():
                for move in self.next_move_possible:
                    self.maze_memory.create_child(move)

    def action(self):
        if self.state == EntityState.OUT: return

        # todo se déplace ou pas en fonction de la mémoire et de l'objectif
        # si mode = cherche -> chercher sortie -> faire en fonction de mémoire
        # si mode = fuite -> fuir chat -> ignoré mémoire
        # si mode = retour -> faire demi-tour -> remonter la branche jusqu'à la dernière intersection

        # un seul choix -> y aller
        if len(self.next_move_possible) == 1:
            move = self.next_move_possible[0]
            if self.move2((self.tile_x + move.value[0], self.tile_y + move.value[1])):
                self.maze_memory.add_value(move)
            if self.scene.lab.get_tile((self.tile_x, self.tile_y)) == 'S':
                self.state = EntityState.OUT

        # plusieurs choix -> choisir un chemin
        elif len(self.next_move_possible) > 1:
            branch = random.choice(self.maze_memory.get_children())
            move = branch.get_last_value().value
            self.move2((self.tile_x + move[0], self.tile_y + move[1]))
            self.maze_memory = branch

        # cul de sac -> faire demi-tour
        else:
            self.state = EntityState.REVERSE
            prev_move = self.maze_memory.pop()

            # si de retour à l'intersection -> change de branche
            if prev_move == EntityMove.NONE:
                self.maze_memory.set_completed()
                self.maze_memory = self.maze_memory.get_parent()
                # prend une autre inter s'il y en a une de non finie
                for branch in self.maze_memory.get_children():
                    if not branch.is_completed():
                        self.maze_memory = branch
                        prev_move = self.maze_memory.get_last_value()
                        self.move2((self.tile_x + prev_move.value[0], self.tile_y + prev_move.value[1]))
                        self.state = EntityState.SEARCH
                        return
                # sinon, encore revenir en arrière
                prev_move = self.maze_memory.pop()

            # si pas arrivé à la dernière intersection
            if prev_move != EntityMove.NONE:
                self.move2((self.tile_x + prev_move.value[0] * -1, self.tile_y + prev_move.value[1] * -1))
