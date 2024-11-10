import numpy

import Scene
from Entity import Entity


class Mouse(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, maze):
        Entity.__init__(self, img_url, position, scene, maze)
        self.exitLocation = None
        self.sawExit = False

    def sees_exit(self):
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
    
    def move(self):
        if self.sawExit:
            self.move_to_exit()
        else:
            super().move()
            self.sees_exit()

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
