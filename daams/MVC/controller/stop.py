'''
Created on 6 mars 2019

@author: Denis
'''
class StopControlleur:
    
    def __init__(self,superviseur):
        """ce controlleur fera arreter le robot
        arguments : un superviseur
        """
        self.superviseur=superviseur
    
    def execute(self):
        
        self.superviseur.v =0
        self.superviseur.omega=0