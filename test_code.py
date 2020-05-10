from macgyver import MacGyver

# Gestionnaire du labyrinthe
class maze:


    # Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
    def __init__(self):

        # Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
        # déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
        self.mac_gyver = None
        self.labyrinthe = self.parse_file()
        self.verif = self.parse_laby()

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


    # Les différentes fonctions que Mac_gyver emprunte

    def bottom(self):
        self.mac_gyver.coordinates[0] += 1

    def top(self):
        self.mac_gyver.coordinates[0] -= 1

    def left(self):
        self.mac_gyver.coordinates[1] -= 1

    def right(self):
        self.mac_gyver.coordinates[1] += 1

    def bottom(self):
        m.move("bottom")

    def top(self):
        m.move("top")

    def left(self):
        m.move("left")

    def right(self):
        m.move("right")

    def bottom(self):
        if self.check_move(): 
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[0] += 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"


    def top(self):
        if self.check_move():
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[0] -= 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"



    def left(self):
        if self.check_move():
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[1] -= 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"


    def right(self):
        if self.check_move():
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
        self.mac_gyver.coordinates[1] += 1
        self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

        # Une fonction qui récupère, trouve les nouvelles coordonées de macgyver et de sa position initiale et de sa direction et renvoie ses nouvelles coordonnées
        
        def find_new_coo(self, direction=False):
            m_c = self.mac_gyver.coordinates

            if direction == "bottom":
                m_c[0] += 1

            if direction == "top":
                m_c[0] -= 1

            if direction == "left" :
                m_c[1] -= 1

            if direction == "right":
                m_c[1] += 1

            return m_c

        def check_move(self):
        # Récupération des coordonnées de labyrinthe 
        case_y = self.mac_gyver.coordinates[0]
        case_x = self.mac_gyver.coordinates[1]
        # Si c'est un mur retourner False
        if case_x or case_y == "ctse":
            return True
        elif case_x or case_y == "g" and self.mac_gyver.bag == 3:
            return True
        elif case_x or case_y == "m":
            return False
        # Sinon tout ce qui sera endehors de ses diférentes conditions, sera False.
        else :
            return False
            
        def check_move(self):
            # Récupération des coordonnées de labyrinthe 
            case = self.labyrinthe[tuple(self.mac_gyver.coordinates)]
            # Si c'est un mur retourner False
            if case == 'm':
                return False
            # Si l'object 't' est sur la case,  ramasser cet objet
            if case == 't':
                return True
            # Si l'object 'e' est sur la case, ramasser cet objet
            if case == 'e':
                return True
            # Si l'object 's' est sur la case, ramasser cet objet
            if case == 's':
                return True
            # Si le macgyver est sur la case du gardien et qu'il a ramasser les 3 objects, il aura gagné
            if case == 'g' and objects == 3:
                return True
            # Sinon tout ce qui sera endehors de ses diférentes conditions, sera False.
            return False
            
    def move(self, direction=True):
        self.parse_laby()
        if self.check_move():
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

            
    def move(self):
        laby = self.parse_laby()
        case = self.check_move()
        m_c = self.mac_gyver.coordinates
        a = input(" Les flêches directionnelles sont : Gauche = q ; Bas = s ; Haut = z ; Droite = f : ")
        if a == "q":
            if case == ' ':
                m_c[1] -= 1
                case = ' '
            elif case == 't' 'e' 's':
                case = m_c
                Objects += 1
                case = ' '
        if a == "s":
            if case == ' ':
                m_c[0] -= 1
                case = ' '
            elif case == 't' 'e' 's':
                case = m_c
                Objects += 1
                case = ' '
        if a == "z":
            if direction == ' ':
                m_c[1] -= 1
                case = ' '
            elif case == 't' 'e' 's':
                case = m_c
                Objects += 1
                case = ' '
        if a == "f":
            if direction == ' ':
                m_c[1] += 1
                case = ' '
            elif case == 't' 'e' 's':
                case = m_c
                Objects += 1
                case = ' '
        if sac_objets == 3:
            print("Vous avez gagnez ! ")
        else:
            print("Vous avez perdu ! ")


        q = self.left()
        d = self.right()
        w = self.bottom()
        z = self.top()
        case = self.labyrinthe[tuple(self.mac_gyver.coordinates)]



if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()
    print(m.verif)