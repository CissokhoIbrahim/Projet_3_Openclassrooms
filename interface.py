#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The imports for differents modules
"""
import pygame
from labyrinthe import Maze
from constante import COTE_FENETRE

class Intermaze():
    """docstrig for InterMaze"""
    m = Maze()

    pygame.init()
    # Open of the Pygame window
    fenetre = pygame.display.set_mode((COTE_FENETRE, COTE_FENETRE))
    # tittle of window
    pygame.display.set_caption("Maze")
    # The bakground at the maze
    fond = pygame.image.load("ressource/fond.jpg")
    # Loading the window
    fenetre.blit(fond, (0, 0))
    m.picture_maze(fenetre)
    pygame.display.flip()

    continuer = 1
    while continuer:
        pygame.time.Clock().tick(30)
        # Course of the various events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    m.move("bottom")
                if event.key == pygame.K_UP:
                    m.move("top")
                if event.key == pygame.K_LEFT:
                    m.move("left")
                if event.key == pygame.K_RIGHT:
                    m.move("right")
                if event.key == pygame.BREAK:
                    continuer = 0
                # Refreshing the screen
                fenetre.blit(fond, (0, 0))
                m.picture_maze(fenetre)
                pygame.display.flip()
if __name__ == '__main__':

    t = Intermaze()

    print(t)
