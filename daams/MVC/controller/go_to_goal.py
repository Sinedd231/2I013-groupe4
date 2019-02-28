'''
Created on 18 févr. 2019

@author: Denis
'''
from MVC.utiles import formules as fm


class GoToGoalController:
    
    def __init__(self, superviseur):
        """ce controlleur cherchera a aller vers l'objectif quoi qu'il arrive
        arguments : un superviseur
        """
        self.superviseur = superviseur
        self.chemin_vers_goal = [0, 0]  # on initialise le vecteur objectif au hasard, il sera correctement mis a jour par la suite
        
    def calcul_chemin(self):
        
        c = self.superviseur.goal.centre()
        u = c[0] - self.superviseur.robot.x
        v = c[1] - self.superviseur.robot.y
        
        return [u, v]
    
    # pour mettre a jour le vecteur objectif
    def set_chemin(self):
        
        self.chemin_vers_goal = self.calcul_chemin() 
    
    def execute(self):
        
        self.set_chemin()
        angle=fm.convertir_direction_angle(self.chemin_vers_goal[0], self.chemin_vers_goal[1])-fm.convertir_direction_angle(self.superviseur.robot.direction[0], self.superviseur.robot.direction[1])
        v=500 #m/s
        
        self.superviseur.v=v
        self.superviseur.omega=angle/0.1 #rad/s
    