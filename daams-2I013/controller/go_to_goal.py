'''
Created on 18 févr. 2019

@author: Denis
'''
import formules as fm

class GoToGoalController:
    
    def __init__(self, superviseur):
        
        self.superviseur = superviseur
    
    
    def tourner_vers_goal(self):
        
        u = self.superviseur.goal[0] - self.superviseur.robot.x
        v=  self.superviseur.goal[1] - self.superviseur.robot.x
        self.superviseur.tourner_radiant(fm.convertir_direction_angle(u,v))