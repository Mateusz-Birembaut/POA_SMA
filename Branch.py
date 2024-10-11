class Branch:

	def __init__(self, parent: Branch):
		self.parent = parent
		self.values = ""
		self.children = []

	def add_value(self, value: str):
		self.values.append(value)

	def create_children(self, amount: int):
		for i in range(amount):
			self.children.append()
