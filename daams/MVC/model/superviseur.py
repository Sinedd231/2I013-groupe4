'''
Created on 14 fevr. 2019

@author: Denis
'''

from MVC.controller.strategies import StrategieInterface, GoalStrat, SquareStrat

class Superviseur:
    
    def __init__(self, robot):
        """le superviseur sert d'intermediaire entre les controlleurs et le robot
        le superviseur choisira une strategie parmie toutes celles disponibles
        il traduira aussi les commandes pour le robot
        arguments : un robot
        """
        self.robot = robot;
        self.goal = None  # Chaque superviseur aura acces a l'objectif de world, on initialise a None puis on le mettra a jour plus tard
        self.interface= StrategieInterface(self)
        
        #on prepare toutes les "grosses" strategies
        self.goalstrat= GoalStrat(self)
        self.squarestrat= SquareStrat(self)
           
    def step(self,dt):
        v, omega = self.interface.get_command(self.squarestrat)
        self.translate_command(v, omega)
        self.robot.step(dt)

    
    def translate_command(self,v,omega):
        
        v_droite, v_gauche = self.calcul_dps(v, omega)
        self.robot.set_dps(v_droite, v_gauche)
        
    def calcul_dps(self,v ,omega):
        
        v_droite = ((2*v)+(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        v_gauche = ((2*v)-(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        
        return v_droite, v_gauche
    
    def define_goal(self,goal):
        
        self.goal = goal
    