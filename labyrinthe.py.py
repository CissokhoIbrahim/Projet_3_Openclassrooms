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
			content = {}

			x,y = (), ()

			f = open("labyrinthe.txt", "r")
			for line in f:
				for caracter in line:
					content[(x, y)] = caracter
					y+1
					if(y == 15):
						y = 0
				x+1
			print(content)


		def get_to_file(self):
			with open("Dessin_du_labyrinthe.txt", "rb") as file:
				my_depickler = pickle.Unpickler(file)
				get_to_file = my_depickler.load()
			



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
	print(p.parse_filetxt_into_dic())
