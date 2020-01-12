class MacGyver(labyrinthe):

	def __init__(self):
		self.droite = "r"
		self.gauche = "l"
		self.bas = "b"
		self.haut = "t"
		self.nom_Mac = "MacGyver"
		self.destination = {(x, y): "chemin"}
		self.mur = {(x, y): "mur"}
		self.grille_labyrinthe = {(x, y): "grille du labyrinthe"}
		self.ramasser = {(x, y): "ramasser"}

	def droite(self):
		self.droite = input("Taper la touche 'r' pour aller à doite : ")
		if self.droite == "r":
			self.droite += 1

	def bas(self):
		self.bas = input("Taper la touche 'b' pour aller en bas : ")
		if self.bas == "b":
			self.bas -= 1


	def gauche(self):
		self.gauche = input("Taper la touche 'l' pour aller à gauche : ")
		if self.gauche == "l":
			self.gauche -= 1			


	def haut(self):
		self.haut = input("Taper la touche 't' pour aller en haut : ")
		if self.haut == "t":
			self.haut += 1


	def destination(self):
		if self.destination is not self.mur:
			self.destination += 1
		elif self.destination  is not self.grille_labyrinthe:
			self.destination += 1
		elif self.argent or self.bijoux:
			self.ramasser = self.nom_Mac
		elif self.nom_Gard == self.nom_Gard:
			self.destination -= 1