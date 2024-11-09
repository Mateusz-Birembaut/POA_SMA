from enum import Enum


class EntityState(Enum):
    SEARCH = 1
    CHASE = 2
    FLEE = 3
    REVERSE = 4
    OUT = 5
