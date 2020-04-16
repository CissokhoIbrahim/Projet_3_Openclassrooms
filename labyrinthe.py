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

    def append_objects(self):
        liste = self.random_coordinates()
        liste[0] = 't'
        print(liste[0])
        liste[1] = 's'
        liste[2] = 'e'
        return liste

    # Les différentes fonctions que Mac_gyver emprunte


    def bottom(self):    
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[0] += 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

    def top(self):
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[0] -= 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"


    def left(self):
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[1] -= 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"


    def right(self):
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[1] += 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
    

    def parse_laby(self):
        objects = self.append_objects()
        line = ""
        cpt = 0
        for key, value in self.labyrinthe.items():
            if value == "m":
                line += "#"
            if value == "c":
                line += " "
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

    def check_move(self):
        if self.mac_gyver.coordinates[1] < 0 or self.mac_gyver.coordinates[0] < 0:
            return None
        elif self.mac_gyver.coordinates[0] or self.mac_gyver.coordinates[1] != " ":
            return None
        else :
            return [self.mac_gyver.coordinates[0], self.mac_gyver.coordinates[1]]
    
    def move(self):
        case = self.labyrinthe[tuple(self.mac_gyver.coordinates)]
        objects = self.append_objects()
        self.parse_laby()
        self.check_move()
        a = input(" Les flêches directionnelles sont : Gauche = q ; Bas = w ; Haut = z ; Droite = d : ")
        if a == "w":
            self.bottom()
        elif a == "z":
            self.top()
        elif a == "d":
            self.right()
        elif a == "q":
            self.left()
        if case == objects:
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
            self.custom_count += 1
            self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        if case == "G":
            print("Le nombre d'objects récupérer : {} et l'object lui même %s"% str (append_objects)(self.custom_count))
        if objects == 3:
            printt("MacGyver à gagner !!!!!! ")
        else :
            print("Il a perdu !!!! ")         
        self.parse_laby()



if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()

    print(m.append_objects())