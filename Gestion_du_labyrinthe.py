# Gestionnaire du labyrinthe

import pickle

class Gestion_labyrinthe:

	def __init__(self):
		self.nom = "Le coeur du labyrinthe"
		self.droite = "r"
		self.gauche = "l"
		self.bas = "b"
		self.haut = "t"
		 

		def parse_filetxt_into_dic(self):
			contenue = {

    (x, y): "mur",
    (x, y): "chemin",
   	(x, y): "ramasser",
    (x, y): "McGyver",
    (x, y): "Gardien",
    (x, y): "grille_labyrinthe",

}
			with open("Dessin_du_labyrinthe.txt", "wb") as file:
				file_txt = pickle.Pickler(file)
				file_txt.dump(contenue)
			
		def get_to_file(self):
			with open("Dessin_du_labyrinthe.txt", "rb") as file:
				my_depickler = pickle.Unpickler(file)
				get_to_file = my_depickler.load()
			

class MacGyver(Gestion_labyrinthe):

	def __init__(self):
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


class Gardien(MacGyver, Gestion_labyrinthe):
	
	def __init__(self):
		self.nom_Gard = "Gardien"		



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

if __name__== "__main__":
	p = Gestion_labyrinthe()