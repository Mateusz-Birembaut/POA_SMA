from Enums import EntityMove


class Branch:

	def __init__(self, parent: 'Branch' = None):
		self.__parent = parent
		self.__values: list[EntityMove] = []
		self.__previous_value = -1
		self.__children: list[Branch] = []
		self.__completed = False

	def get_parent(self) -> 'Branch':
		return self.__parent

	def is_completed(self) -> bool:
		return self.__completed

	def get_values(self) -> list[EntityMove]:
		return self.__values

	def get_last_value(self) -> EntityMove:
		if len(self.__values) == 0:
			return EntityMove.NONE
		return self.__values[-1]

	def get_previous_value(self) -> EntityMove:
		if self.__previous_value < 0:
			return EntityMove.NONE
		self.__previous_value -= 1
		return self.__values[self.__previous_value + 1]

	def add_value(self, value: EntityMove):
		self.__values.append(value)
		self.__previous_value += 1

	def get_children(self) -> list['Branch']:
		return self.__children

	def create_child(self, first_value: EntityMove):
		self.__children.append(Branch(self))
		self.__children[-1].add_value(first_value)

	def set_completed(self):
		self.__completed = True
