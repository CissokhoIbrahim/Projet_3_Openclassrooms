import pickle

class Gestion_labyritnhe:

	{
(x, y): "mur",
(x, y): "chemin",
(x, y): "McGyver",
(x, y): "Gardien",
	}

	with open('Dessin_du_labyrinthe.txt', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(score)
			

class MacGyver:


	def __init__(self):
		self.nom = "MacGyver"



class Gardien:


	def __init__(self):
		self.nom = "Gardien"


