'''
Created on 14 févr. 2019

@author: Denis
'''
import formules as fm
import random
from view.viewer import HAUTEUR, LARGEUR

class Superviseur:
    
    def __init__(self,robot):
        
        self.robot=robot;
        self.goal = ( random.uniform(0,LARGEUR),random.uniform(0,HAUTEUR) )
    
    
    def tourner_radiant (self,angle):
        """
        la fonction prend un objet de la classe robot et un angle en radiant
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        self.robot.direction = fm.rotation_vecteur(self.robot.direction, angle)
        
        
    def tourner_degree (self,angle):
        """
        la fonction prend un objet de la classe robot et un angle en degree
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        self.robot.direction = fm.rotation_degree(self.robot.direction, angle)
        