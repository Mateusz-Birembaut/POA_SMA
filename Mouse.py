import random

import Labyrinth
import Move
from Branch import Branch
from Entity import Entity
from EntityState import EntityState
from Scene import Scene


class Mouse(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene):
        Entity.__init__(self, img_url, position, scene)
        self.visibility = 5
        self.maze_memory = Branch()
        self.symbol = 'M'
        self.next_move_possible = []

    # aka update_memory
    def see(self, lab: Labyrinth):  # maze: list[str]):
        self.next_move_possible = []
        if self.state != EntityState.SEARCH: return
        print('-----SEE-----')
        # regarde les self.visibility tuiles autour de lui (sauf d'où il vient)
        # et l'enregistre dans sa mémoire
        to_test = [[0, -1, 'z'], [0, 1, 's'], [1, 0, 'd'], [-1, 0, 'q']]
        for coord in to_test:
            # print(coord)
            if Move.invert_move[self.maze_memory.get_last_value()] == coord[:-1]:
                print(coord[2], '- d\'où on vient donc ignore')
                continue
            # print('attempt :', (self.tile_y + coord[1], self.tile_x + coord[0]))
            # if lab.tile_exists((self.tile_y + coord[1], self.tile_x + coord[0])):
            adjacent_tile = lab.get_tile([self.tile_x + coord[0], self.tile_y + coord[1]])
            if adjacent_tile != '':
                # print('case existe')
                if adjacent_tile == ' ':
                    self.next_move_possible.append(coord[2])
                    # for i in range(self.visibility):
                    #     if lab.tile_existe((self.tile_y + (i+2)*coord[1], self.tile_x + (i+2)*coord[0])):
                    #         adjacent_tile = lab.maze[self.tile_y + (i+2)*coord[1]][self.tile_x + (i+2)*coord[0]]
                    #         if adjacent_tile == 'C':
                    #             # TODO activer mode fuite et aller à l'oposé
                    #             pass
                elif adjacent_tile == 'S':
                    print('c\'est la sortie !!!!!!!!!!!!!!!!!!!!!!!')
                    self.next_move_possible = [coord[2]]
                    break
        if len(self.next_move_possible) > 1:
            # on créer les branches seulement si elles ne sont pas déjà créées
            if not self.maze_memory.get_children():
                print(len(self.next_move_possible), 'chemins possibles, création branches')
                for i in self.next_move_possible:
                    self.maze_memory.create_child(i)
        print(self.next_move_possible)

    # aka move_or_idle
    def action(self, lab: Labyrinth):
        if self.state == EntityState.OUT: return
        # todo se déplace ou pas en fonction de la mémoire et de l'objectif
        # si mode = cherche -> chercher sortie -> faire en fonction de mémoire
        # si mode = fuite -> fuir chat -> ignoré mémoire
        print('ACTION')
        if len(self.next_move_possible) == 1:
            res = self.next_move_possible[0]
            print(res)
            if self.move((self.tile_x + Move.move[res][0], self.tile_y + Move.move[res][1]), lab):
                self.maze_memory.add_value(res)
            if lab.get_tile((self.tile_x, self.tile_y)) == 'S':
                self.state = EntityState.OUT
        elif len(self.next_move_possible) > 1:
            print('---CHANGEMENT BRANCH---')
            res = random.choice(self.maze_memory.get_children())
            print(res.get_last_value())
            self.maze_memory = res
            self.move((self.tile_x + Move.move[res.get_last_value()][0], self.tile_y + Move.move[res.get_last_value()][1]), lab)
        else:
            print('cul de sac -> revenir en arrière || STATE != SEARCH')
            print('---CHANGEMENT STATE---', self.state, EntityState.REVERSE)
            self.state = EntityState.REVERSE
            print('historique', self.maze_memory.get_values())
            prev = self.maze_memory.get_previous_value()
            if prev == '':
                print('on est de retour à l\'intersection, ont change de branche')
                self.maze_memory.set_completed()
                self.maze_memory = self.maze_memory.get_parent()
                # prend une autre inter s'il y en a une de non finie
                for branch in self.maze_memory.get_children():
                    if not branch.is_completed():
                        print('---CHANGEMENT BRANCH---')
                        self.maze_memory = branch
                        prev = self.maze_memory.get_last_value()
                        print(prev)
                        self.move((self.tile_x + Move.move[prev][0], self.tile_y + Move.move[prev][1]), lab)
                        print('---CHANGEMENT STATE---', self.state, EntityState.SEARCH)
                        self.state = EntityState.SEARCH
                        break
                # revenir en arrière
                if self.state == EntityState.REVERSE:
                    print('toutes les branches sont visitées, ont revient en arrière')
                    prev = self.maze_memory.get_previous_value()
                    print(Move.invert_char[prev])
                    self.move((self.tile_x + Move.invert_move[prev][0], self.tile_y + Move.invert_move[prev][1]), lab)
            else:
                print(Move.invert_char[prev])
                self.move((self.tile_x + Move.invert_move[prev][0], self.tile_y + Move.invert_move[prev][1]), lab)

    # ???
    def next(self):
        pass
