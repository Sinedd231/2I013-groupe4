'''
Created on 14 févr. 2019

@author: Denis
'''

from math import sqrt
import random
from view.viewer import HAUTEUR

class Obstacle:
    
    def __init__(self):
        
        self.x = random.uniform(*random.choice( [(0,310),(430,HAUTEUR) ] ) )
        self.y = random.uniform(0,HAUTEUR)
        self.largeur = random.uniform(15,50)
        self.hauteur = random.uniform(15,50)
        self.init_coords()
        
    
    def init_coords(self):
        """ sur tkinter il faut 2 points pour dessiner un rectangle
            le coin en haut a gauche, donc xy chez nous, et le coin en bas a droite
            on doit donc determiner les coordonnees de ce coin
        """
        
        self.x1 = self.x+ sqrt(self.largeur**2 + self.hauteur**2)    #longueur de la diagonale = racine de (hauteur^2 + largeur^2)
        self.y1 = self.y+ self.hauteur