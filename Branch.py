class Branch:

	def __init__(self, parent):
		self.__parent = parent
		self.__values = ""
		self.__children = []

	def get_parent(self):
		return self.__parent

	def get_last_value(self) -> str:
		return self.__values[-1]

	def add_value(self, value: str):
		self.__values.append(value)

	def create_children(self, amount: int):
		for i in range(amount):
			self.__children.append(Branch(self))
