class Objects:

	def __init__(self):
		self.custom_count = 0
		self.items = {
			't' : True,

			'e' : True,

			's' : True

		}

	def __str__(self):
		print("Compteur de l'objet : {}".format(self.custom_count))


	def add(self, items = 0):
		if items == 't' and self.items{'t': True}:
			self.custom_count += 1
			return True
		if items == 't' and self.items{'e': True}:
			self.custom_count += 1
			return True
		if items == 't' and self.items{'s': True}:
			self.custom_count += 1
			return True
		return False
	
	


if __name__== "__main__":
# On instancie un objet "maze"
	o = Objects()

	print(o.add)



# On affiche l'attribut "labyrinthe" de l'objet "maze", qui s'est automatiquement
# créé grâce au constructeur
