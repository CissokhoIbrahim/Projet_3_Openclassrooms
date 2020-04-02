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

                if caracter == 'd':
                    self.mac_gyver = MacGyver([x,y])
                    # On ajoute 1 à y
                    y = y+1
        return content

    def parse_laby(self):
        laby = self.labyrinthe
        for key, value in laby.items():
            if value == 'm':
                value = "#"
            if value == 'c':
                value = " "
            if value == 'a':
                value = " "
            print(value)

        for line in laby:
            for value in line:
                print(value)

if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()
    print(m.verif)