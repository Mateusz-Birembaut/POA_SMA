class Branch:

	def __init__(self, parent: 'Branch' = None):
		self.__parent = parent
		self.__values = ''
		self.__previous_value = -1
		self.__children: list[Branch] = []
		self.__completed = False

	def is_completed(self):
		return self.__completed

	def set_completed(self):
		self.__completed = True

	def get_parent(self):
		return self.__parent

	def get_last_value(self) -> str:
		return self.__values[-1:]

	def get_values(self) -> str:
		return self.__values

	def add_value(self, value: str):
		self.__values += value
		self.__previous_value += 1

	def get_previous_value(self) -> str:
		if self.__previous_value < 0: return ''
		self.__previous_value -= 1
		return self.__values[self.__previous_value + 1]

	def create_child(self, first_value: str):
		self.__children.append(Branch(self))
		self.__children[-1].add_value(first_value)

	def get_children(self):
		return self.__children
