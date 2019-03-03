'''
Created on 3 mars 2019

@author: Denis
'''

class MoveForwardControlleur:
    
    def __init__(self,superviseur):
        """ce controlleur fera avancer le robot a sa vitesse maximale
        arguments : un superviseur
        """
        self.superviseur = superviseur
    
    
    def execute(self):
        
        self.superviseur.v=self.superviseur.robot.vmax
        self.superviseur.omega=0