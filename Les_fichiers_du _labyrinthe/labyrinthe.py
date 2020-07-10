#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Macgyver Labyrinthe
Jeu dans lequel on doit déplacer MG jusqu'aux objets à travers un labyrinthe et doit se présenter devant le gardien.

Script Python
Fichiers : labyrinthe.py, constante.py, MacGyver.py, Objets.py, Gardien.py + labyrinthe.txt .
"""


import pygame
from pygame.locals import * 
from macgyver import MacGyver
from constante import *

""" Maze Manager"""
class Maze:
    """ Builder: triggers automatically when creating a "maze" object """
    def __init__(self):
        """ When the object is instanciated, the variable "Macgyver" is automatically """
        """ triggered, and its value is None """
        self.mac_gyver = None
        """ When the object is instanciated, the "parse_file" method is automatically """
        """ triggered, and its contents are inserted into a self.labyrinth attribute """
        self.labyrinthe = self.parse_file()
        """ When the object is instanciated, the "get_items" method is automatically """
        """ triggered, and its content is inserted into a "self.get_objects" attribute. """
        self.get_objects = self.get_items()
        """ We would instanait the counter of the backpack from Macgyver to 0, it must pick up 3 objects """
        self.macc_gyver_bag = 0


    """ Method that manages the parsing of the .txt file representing the maze """
    def parse_file(self):

        """ The variables/tables needed for the method are created """
        content = {}
        coo_x, coo_y = 0, 0

        """ We open the file in playback and assign its contents to "f" """
        spider = open("labyrinthe.txt", "r")

        """ We walk the lines of "f" """
        for line in spider:
            """ We're going through the characters of "line" """
            for caracter in line:
                """ If the character is a 'd' then create the pair of keys 'MacGyver' """
                if caracter == 'd':
                    self.mac_gyver = MacGyver([coo_x, coo_y])
                """ If the character is a 'back to the line' """    
                if caracter == "\n":
                    """ we iron y to 0, and x to x+1 """
                    coo_y = 0
                    coo_x = x+1
                    """Otherwise the character is not a back to the line"""
                else:
                    """We create the pair key: value in the dictionary content"""
                    content[(coo_x, coo_y)] = caracter
                    coo_y = coo_y+1
        return content


    """ Create a method that recovers all the "keys" of the "self.labyrinthe" attribute whose value is "c" (for way!) """
    def get_keys(self):
        liste = []
        for key, value in self.labyrinthe.items():
            if value == 'c':
                liste.append(key)
        return liste

    """ This function randomly selects 3 coordinated """
    def random_coordinates(self):
        import random
        i = 0
        liste = self.get_keys()
        liste_coordinates = []
        """ We run three he's function """ 
        for i in range(0,3):
            random.shuffle(liste)
            liste_coordinates.append(liste[0])
            liste.pop(0)
        return liste_coordinates

    """ Then, use this method to recover 3 coordinates randomly, in order to place our 3 objects (tube, ether, syringe) """
    def get_items(self):
        liste = self.random_coordinates()
        self.labyrinthe[(tuple(liste[0]))] = 't'
        self.labyrinthe[(tuple(liste[1]))] = 's'
        self.labyrinthe[(tuple(liste[2]))] = 'e'
        return liste

    """ The different travel functions of Mac_gyver """
    def bottom(self):
        m.move("bottom")

    def top(self):
        m.move("top")

    def left(self):
        m.move("left")

    def right(self):
        m.move("right")

    """ The fontion check_move that verifies whether the move is allowed and whether they can pick up an object or not """
    def check_move(self, direction = False):

        destination = None
        
        if direction == "bottom":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0] + 1, self.mac_gyver.coordinates[1])] 
        
        if direction == "top":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0] -1, self.mac_gyver.coordinates[1])] 
        
        if direction == "left":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0], self.mac_gyver.coordinates[1] - 1)]
        
        if direction == "right":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0], self.mac_gyver.coordinates[1] + 1)]

        if destination == "m":
            return False
        
        if destination == "c":
            return True
        
        if destination == 't':
            self.macc_gyver_bag += 1
            print("Vous avez : {} objet .".format(self.mac_gyver.bag))
            return True
            
        if destination == 's':
            self.macc_gyver_bag += 1
            print("Vous avez : {} objet .".format(self.mac_gyver.bag))
            return True
            
        if destination == 'e':
            self.macc_gyver_bag += 1
            print("Vous avez : {} objet .".format(self.mac_gyver.bag))
            return True
        
        if destination == "g":
            if self.macc_gyver_bag == 3:
                print(" Vous avez gagnez !!!! .")
                return True
            else:
                print(" Vous avez perdu !!!! .")

    """ This function draws function (self.labyrinth), 15 lines in height and width """
    def parse_laby(self):
        line = ""
        cpt = 0
        for key, value in self.labyrinthe.items():
            if value == "m":
                line += "#"
            if value == "c":
                line += " "
            if value == "t":
                line += "T"
            if value == "s":
                line += "S"
            if value == "e":
                line += "E"
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

    def picture_maze(self, fenetre):
        """ How to view the level based 
        of the structure list referred by generer ()
        Chargement images (only the arrival one contains transparency """

        mur = pygame.image.load(image_Mur).convert()
        Mac_gyverr = pygame.image.load(image_Mac__gyver).convert_alpha()
        Guard = pygame.image.load(image_Guard).convert_alpha()
        Seringue = pygame.image.load(image_seringue).convert_alpha()
        Ether = pygame.image.load(image_ether).convert_alpha()
        Aiguille = pygame.image.load(image_aiguille).convert_alpha()
        
        for key, value in self.labyrinthe.items():
            x = key[0] * taille_sprite
            y = key[1] * taille_sprite

            if value == 'd':
                fenetre.blit(Mac_gyverr, (x,y))
            if value == 'm':
                fenetre.blit(mur, (x,y))
            if value == 'g':
                fenetre.blit(Guard, (x,y))
            if value == 's':
                fenetre.blit(Seringue, (x,y))
            if value == 'e':
                fenetre.blit(Ether, (x,y))
            if value == 't':
                fenetre.blit(Aiguille, (x,y))

    """ This function recovers Macgyver's various movements. """
    def move(self, direction = False):
        if direction == "bottom":
            if self.check_move(direction):
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                self.mac_gyver.coordinates[0] += 1
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

        if direction == "top":
            if self.check_move(direction):
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c" 
                self.mac_gyver.coordinates[0] -= 1
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

        if direction == "left":
            if self.check_move(direction):
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                self.mac_gyver.coordinates[1] -= 1
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

        if direction == "right":
            if self.check_move(direction):
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "c"
                self.mac_gyver.coordinates[1] += 1
                self.labyrinthe[tuple(self.mac_gyver.coordinates)] = "d"

if __name__ == '__main__':

    pass