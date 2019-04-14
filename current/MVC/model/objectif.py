'''
Created on 19 fevr. 2019

@author: Denis
'''
from .abstract_polygone import Polygone


class Objectif(Polygone):
    # l'objectif sera represente par un rectangle
    
    def __init__(self, x, y):
        """L'objectif sera un rectangle, represente sur l'affichage par un cercle
        mais cela marche tres bien avec tkinter
        """
        self.x = x
        self.y = y
        self.x1 = self.x + 30  # largeur et hauteur fixees
        self.y1 = self.y + 30
    
    # calcule le centre du rectangle, qui sera le point vise par le go to goal
    def centre(self):
        return [(self.x + self.x1) / 2, (self.y + self.y1) / 2]
    
    def getVecteurs(self):
        return [    [self.x, self.y],
                    [self.x1, self.y],
                    [self.x1, self.y1],
                    [self.x, self.y1]   ]
        
    def getCotes(self):
        return super().getCotes()
    
    def nbrCotes(self):
        return 4  # parce que rectangle

