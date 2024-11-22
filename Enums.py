from enum import Enum

from Vec2 import Vec2


class EntityState(Enum):
    SEARCH = 1
    CHASE = 2
    REVERSE = 3
    WIN = 4


class EntityMove(Enum):
    UP = Vec2(0, -1)
    DOWN = Vec2(0, 1)
    LEFT = Vec2(-1, 0)
    RIGHT = Vec2(1, 0)
    NONE = Vec2(0, 0)
