'''
Created on 5 mars 2019

@author: Denis
'''

from MVC.controller.controlleurs import GoToGoalControlleur, MoveForwardControlleur, TurnControlleur
from MVC.view.viewer import HAUTEUR, LARGEUR
from MVC.model.world import DT

""" les strategies prennent tous un superviseur en argument pour pouvoir voir
le robot. On joue avec les controlleurs et selon la strategie, on essaie d'en 
tirer une certaine vitesse et vitesse angulaire qu'on transmettra au superviseur
"""

class LigneStrat():
    """cette strategie consiste a faire avancer le robot en ligne droite
    sur une certaine distance donnee en parametre
    """
    
    def __init__(self,superviseur,distancemax):
        
        self.superviseur=superviseur
        self.distance=0
        self.distancemax=distancemax
        self.controlleur=MoveForwardControlleur(self.superviseur)
        
    def get_command(self):
        
        #tests sur les bords de la fenetre de la simulation
        
        if (self.superviseur.robot.A[0] >= LARGEUR or self.superviseur.robot.A[0] <= 0
        or self.superviseur.robot.A[1] <= 0 or self.superviseur.robot.A[1] >= HAUTEUR):
            return 0,0
        
        #si on a pas atteint la distance fixee
        if (self.distance < self.distancemax):
            v, omega= self.controlleur.execute()
            self.distance += v*DT   #on va faire une simplication et utiliser cette formule meme
                                    #si ca sera sans doute pas ca dans le monde reel
            return v, omega
        else:
            #sinon, on ne veut plus que le robot bouge
            return 0,0


class GoalStrat():
    """on se dirige vers l'objectif donne en parametre, quoi qu'il arrive
    """
    
    def __init__(self,superviseur,goal):
        
        self.superviseur=superviseur
        self.goal=goal
        self.controlleur= GoToGoalControlleur(self.superviseur, self.goal)
        
    def get_command(self):
         
        return self.controlleur.execute()
        
        
class Turn90Strat():
    """on tourne de 90 degrees
    """
    
    def __init__(self,superviseur):
        
        self.superviseur=superviseur
        self.controlleur=TurnControlleur(self.superviseur,90)
    
    def get_command(self):
        
        v, omega= self.controlleur.execute()
        
        #on n'atteindra jamais l'angle exacte voulue, on fixe donc
        #la precision arbitrairement a 0.1
        
        if (abs(omega)<0.1):
            #si le robot tourne a une vitesse inferieure a cette precision, on
            #estime qu'on a fini la rotation
            return 0,0
        else:
            return v,omega


class SquareStrat():
    """on fait dessiner un carre au robot
    """
    
    def __init__(self,superviseur):
        
        self.superviseur= superviseur
        
        #on a besoin de sous strategies ici
        self.strat_avancer = LigneStrat(self.superviseur,500)
        self.strat_tourner= Turn90Strat(self.superviseur)
        
    def get_command(self):
        #on fait alterner les sous strategies et on 
        #base notre raisonnement sur leurs reponses respectives,
        #si une sous strategie renvoie 0,0 on passe a la sous strategie
        #suivante
        
        v_avancer, omega_avancer = self.strat_avancer.get_command()
            
        if (v_avancer==0 and omega_avancer==0):
            v_tourner, omega_tourner = self.strat_tourner.get_command()
            
            if (v_tourner==0 and omega_tourner==0):
                self.strat_avancer=LigneStrat(self.superviseur,500)
                
            return v_tourner, omega_tourner
            
        else:
            #on actualise le vecteur rotation au cas ou on commencerait la
            #rotation le prochain tour
            
            self.strat_tourner=Turn90Strat(self.superviseur)
              
        return v_avancer,omega_avancer
            