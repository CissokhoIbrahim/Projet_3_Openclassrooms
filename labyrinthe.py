from macgyver import MacGyver
# Gestionnaire du labyrinthe
class maze:


    # Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
    def __init__(self):

        # Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
        # déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
        self.labyrinthe = self.parse_file()
        # Lors de l'instanciation de l'objet, la variable "Macgyver" est automatiquement
        # déclenchée, et sa valeur est None
        self.mac_gyver = None
        # Lors de l'instanciation de l'objet, la méthode "get_items" est automatiquement
        # déclenchée, et son contenu est inséré dans un attribut "self.get_objects"
        self.get_objects = self.get_items()
        # Nous instancions le compteur du sac à dos de "Macgyver" à 0, il doit ramasser 3 objets
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
        self.labyrinthe[(tuple(liste[0]))] = 't'
        self.labyrinthe[(tuple(liste[1]))] = 's'
        self.labyrinthe[(tuple(liste[2]))] = 'e'
        return liste

    # Les différentes fonctions de déplacements de Mac_gyver

    def bottom(self):
        m.move("bottom")

    def top(self):
        m.move("top")

    def left(self):
        m.move("left")

    def right(self):
        m.move("right")

    # La fontion check_move qui vérifie si le déplacement est autorisé et si ont peut ramasser un objet ou non
    def check_move(self, direction = False):

        destination = None

        a = input(" La direction est soit : Gauche = q ; Bas = w ; Haut = z ; Droite = f ou exit/o pour quitter : ")        
        
        if direction == "bottom" or a == "w":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0] + 1, self.mac_gyver.coordinates[1])]
        
        if direction == "top" or a == "z":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0] -1, self.mac_gyver.coordinates[1])]
        
        if direction == "left" or a == "q":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0], self.mac_gyver.coordinates[1] - 1)]
        
        if direction == "right" or a == "f":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0], self.mac_gyver.coordinates[1] + 1)]


        print(destination)

        if destination == "m":
            print("Vous ne pouvez pas franchir un mur !!! ")
            return False
        
        if destination == "c":
            return True
        
        if destination == 't':
            self.mac_gyver.bag += 1
            print("Vous avez pour l'instant {} objet ".format(self.mac_gyver.bag))
            return True
            
        if destination == 's':
            self.mac_gyver.bag += 1
            print("Vous avez pour l'instant {} objet ".format(self.mac_gyver.bag))
            return True
            
        if destination == 'e':
            self.mac_gyver.bag += 1
            print("Vous avez pour l'instant {} objet ".format(self.mac_gyver.bag))
            return True
        
        if destination == "g":
            print("Vous avez ramasser : {} objets en tout ".format(self.mac_gyver.bag))
            if self.mac_gyver.bag == 3:
                print("Vous avez gagnez !!! ")
                return True
            else:
                print("Vous avez perdu !!! ")
                return True
        else:
            return True

    # Cette fonction dessine la fonction (self.labyrinthe), de 15 lignes.
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

    # Cette fonction récupère les différents déplacements de Macgyver.
    def move(self, direction = False):
        while True:
            self.parse_laby()
            a = input(" La direction est soit : Gauche = q ; Bas = w ; Haut = z ; Droite = f ou exit/o pour quitter : ")
            if direction == "bottom" or a == "w":
                if self.check_move(direction):
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                    self.mac_gyver.coordinates[0] += 1
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

            if direction == "top" or a == "z":
                if self.check_move(direction):
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                    self.mac_gyver.coordinates[0] -= 1
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

            if direction == "left" or a == "q":
                if self.check_move(direction):
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                    self.mac_gyver.coordinates[1] -= 1
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

            if direction == "right" or a == "f":
                if self.check_move(direction):
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                    self.mac_gyver.coordinates[1] += 1
                    self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"
            if a == "exit" or a == "o":
                print("A bientôt !!! ")
                break
        return self.parse_laby()
    
if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()

    print(m.move())