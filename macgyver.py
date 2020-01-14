class MacGyver(maze):

	def __init__(self):
		self.right = "r"
		self.left = "l"
		self.bottom = "b"
		self.top = "t"
		self.name_Mac = "MacGyver"
		self.destination = {(x, y): "way"}
		self.wall = {(x, y): "wall"}
		self.grid_way = {(x, y): "grid of the way"}
		self.Pick up = {(x, y): "Pick up"}

	def right(self):
		self.right = input("Tap the 'r' button to go to right : ")
		if self.right == "r":
			self.right += 1

	def bottom(self):
		self.bottom = input("Tap the 'b' button to go to bottom : ")
		if self.bottom == "b":
			self.bottom -= 1


	def left(self):
		self.left = input("Tap the 'l' button to go to left : ")
		if self.left == "l":
			self.left -= 1			


	def top(self):
		self.top = input("Tap the 'r' button to go to top : ")
		if self.top == "t":
			self.top += 1


	def destination(self):
		if self.destination is not self.grid_way:
			self.destination += 1
		elif self.destination  is not self.grid_way:
			self.destination += 1
		elif self.money or self.jewelry:
			self.Pick up = self.name_Mac
		elif self.name_Gard == self.name_Gard:
			self.destination -= 1