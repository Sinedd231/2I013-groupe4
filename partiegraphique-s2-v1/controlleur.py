'''
Created on 2 fevr. 2019

@author: Denis
'''
from Robot import *
from tourner import *
from math import *

class Controlleur:
    """le controlleur prendra en variable un robot, qu'il controlera"""
    
    def __init__(self, robot):
        self.robot= robot
    
    def update_coords_dir(self):
        """permet de mettre a jour les coordonnees du robot suite a un changement de direction"""
        
        self.robot.centregravite = centregravite(self.robot.A, self.robot.B, self.robot.C)
        self.robot.A= tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], atan2( self.robot.direction[0], self.robot.direction[1] ), self.robot.A)
        self.robot.B= tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], atan2( self.robot.direction[0], self.robot.direction[1] ), self.robot.B)
        self.robot.C= tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], atan2( self.robot.direction[0], self.robot.direction[1] ), self.robot.C)
        #on fait donc la rotation des 3 points autour du centre de gravite