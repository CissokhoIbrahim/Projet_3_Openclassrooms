# Gestionnaire du labyrinthe

class maze:

	def __init__(self):
		self.name = "labyrinthe"
		self.parse_file = self.parse_file()
		

		def parse_file(self):
			content = {}, {}, {}, {}

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


if __name__== "__main__":
	first_object = maze()
	print(first_object.parse_file())


