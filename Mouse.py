from Entity import Entity
from Branch import Branch
from Scene import Scene

class Mouse(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, symbol: str):
        Entity.__init__(self, img_url, position, scene, symbol)
        self.visibility = 5
        self.maze_memory = Branch(None)

    # aka update_memory
    def see(self, maze: list[str]):
        # regarde les self.visibility tuiles autour de lui (sauf d'où il vient)
        # et l'enregistre dans sa mémoire
        to_test = [[1, 0, 'd'], [0, 1, 's'], [-1, 0, 'q'], [0, -1, 'z']]
        for coord in to_test:
            if self.maze_memory.get_last_value() == coord[2]: continue
            adjacent_tile = maze[self.tile_y + coord[1]][self.tile_x + coord[0]]
            if adjacent_tile != '#':
                while True:
                    pass
            elif adjacent_tile == 'E':
                print('sortie trouvée !!!')

    # aka move_or_idle
    def action(self):
        # se déplace ou pas en fonction de la mémoire et de l'objectif
        pass

    # ???
    def next(self):
        pass
