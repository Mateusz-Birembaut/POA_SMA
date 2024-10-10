from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.solve.BacktrackingSolver import BacktrackingSolver

m = Maze()
m.generator = Prims(10, 10)
m.generate()

m.solver = BacktrackingSolver()
m.generate_entrances()
# m.solve()
print(m)