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
 
def remplacer(chaine,i,car):
    """remplace le ième caractère de la chaine par caractère"""
    s=chaine[:i]+car+chaine[i+1:]
    return s
 
while (perso_l!=9) or (perso_c!=8) :
    a = input("ou voulez vous aller:(gauche = q, droite = d, haut = z, bas = s)")
    if a == "q":
        if laby[perso_l][perso_c-1] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l][perso_c-1] == " " :
            laby[perso_l]=remplacer(laby[perso_l],perso_c-1,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_c=perso_c-1
    if a == "d":
        if laby[perso_l][perso_c+1] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l][perso_c+1] == " " :
            laby[perso_l]=remplacer(laby[perso_l],perso_c+1,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_c=perso_c+1
    if a == "z":
        if laby[perso_l-1][perso_c] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l-1][perso_c] == " " :
            laby[perso_l-1]=remplacer(laby[perso_l-1],perso_c,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_l=perso_l-1
    if a == "s":
        if laby[perso_l+1][perso_c] == "*" :
            print("vous ne pouvez pas passer!")
        elif laby[perso_l+1][perso_c] == " " :
            laby[perso_l+1]=remplacer(laby[perso_l+1],perso_c,"8")
            laby[perso_l]=remplacer(laby[perso_l],perso_c," ")
            perso_l=perso_l+1
    if perso == [9,8] :
        print("Bravo vous avez terminé !!!!!")
    afficher(laby)