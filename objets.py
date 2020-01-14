class Objects(Gard, MacGyver, maze):

	def __init__(self):
		self.name = "Objects"
		self.money = "Money"
		self.jewelry = "gold"


	def paths(self):
		if self.right == self.money:
			self.money += 1
		elif self.right == self.jewelry:
			self.jewelry += 1
		if self.bottom == self.money:
			self.money -= 1
		elif self.bottom == self.jewelry:
			self.jewelry -= 1
		if self.left == self.money:
			self.money -= 1
		elif self.left == self.jewelry:
			self.jewelry -= 1
		if self.top == self.money:
			self.money += 1
		elif self.top == self.jewelry:
			self.jewelry += 1