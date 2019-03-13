'''
Created on 18 fevr. 2019

@author: Denis
'''
from MVC.utiles import formules as fm


class GoToGoalControlleur:
    
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
        omega=angle*10 
        
        return self.superviseur.robot.vmax/(abs(omega) + 1)**0.5, omega    #on fait diminuer la vitesse quand le robot est en rotation
                                                                        #avec cette formule, v se rapproche rapidement de 0 quand omega augmente
                                                                        #de cette maniere on se ramene a un comportement alternant move forward - turn 9 


class MoveForwardControlleur:
    
    def __init__(self,superviseur):
        """ce controlleur fera avancer le robot a sa vitesse maximale
        arguments : un superviseur
        """
        self.superviseur = superviseur
    
    
    def execute(self):
        
        return self.superviseur.robot.vmax, 0
    
    
class Turn90Controlleur:
    
    def __init__(self,superviseur):
        """ce controlleur fera tourner le robot de 90 degrees
        arguments : un superviseur
        """
        
        self.superviseur=superviseur
        self.chemin_vers_goal =  fm.rotation_degree(self.superviseur.robot.direction, 90) #on doit calculer le vecteur rotation qu'une seule fois
    
    
    def execute(self):
        
        angle=fm.convertir_direction_angle(self.chemin_vers_goal[0], self.chemin_vers_goal[1])-fm.convertir_direction_angle(self.superviseur.robot.direction[0], self.superviseur.robot.direction[1])
                
        return 0, angle*10
    