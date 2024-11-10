class Vec2():

    def __init__(self, x: int, y: int):
        self.__values = x, y

    def __getitem__(self, index: int) -> int:
        return self.__values[index]

    def __mul__(self, other: int) -> tuple[int, int]:
        return self.__values[0] * other, self.__values[1] * other

    def __eq__(self, other):
        return self.__values[0] == other[0] and self.__values[1] == other[1]
