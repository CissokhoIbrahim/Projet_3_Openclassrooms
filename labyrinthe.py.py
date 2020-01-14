# Gestionnaire du labyrinthe
class maze:

# Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
	def __init__(self):
# Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
# déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
		self.labyrinthe = self.parse_file()

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
# On ajoute 1 à y
				y = y+1
				return content

# Créer une méthode qui récupère toutes les "clés" de l'attribut "self.labyrinthe"
# dont la valeur est "c" (pour chemin !)


# Ensuite, se servir de cette méthode pour récupérer 3 coordonnées,
# aléatoirement, afin d'y placer nos 3 objets (tube, ether, seringue)


if __name__== "__main__":
# On instancie un objet "maze"
	m = maze()

# On affiche l'attribut "labyrinthe" de l'objet "maze", qui s'est automatiquement
# créé grâce au constructeur
	print(m.labyrinthe)
