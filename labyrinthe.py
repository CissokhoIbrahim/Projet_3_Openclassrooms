#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""the modules for importation"""

import pygame
from macgyver import MacGyver
import constante


class Maze:
    """Builder: triggers
    automatically when creating a "maze" object"""
    def __init__(self):
        """When the object is instanciated,the variable "Macgyver" is automatically"""

        self.mac_gyver = None
        """triggered, and its value is None, when the object is instanciated,
        the "parse_file" method is automatically
        triggered, and its contents are inserted into a self.labyrinth attribute"""

        self.labyrinthe = self.parse_file()
        """When the object is instanciated, the get_items method is automatically
        triggered, and its content is inserted into a self.get_objects attribute"""

        self.get_objects = self.get_items()
        """We would instanait the counter of
        the backpack from Macgyver to 0, it must pick up 3 objects"""

        self.bag = 0

    def parse_file(self):
        """Method that manages the parsing of
        the .txt file representing the maze"""

        content = {}
        coo_x, coo_y = 0, 0

        spider = open("labyrinthe.txt", "r")
        """We open the file in playback and assign its contents to spider"""

        for line in spider:
            """We walk the lines of spider"""

            for caracter in line:
                """We're going through the characters of line"""

                if caracter == 'd':
                    """If the character is a d then create the pair of keys MacGyver"""
                    self.mac_gyver = MacGyver([coo_x, coo_y])
                    """If the character is a back to the line"""
                if caracter == "\n":
                    """ we iron y to 0, and x to x+1 """
                    coo_y = 0
                    coo_x = coo_x+1
                    """Otherwise the character is not a back to the line"""
                else:
                    """We create the pair key: value in the dictionary content"""
                    content[(coo_x, coo_y)] = caracter
                    coo_y = coo_y+1
        return content


    def get_keys(self):
        """ Create a method that recovers
        all the "keys" of the self.labyrinthe
        attribute whose value is c (for way!) """
        liste = []
        for key, value in self.labyrinthe.items():
            if value == 'c':
                liste.append(key)
        return liste

    def random_coordinates(self):
        """ This function randomly
        selects 3 coordinated """
        import random
        i = 0
        liste = self.get_keys()
        liste_coordinates = []
        for i in range(0,3):
            """ We run three he's function """
            random.shuffle(liste)
            liste_coordinates.append(liste[0])
            liste.pop(0)
        return liste_coordinates

    def get_items(self):
        """ Then, use this method to recover
        3 coordinates randomly, in order to place our
        3 objects (tube, ether, syringe) """
        liste = self.random_coordinates()
        self.labyrinthe[(tuple(liste[0]))] = 't'
        self.labyrinthe[(tuple(liste[1]))] = 's'
        self.labyrinthe[(tuple(liste[2]))] = 'e'
        return liste

    def bottom(self):
        m.move("bottom")

    def top(self):
        m.move("top")

    def left(self):
        m.move("left")

    def right(self):
        m.move("right")


    def check_move(self, direction):
        """ The fontion check_move that verifies
        whether the move is allowed and whether
        they can pick up an object or not """

        destination = None

        if direction == "bottom":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0] + 1,
            self.mac_gyver.coordinates[1])]

        if direction == "top":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0] -1,
            self.mac_gyver.coordinates[1])]

        if direction == "left":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0],
            self.mac_gyver.coordinates[1] - 1)]

        if direction == "right":
            destination = self.labyrinthe[(self.mac_gyver.coordinates[0],
            self.mac_gyver.coordinates[1] + 1)]

        if destination == "m":
            return False

        if destination == "c":
            return True

        if destination == 't':
            self.bag += 1
            print("Vous avez : {} objet .".format(self.bag))
            return True

        if destination == 's':
            self.bag += 1
            print("Vous avez : {} objet .".format(self.bag))
            return True

        if destination == 'e':
            self.bag += 1
            print("Vous avez : {} objet .".format(self.bag))
            return True

        if destination == "g":
            if self.bag == 3:
                print(" Vous avez gagnez !!!! .")
                return True
            else:
                print(" Vous avez perdu !!!! .")
                return True

    def parse_laby(self):
        """ This function draws function
        (self.labyrinth), 15 lines in height and width """
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
        """How to view the level based
        of the structure list referred by generer
        Chargement images only the arrival one contains transparency"""
        MUR = pygame.image.load(IMAGE_MUR).convert_alpha()
        MACGYVER = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
        GUARD = pygame.image.load(IMAGE_GUARD).convert_alpha()
        SERINGUE = pygame.image.load(IMAGE_SERINGUE).convert_alpha()
        ETHER = pygame.image.load(IMAGE_ETHER).convert_alpha()
        AIGUILLE = pygame.image.load(IMAGE_AIGUILLE).convert_alpha()

        for key, value in self.labyrinthe.items():
            case_x = key[0] * TAILLE_SPRITE
            case_y = key[1] * TAILLE_SPRITE

            if value == 'd':
                fenetre.blit(MACGYVER, (case_x,case_y))
            if value == 'm':
                fenetre.blit(MUR, (case_x,case_y))
            if value == 'g':
                fenetre.blit(GUARD, (case_x,case_y))
            if value == 's':
                fenetre.blit(SERINGUE, (case_x,case_y))
            if value == 'e':
                fenetre.blit(ETHER, (case_x,case_y))
            if value == 't':
                fenetre.blit(AIGUILLE, (case_x,case_y))


    def move(self, direction):
        """ This function recovers
        Macgyver's various movements."""
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
