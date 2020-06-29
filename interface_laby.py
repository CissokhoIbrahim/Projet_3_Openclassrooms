import pygame
from pygame.locals import *
from labyrinthe import maze
from constantes_2 import *
from macgyver import MacGyver

m = maze()

pygame.init()

# #Ouverture of the Pygame window
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

# tittle of window
pygame.display.set_caption("Maze")
# The bakground at the maze
fond = pygame.image.load("ressource/fond.jpg")

# Loading the window
fenetre.blit(fond, (0,0))
m.picture_maze(fenetre)
pygame.display.flip()

# while = 1
Part_of_the_game = 1
while Part_of_the_game:
	pygame.time.Clock().tick(30)
	# Course of the various events
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
				Part_of_the_game = 0
			if event.key == K_ESCAPE:
				Part_of_the_game = 0
			# Refreshing the screen
			fenetre.blit(fond, (0,0))
			m.picture_maze(fenetre)
			pygame.display.flip()