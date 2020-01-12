class Objets(Gardien, MacGyver, Gestion_labyrinthe):

	def __init__(self):
		self.nom = "Objets"
		self.argent = "Argent"
		self.bijoux = "Or"


	def chemins(self):
		if self.droite == self.argent:
			self.argent += 1
		elif self.droite == self.bijoux:
			self.bijoux += 1
		if self.bas == self.argent:
			self.argent -= 1
		elif self.bas == self.bijoux:
			self.bijoux -= 1
		if self.gauche == self.argent:
			self.argent -= 1
		elif self.gauche == self.bijoux:
			self.bijoux -= 1
		if self.haut == self.argent:
			self.argent += 1
		elif self.haut == self.bijoux:
			self.bijoux += 1