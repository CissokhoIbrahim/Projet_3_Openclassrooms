# Gestionnaire du labyrinthe
class maze:


    # Constructeur : se déclenche automatiquement lors de la création d'un objet "maze"
    def __init__(self):

        # Lors de l'instanciation de l'objet, la méthode "parse_file" est automatiquement
        # déclenchée, et son contenu est inséré dans un attribut "self.labyrinthe"
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


    # Les différentes fonctions que Mac_gyver emprunte


    def bottom(self, direction=False):
        a = input("Appuyer sur la touche 'w' pour aller en bas ! ")
        if a == "w":
            self.parse_laby(1+1, 4)

    def top(self):
        a = input("Appuyer sur la touche 'z' pour aller en haut : ")
        if a == "z":
            print("Vous êtes bien en haut")


    def left(self):
        a = input("Appuyer sur la touche 'q' pour aller à gauche : ")
        if a == "q":
            print("Vous êtes bien à gauche")

    def right(self):
        a = input("Appuyer sur la touche 'd' pour aller en bas ! ")
        if a == "d":
            print("Vous êtes bien à droite")
    

    def parse_laby(self):
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


if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()

    m.bottom()
    print(m.parse_laby())