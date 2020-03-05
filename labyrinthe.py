from macgyver import MacGyver

# Gestionnaire du labyrinthe
class maze:


	# Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
	def __init__(self):

		# Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
		# déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
		self.mac_gyver = None
		self.labyrinthe = self.parse_file()
		self.verif = self.check_move()
		self.objects = self.liste_append_objects()

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
		liste_1 = []
		for key, value in self.labyrinthe.items():
			if value == 'c':
				liste.append(key)
		return liste

# Cette fonction chosir aléatoirement 3 coordonées

	def random_coordinates(self):
		import random
		liste_2 = self.get_keys()
		liste_coordinates = []
		# je parcours 3 fois
		for i in range(0,3):
			random.shuffle(liste_2)
			liste_coordinates.append(liste_2[0])
			liste_2.pop(0)
		return liste_coordinates


	# Ensuite, se servir de cette méthode pour récupérer 3 coordonnées,
	# aléatoirement, afin d'y placer nos 3 objets (tube, ether, seringue)

	def append_objects(self):
		liste_3 = self.labyrinthe()
		liste_append_objects = liste_3
		liste_append_objects[0] = "t"
		liste_append_objects[1] = "e"
		liste_append_objects[2] = "s"
		return liste_append_objects

	# Les différentes fonctions que Mac_gyver emprunte

	def bottom(self):
		self.mac_gyver.coordinates[0] += 1

	def top(self):
		self.mac_gyver.coordinates[0] -= 1

	def left(self):
		self.mac_gyver.coordinates[1] -= 1

	def right(self):
		self.mac_gyver.coordinates[1] += 1

	# Une fonction qui récupère, trouve et renvoie trouve les coordonnées de Mac_gyver
	def find_new_coo(self):
		m_c = self.mac_gyver.coordinates

		if m_c == "bottom":
			m_c[0] += 1

		if m_c == "top":
			m_c[0] -= 1

		if m_c == "left" :
			m_c[1] -= 1

		if m_c == "right":
			m_c[1] += 1

		return m_c

	def check_move(self):
		destination = self.find_new_coo()
		for (x, y) in self.labyrinthe:
			if destination == 'c':
				return True

			elif destination == self.labyrinthe:
				return True

			elif destination == 'm' or not self.labyrinthe:
				return False

	def move(self):
		r = self.right()
		l = self.left()
		b = self.bottom()
		t = self.top()
		destination = self.find_new_coo()
		ch_mv = self.check_move()
		objects_three = liste_append_objects()

		if destination == ch_mv:
			if destination == 'c':
				destination[0] += 1
				destination[0] -= 1
				destination[1] -= 1
				destination[1] += 1
				ch_mv = 'c'
			if ch_mv == objects_three:
				ch_mv = destination
				destination.append(objects_three)
				ch_mv = 'c'
			if destination == 'g':
				destination(len(objects_three))
			if destination == objects_three:
				print("Gagné")
			else:
				print("Perdu")




if __name__== "__main__":

	# On instancie les différents objets "maze", juste en bas :
	m = maze()

	print(m.move())