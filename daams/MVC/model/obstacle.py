'''
Created on 14 fevr. 2019

@author: Denis
'''

from .abstract_polygone import Polygone


class Obstacle(Polygone):
    # l'obstacle sera represente par un rectangle
    
    def __init__(self, x, y, largeur, hauteur):
        
        self.x = x  # coordonnees
        self.y = y  # absolues
        self.largeur = largeur
        self.hauteur = hauteur
        self.x1 = self.x + self.largeur  # x du point en bas a droite
        self.y1 = self.y + self.hauteur  # y du point en bas a droite
    
    def getVecteurs(self):
        
        return [    [self.x, self.y],
                    [self.x1, self.y],
                    [self.x1, self.y1],
                    [self.x, self.y1]   ]    
    
    def nbrCotes(self):
        return 4  # parce que rectangle
    
    def getCotes(self):
        return super(Obstacle, self).getCotes()
