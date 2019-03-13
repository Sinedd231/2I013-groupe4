'''
Created on 5 mars 2019

@author: Denis
'''

from MVC.controller.controlleurs import GoToGoalControlleur, MoveForwardControlleur, Turn90Controlleur
from MVC.view.viewer import HAUTEUR, LARGEUR
from MVC.model.world import DT

class StrategieInterface:
    
    def __init__(self,superviseur):
        
        self.superviseur= superviseur
        
    def get_command(self,strategie):
        return strategie.get_command()
    

class LigneStrat():
    
    def __init__(self,superviseur,distancemax):
        
        self.superviseur=superviseur
        self.distance=0
        self.distancemax=distancemax
        self.controlleur=MoveForwardControlleur(self.superviseur)
        
    def get_command(self):
        
        if (self.superviseur.robot.A[0] >= LARGEUR or self.superviseur.robot.A[0] <= 0
        or self.superviseur.robot.A[1] <= 0 or self.superviseur.robot.A[1] >= HAUTEUR):
            return 0,0
        
        if (self.distance < self.distancemax):
            v, omega= self.controlleur.execute()
            self.distance += v*DT   #on va faire une simplication et utiliser cette formule meme
                                    #si ca sera sans doute pas ca dans le monde reel
            return v, omega
        else:
            return 0,0


class GoalStrat():
    
    def __init__(self,superviseur):
        
        self.superviseur=superviseur
        self.controlleur= GoToGoalControlleur(self.superviseur)
        
    def get_command(self):
         
        return self.controlleur.execute()


class Turn90Strat():
    
    def __init__(self,superviseur):
        
        self.superviseur=superviseur
        self.controlleur=Turn90Controlleur(self.superviseur)
    
    def get_command(self):
        
        v, omega= self.controlleur.execute()
        
        if (abs(omega)<0.1):
            return 0,0
        else:
            return v,omega


class SquareStrat():
    
    def __init__(self,superviseur):
        
        self.superviseur= superviseur
        self.strat_avancer = LigneStrat(self.superviseur,500)
        self.strat_tourner= Turn90Strat(self.superviseur)
        
    def get_command(self):
        
        v_avancer, omega_avancer = self.strat_avancer.get_command()
            
        if (v_avancer==0 and omega_avancer==0):
            v_tourner, omega_tourner = self.strat_tourner.get_command()
            
            if (v_tourner==0 and omega_tourner==0):
                self.strat_avancer=LigneStrat(self.superviseur,500)
                
            return v_tourner, omega_tourner
            
        else:
            self.strat_tourner=Turn90Strat(self.superviseur)
              
        return v_avancer,omega_avancer
            