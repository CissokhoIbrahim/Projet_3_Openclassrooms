import pygame
from pygame.locals import *
from labyrinthe import maze
from constantes_2 import *
from macgyver import MacGyver

m = maze()

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.display.set_caption("Maze")

fond = pygame.image.load("ressource/fond.jpg")
fenetre.blit(fond, (0,0))

m.afficher(fenetre)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIEn b
continuer = 1
while continuer:
	pygame.time.Clock().tick(30)
	# Parcours des différents évenements
	for event in pygame.event.get(): # Attente des événements
		#Touches de déplacement de Donkey Kong
		if event.type == K_RIGHT:
			m.move("right")
		if event.type == K_LEFT:
			m.move("left")
		if event.type == K_UP:
			m.move("top")
		if event.type == K_DOWN:
			m.move("bottom")

		if event.type == QUIT:
			continuer = 0
	
#Re-collage
fenetre.blit(fond, (0,0))
m.afficher(fenetre)
fenetre.blit(m.move(), (self.macgyver.coordinates[0], self.macgyver.coordinates[1]))
#Rafraichissement
pygame.display.flip()
