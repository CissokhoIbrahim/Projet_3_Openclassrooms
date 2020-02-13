from macgyver import MacGyver

# Gestionnaire du labyrinthe
class maze:


	# Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
	def __init__(self):

		# Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
		# déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
		self.mac_gyver = None
		self.labyrinthe = self.parse_file()
		# self.keys = self.append_objects()

	# Méthode qui gère la parsing du fichier .txt représentant le labyrinthe
	def parse_file(self):

		# On crée les variables / tableaux nécessaire à la méthode
		content = {}
		x, y = 0, 0

		# On ouvre le fichier en lecture et on affecte son contenu à "f"
		f = open("labyrinthe.txt", "r")

		# On parcours les lignes de "f"
		for line in f:
		# On parcours les caractères de "line"
			for caracter in line:
			# Si le caractère est un 'retour a la ligne"
				if caracter == "\n":
					# on repasse y à 0, et x à x+1
					y = 0
					x = x+1
				# Si le caractère n'est pas un 'retour a la ligne'
				else:
					# On créer la paire "clé : valeur" dans le dictionnaire "content"
					content[(x, y)] = caracter
					if caracter == 'd':
						self.mac_gyver = MacGyver([x,y])
						# On ajoute 1 à y
						y = y+1
		return content


# Créer une méthode qui récupère toutes les "clés" de l'attribut "self.labyrinthe"
# dont la valeur est "c" (pour chemin !)

	def get_keys(self):
		liste = []
		for key, value in self.labyrinthe.items():
			if value == 'c':
				liste.append(key)
		return liste

	def random_coordinates(self):
		import random
		liste = self.get_keys()
		liste_coordinates = []
		# je parcours 3 fois
		for i in range(0,3):
			random.shuffle(liste)
			liste_coordinates.append(liste[0])
			liste.pop(0)
		return liste_coordinates


	# Ensuite, se servir de cette méthode pour récupérer 3 coordonnées,
	# aléatoirement, afin d'y placer nos 3 objets (tube, ether, seringue)

	def append_objects(self):
		liste = self.random_coordinates()
		liste_append_objects = liste
		liste_append_objects[0] = "t"
		liste_append_objects[1] = "e"
		liste_append_objects[2] = "s"
		return liste_append_objects

	def bottom(self):
		self.mac_gyver.coordinates[0] += 1

	def top(self):
		self.mac_gyver.coordinates[0] -= 1

	def left(self):
		self.mac_gyver.coordinates[1] -= 1

	def right(self):
		self.mac_gyver.coordinates[1] += 1


if __name__== "__main__":

	# On instancie un objet "maze"

	m = maze()


	# je veux aller en bas :
	m.right()
	print(m.mac_gyver.coordinates)