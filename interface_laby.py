import pygame
from pygame.locals import *
from labyrinthe import maze
from constantes_2 import *

m = maze()

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.display.set_caption("Maze")

fond = pygame.image.load("ressource/fond.jpg")
fenetre.blit(fond, (0,0))
#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	pygame.time.Clock().tick(30)

	# Parcours des différents évenements
	for event in pygame.event.get(): # Attente des événements
		if event.type == QUIT:
			continuer = 0
	
#Re-collage
fenetre.blit(fond, (0,0))
m.afficher(fenetre)
#Rafraichissement
pygame.display.flip()
