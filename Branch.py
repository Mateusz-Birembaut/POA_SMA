class Branch:

	def __init__(self, parent: 'Branch' = None):
		self.__parent = parent
		self.__values = ''
		self.__previous_value = -1
		self.__children: list[Branch] = []

	def get_parent(self):
		return self.__parent

	def get_last_value(self) -> str:
		return self.__values[-1:]

	def add_value(self, value: str):
		self.__previous_value += 1
		self.__values += value

	def get_previous_value(self) -> str:
		if self.__previous_value < 0: return ''
		self.__previous_value -= 1
		return self.__values[self.__previous_value + 1]

	def create_children(self, amount: int):
		for i in range(amount):
			self.__children.append(Branch(self))
