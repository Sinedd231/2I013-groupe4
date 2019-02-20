'''
Created on 18 févr. 2019

@author: Denis
'''
from utiles import formules as fm


class GoToGoalController:
    
    def __init__(self, superviseur):
        """ce controlleur cherchera a aller vers l'objectif quoi qu'il arrive
        arguments : un superviseur
        """
        self.superviseur = superviseur
        self.chemin_vers_goal = [0, 0]  # on initialise le vecteur objectif au hasard, il sera correctement mis a jour par la suite
        self.instanciation = True  # facon pas tres propre d'empecher la rotation du robot a chaque tour: si instanciation vaut true, 
                                # alors il y aura rotation au prochain tour
    
    def calcul_chemin(self):
        
        c = self.superviseur.goal.centre()
        u = c[0] - self.superviseur.robot.x
        v = c[1] - self.superviseur.robot.y
        
        return u, v
    
    # pour mettre a jour le vecteur objectif
    def set_chemin(self):
        self.chemin_vers_goal = self.calcul_chemin() 
    
    # fonction de rotation du robot
    def tourner_vers_goal(self):
        
        self.superviseur.tourner_degree(fm.convertir_radians_degree(fm.convertir_direction_angle(self.chemin_vers_goal[0], self.chemin_vers_goal[1])))
        
    def execute(self):
        
        if self.instanciation:  # on effectue donc une rotation une premiere fois, puis plus jamais comme on met instanciation a false
            self.set_chemin()
            self.tourner_vers_goal()
            self.instanciation = False
            
        self.superviseur.avancer()  # apres la rotation, ce controlleur ne fait rien d'autre qu'avancer
    