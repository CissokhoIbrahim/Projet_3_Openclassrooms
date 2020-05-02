from macgyver import MacGyver
from objets import Objects
# Gestionnaire du labyrinthe
class maze:


    # Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
    def __init__(self):

        # Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
        # déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
        self.mac_gyver = None
        self.labyrinthe = self.parse_file()
        self.get_objects = self.get_items()
        self.mac_gyver.bag = 0

    # Méthode qui gère le parsing du fichier .txt représentant le labyrinthe

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
                # Si le caractère est un 'd' alors créer la paire de clés 'MacGyver' "
                if caracter == 'd':
                    self.mac_gyver = MacGyver([x, y])
                # Si le caractère est un 'retour a la ligne"    
                if caracter == "\n":
                    # on repasse y à 0, et x à x+1
                    y = 0
                    x = x+1
                
                # Sinon le caractère n'est pas un 'retour a la ligne'
                else:
                    # On créer la paire "clé : valeur" dans le dictionnaire "content"
                    content[(x, y)] = caracter
                    y = y+1
        return content


    # Créer une méthode qui récupère toutes les "clés" de l'attribut "self.labyrinthe" dont la valeur est "c" (pour chemin !)

    def get_keys(self):
        liste = []
        for key, value in self.labyrinthe.items():
            if value == 'c':
                liste.append(key)
        return liste

    # Cette fonction chosir aléatoirement 3 coordonées

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

    def get_items(self):
        liste = self.random_coordinates()
        self.labyrinthe[(tuple(liste[0]))] = "t"
        self.labyrinthe[(tuple(liste[1]))] = "s"
        self.labyrinthe[(tuple(liste[2]))] = "e"
        return liste

    # Les différentes fonctions que Mac_gyver emprunte pour ses déplacements

    def bottom(self):
        if self.check_move(): 
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
            self.mac_gyver.coordinates[0] += 1
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
        elif self.mac_gyver.bag == "tse":
            self.mac_gyver.bag += 1
            print("Vous avez", self.mac_gyver.bag, "objet !!! ")


    def top(self):
        if self.check_move():
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
            self.mac_gyver.coordinates[0] -= 1
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
        elif self.mac_gyver.bag == "tse":
            self.mac_gyver.bag += 1
            print("Vous avez", self.mac_gyver.bag, "objet !!! ")



    def left(self):
        if self.check_move():
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
            self.mac_gyver.coordinates[1] -= 1
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
        elif self.mac_gyver.bag == "tse":
            self.mac_gyver.bag += 1
            print("Vous avez", self.mac_gyver.bag, "objet !!! ")



    def right(self):
        if self.check_move():
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
            self.mac_gyver.coordinates[1] += 1
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
        elif self.mac_gyver.bag == "tse":
            self.mac_gyver.bag += 1
            print("Vous avez", self.mac_gyver.bag, "objet !!! ")

    def check_move(self):
        # Récupération des coordonnées de labyrinthe 
        case = self.labyrinthe[tuple(self.mac_gyver.coordinates)]
        # Si c'est un mur retourner False
        if case == "mtse" or case == "g" and self.mac_gyver.bag == 3:
            return True
        # Sinon tout ce qui sera endehors de ses diférentes conditions, sera False.
        else :
            return False

    def parse_laby(self):
        line = ""
        cpt = 0
        for key, value in self.labyrinthe.items():
            if value == "m":
                line += "#"
            if value == "c":
                line += " "
            if value == "t":
                line += "T"
            if value == "s":
                line += "S"
            if value == "e":
                line += "E"
            if value == "d":
                line += "M"
            if value == "g":
                line += "G"
            cpt += 1
            if cpt == 15:
                print(line)
                cpt = 0
                line = ""
        return line


    def move(self, direction):
        self.parse_laby()
        if check_move():
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
            if direction == "bottom":
                self.mac_gyver.coordinates[0] += 1
            if direction == "top":
                self.mac_gyver.coordinates[0] -= 1
            if direction == "left":
                self.mac_gyver.coordinates[1] -= 1
            if direction == "right":
                self.mac_gyver.coordinates[1] += 1
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"


if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()

    print(m.parse_laby())
    m.left()
    print(m.parse_laby())