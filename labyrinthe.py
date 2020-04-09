from macgyver import MacGyver
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


    # Les différentes fonctions que Mac_gyver emprunte


    def bottom(self, direction=False):
        a = input("Appuyer sur la touche 'W' pour aller en haut : ")
        if a == "W":
            self.mac_gyver.coordinates[0] += 1

    def top(self):
        a = input("Appuyer sur la touche 'z' pour aller en haut : ")
        if a == "z":
            self.mac_gyver.coordinates[0] -= 1


    def left(self):
        a = input("Appuyer sur la touche 'q' pour aller à gauche : ")
        if a == "q":
            self.mac_gyver.coordinates[1] -= 1

    def right(self):
        a = input("Appuyer sur la touche 'd' pour aller  àdroite ! ")
        if a == "d":
            self.mac_gyver.coordinates[1] += 1
    




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
        return line


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

if __name__== "__main__":

    # On instancie les différents objets "maze", juste en bas :
    m = maze()

    
    print(m.parse_laby())
    m.bottom()
    print(m.parse_laby())
