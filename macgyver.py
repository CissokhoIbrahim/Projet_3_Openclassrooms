class MacGyver(maze):

	def __init__(self):
		self.right = "r"
		self.left = "l"
		self.bottom = "b"
		self.top = "t"
		self.Mac = "Mac"
		
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


if __name__== "__main__":
# On instancie un objet "maze"
	m = maze()
	j = maze()

# On affiche l'attribut "labyrinthe" de l'objet "maze", qui s'est automatiquement
# créé grâce au constructeur
	