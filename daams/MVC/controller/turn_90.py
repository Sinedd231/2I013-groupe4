'''
Created on 3 mars 2019

@author: Denis
'''
from MVC.utiles import formules as fm

class Turn90Controlleur:
    
    def __init__(self,superviseur):
        """ce controlleur fera tourner le robot de 90 degrees
        arguments : un superviseur
        """
        
        self.superviseur=superviseur
        self.chemin_vers_goal =  fm.rotation_degree(self.superviseur.robot.direction, 90) #on doit calculer le vecteur rotation qu'une seule fois
    
    
    def execute(self):
        
        self.superviseur.v=0
        
        angle=fm.convertir_direction_angle(self.chemin_vers_goal[0], self.chemin_vers_goal[1])-fm.convertir_direction_angle(self.superviseur.robot.direction[0], self.superviseur.robot.direction[1])
                
        self.superviseur.omega= angle*10