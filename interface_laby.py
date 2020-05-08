laby = ["*8********","* ********","*        *","**** * * *","*    * * *","****** * *","*      * *","* ********","*        *","******** *"]
 
for i in range(10) :
    print(laby[i])
 
perso = [0,1]      #position du personnage
perso_l = 0
perso_c = 1
 
def afficher(laby):
    """affiche un labyrinthe défini comme une liste de chaines"""
    for ligne in laby[:len(laby)]:
        print(ligne)
 
class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    
    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

tab = TableauNoir()

tab.ecrire("Coucou bb comment vas tu ?")
tab.surface