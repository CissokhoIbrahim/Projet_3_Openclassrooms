#Importation des bibliothèques nécessaires

import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640,480))

#Chargement et collage du fond
fond = pygame.image.load("structures.png").convert()
fenetre.blit(fond, (0, 0))

#Chargement et collage du personnage
perso = pygame.image.load("macgyver.png").convert_alpha()
perso_x = 0
perso_y = 0
fenetre.blit(perso, (perso_x, perso_y))

#Rafraîchissement de l'écran
pygame.display.flip()


#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:

				perso_x = event.pos[0]
				perso_y = event.pos[1]


fenetre.blit(fond, (0, 0))
fenetre.blit(perso, (perso_x, perso_y))

pygame.display.flip()