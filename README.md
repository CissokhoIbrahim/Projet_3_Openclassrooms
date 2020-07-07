OC-Projet.3 --- Labyrinthe-MacGyver

Introduction :

Dans ce projet qui consiste à créer un labyrinthe en mode graphique, nous avons pour objectif de créer una labyrinthe avec comme personnage; macgyver, le guardien et les objets qui y sont répartir aléatoirement. 

J'ai opter pour faire un labyrinthe en deux parties: 

- Une en mode console, ce qui me permettra de créer les fonctions nécessaire au fonctionnement du labyrinthe.
- Et une en mode graphique qui va nous permettre d'utiliser les fonctionnalitées en mode console pour pouvoir jouer en mode graphique.

Pré-requis :

Pour entamer ce projet, il faut d'abord avoir certains pré-requis telle que le fait de connaitre un minimum le langage python et s'exercé dans différents exercices pour faire ce projet.

Installation :

L'installation dans ce projet, est simple, il m'a suffit d'utiliser l'éditeur sublime text, la console git bash et mon repo sur github.

Configuration :

J'ai diviser la configuration du labyrinthe en plusieurs étapes, la première est la création des class de macgyver, guardien, et des objets. Ensuite j'ai créer un script que j'ai nommer labyrinthe.py, dans ce script, il y a la class maze qui gère toutes les fonctionnalités du labyrinthe.

Les touches directionnelles :

Pour jouer au jeu du labyrinthe sur interface, c'est simple, il suffit d'initialiser les fichiers suivant : 
- labyrinthe.py
- cosntantes.py
- interface_laby.py

Ensuite ouvrir la console git bash et faire ceci : 

a/ cd Documents/
b/ cd ProjetInformatique/
c/ cd Projet_3/
d/ python interface_laby.py 

Après avoir passer cette ligne de commande sur git bash, le jeu du labyrinthe s'affichera et pour faire bouger macgyver avec les touches directionnelles, il suffit de jouer avec les flèches de votre ordinateur, pour ramasser, pas besoin d'une touche ssecondaire, vous devez juste aller sur la case de l'objet pour le ramasser, vous ne pouvez pas traverser les murs et pour gagner il vous faut ramasser les trois objets et se présenter devant le gardien pour gagner sinon vous avez perdu. 


