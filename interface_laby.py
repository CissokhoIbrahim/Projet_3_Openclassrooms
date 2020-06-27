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
pygame.display.flip()

#BOUCLE INFINIEn b
continuer = 1
while continuer:
	pygame.time.Clock().tick(30)
	# Parcours des différents évenements
	for event in pygame.event.get(): 
		if(event.type == pygame.KEYDOWN):
			if event.key == K_DOWN:
				m.move("right")
			if event.key == K_UP:
				m.move("left")
			if event.key == K_LEFT:
				m.move("top")
			if event.key == K_RIGHT:
				m.move("bottom")
			if event.key == QUIT:
				continuer = 0
			fenetre.blit(fond, (0,0))
			m.afficher(fenetre)
			pygame.display.flip()