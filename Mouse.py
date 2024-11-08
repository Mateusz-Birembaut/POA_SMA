from Entity import Entity
from Branch import Branch
from Scene import Scene
import random
import Move

class Mouse(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene):
        Entity.__init__(self, img_url, position, scene)
        self.visibility = 5
        self.maze_memory = Branch(None)
        self.symbol = 'M'
        self.next_move_possible = []

    # aka update_memory
    def see(self, lab): # maze: list[str]):
        print('SEE')
        print('last : ', self.maze_memory.get_last_value())
        self.next_move_possible = []
        # regarde les self.visibility tuiles autour de lui (sauf d'où il vient)
        # et l'enregistre dans sa mémoire
        to_test = [[0, -1, 'z'], [0, 1, 's'], [1, 0, 'd'], [-1, 0, 'q']]
        for coord in to_test:
            print(coord)
            if Move.invert_move[self.maze_memory.get_last_value()] == coord[:-1]:
                print('d\'où on vient donc ignore')
                continue
            print('attempt :', (self.tile_y + coord[1], self.tile_x + coord[0]))
            if lab.tile_existe((self.tile_y + coord[1], self.tile_x + coord[0])):
                print('case existe')
                adjacent_tile = lab.maze[self.tile_y + coord[1]][self.tile_x + coord[0]]
                if adjacent_tile == ' ':
                    print('chemin possible, création branche')
                    self.maze_memory.create_children(1)
                    self.next_move_possible.append(coord[2])
                    # for i in range(self.visibility):
                    #     if lab.tile_existe((self.tile_y + (i+2)*coord[1], self.tile_x + (i+2)*coord[0])):
                    #         adjacent_tile = lab.maze[self.tile_y + (i+2)*coord[1]][self.tile_x + (i+2)*coord[0]]
                    #         if adjacent_tile == 'C':
                    #             # TODO activer mode fuite et aller à l'oposé
                    #             pass
                elif adjacent_tile == 'S':
                    print('c\'est la sortie !!!')
        if not self.next_move_possible:
            print('cul de sac -> revenir en arrière')
            prev = self.maze_memory.get_previous_value()
            if prev is None:
                print('on est de retour à l\'intersection, ont change de branche')
                self.maze_memory = self.maze_memory.get_parent()
                prev = self.maze_memory.get_previous_value()
            self.next_move_possible = [Move.invert_char[prev]]

    # aka move_or_idle
    def action(self, lab):
        # se déplace ou pas en fonction de la mémoire et de l'objectif
        # si mode = cherche -> chercher sortie -> faire en fonction de mémoire
        # si mode = fuite -> fuir chat -> ignoré mémoire
        print('ACTION')
        if self.next_move_possible:
            res = random.choice(self.next_move_possible)
            print(res)
            print('pos = ', self.tile_x, self.tile_y)
            print('new_pos = ', self.tile_x + Move.move[res][0], self.tile_y + Move.move[res][1])
            if self.move((self.tile_x + Move.move[res][0], self.tile_y + Move.move[res][1]), lab):
                self.maze_memory.add_value(res)
        else:
            print(self.next_move_possible)

    # ???
    def next(self):
        pass
