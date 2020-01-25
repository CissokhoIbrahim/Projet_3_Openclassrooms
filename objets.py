class Objects():

	def __init__(self):
		

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

	

if __name__== "__main__":
# On instancie un objet "maze"
	j = Objects()

# On affiche l'attribut "labyrinthe" de l'objet "maze", qui s'est automatiquement
# créé grâce au constructeur

	print()