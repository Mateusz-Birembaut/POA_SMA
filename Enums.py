from enum import Enum

from Vec2 import Vec2


class EntityState(Enum):
    SEARCH = 1
    CHASE = 2
    FLEE = 3
    REVERSE = 4
    OUT = 5


class EntityMove(Enum):
    UP = Vec2(0, -1)
    DOWN = Vec2(0, 1)
    LEFT = Vec2(-1, 0)
    RIGHT = Vec2(1, 0)
