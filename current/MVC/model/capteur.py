'''
Created on 14 fevr. 2019

@author: Denis
'''
from .abstract_polygone import Polygone
from MVC.utiles import geometrie as geo

class Capteur(Polygone):
    # le capteur sera represente par un triangle
    
    def __init__(self, robot):
        """arguments: un robot sur lequel se fixer
        """
        self.robot = robot;
        self.update_points_triangle()  # pour intialiser les points du triangle
    
    def update_points_triangle(self):
        
        self.direction = (-1 * self.robot.direction[0], -1 * self.robot.direction[1])
        self.A = [ self.robot.A[0], self.robot.A[1] ]
        self.B = [ self.A[0] - 100, self.A[1] + 5 ]
        self.C = [ self.B[0], self.A[1] - 5 ]
    
    def getVecteurs(self):
        return [self.A, self.B, self.C]
    
    def nbrCotes(self):
        return 3
    
    def getCotes(self):
        return super().getCotes()
    
    # detecte si oui ou non le capteur a croise un solide, et envoie un signal
    def detect_solides(self, world):
        
        for elem in world.solides():
            if elem is not self.robot:  # on ne teste pas le robot du capteur
                
                if geo.check_proximite(elem, self):  # on regarde si les elements sont suffisemment proches pour justifier un test
                    
                    if geo.intersection_polygones(elem, self):  # le test en lui meme
                        return True
        return False

