'''
Created on 14 févr. 2019

@author: Denis
'''

from MVC.controller.strategie import Strategie

class Superviseur:
    
    def __init__(self, robot):
        """le superviseur sert d'intermediaire entre les controlleurs et le robot
        le superviseur choisira une strategie parmie toutes celles disponibles
        il traduira aussi les commandes pour le robot
        arguments : un robot
        """
        self.robot = robot;
        self.goal = None  # Chaque superviseur aura acces a l'objectif de world, on initialise a None puis on le mettra a jour plus tard
        self.strategie= Strategie(self) #la classe strategie qui regroupera toutes les strategies realisables par le robot
        
        #commandes haut niveau, que le superviseur traduira en vitesse roue droite-gauche
        self.v=0
        self.omega=0
           
    def step(self,dt):
        self.strategie.dessiner_carre()  #c'est cette ligne la qu'il faudra modifier, selon la strategie voulue
        self.translate_command()
        self.robot.step(dt)

    
    def translate_command(self):
        
        v_droite, v_gauche = self.calcul_dps(self.v, self.omega)
        self.robot.set_dps(v_droite, v_gauche)
        
    def calcul_dps(self,v ,omega):
        
        v_droite = ((2*v)+(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        v_gauche = ((2*v)-(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        
        return v_droite, v_gauche
    
    def define_goal(self,goal):
        
        self.goal = goal
    