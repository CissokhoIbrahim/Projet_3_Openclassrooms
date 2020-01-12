# Gestionnaire du labyrinthe

class labyrinthe:

	def __init__(self):
		self.nom = "Le coeur du labyrinthe"



		def parse_file(self):
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


		""" def get_to_file(self):
			with open("labyrinthe.txt", "rb") as file:
				my_depickler = pickle.Unpickler(file)
				get_to_file = my_depickler.load()
				"""


if __name__== "__main__":
	p = labyrinthe()
	print( p.parse_file() ) 

