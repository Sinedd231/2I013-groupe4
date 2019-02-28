'''
Created on 14 févr. 2019

@author: Denis
'''

from MVC.controller.go_to_goal import GoToGoalController
from MVC.controller.draw_square import DrawSquareController


class Superviseur:
    
    def __init__(self, robot):
        """le superviseur sert d'intermediaire entre les controlleurs et le robot
        arguments : un robot
        """
        self.robot = robot;
        self.goal = None  # Chaque superviseur aura un objectif a atteindre, on initialise a None puis on le mettra a jour plus tard
        self.controlleuractuel = GoToGoalController(self)  # tous les superviseurs commencent avec go to goal
        
    
    def change_controlleur(self, controlleur):
        self.controlleuractuel = controlleur
    
    def step(self):
        self.controlleuractuel.execute()
        self.translate_command()
    
    
    def translate_command(self):
        
        v_droite, v_gauche = self.calcul_dps(self.v, self.omega)
        self.robot.set_dps(v_droite, v_gauche)
        
    def calcul_dps(self,v ,omega):
        
        v_droite = ((2*v)+(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        v_gauche = ((2*v)-(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        
        return v_droite, v_gauche
    