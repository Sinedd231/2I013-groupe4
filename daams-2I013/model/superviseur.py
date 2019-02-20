'''
Created on 14 févr. 2019

@author: Denis
'''

from controller.go_to_goal import GoToGoalController
from utiles import geometrie as geo
from utiles import formules as fm
from exceptions.objectif_atteint_exception import ObjectifException
from exceptions.collision_exception import CollisionException


class Superviseur:
    
    def __init__(self, robot):
        """le superviseur sert d'intermediaire entre les controlleurs et le robot
        arguments : un robot
        """
        self.robot = robot;
        self.goal = None  # Chaque superviseur aura un objectif a atteindre, on initialise a None puis on le mettra a jour plus tard
        self.controlleuractuel = GoToGoalController(self)  # tous les superviseurs commencent avec go to goal
        
    def tourner_degree (self, angle):
        """
        la fonction prend un objet de la classe robot et un angle en degree
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        self.robot.direction = fm.rotation_degree(self.robot.direction, angle)
    
    def avancer(self):
        dx = fm.cos(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))  # on calcule d'abord le deplacement relatif du robot dx dy
        dy = fm.sin(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))  # EN FONCTION DE SA DIRECTION
            
        self.robot.x += dx  # puis on incremente x et y
        self.robot.y += dy
        
        self.robot.update_coords_dir()  # on met a jours les points relatifs du robot
        self.robot.update_coords_capteur()  # on met a jours les points relatifs du capteur
    
    def change_controlleur(self, controlleur):
        self.controlleuractuel = controlleur
    
    def step(self, world):
        self.controlleuractuel.execute()
        self.check_collisions(world)
    
    def check_collisions(self, world):
        
        # on teste si on a atteint l'objectif
        if geo.check_proximite(self.robot, self.goal):
            if geo.intersection_polygones(self.robot, self.goal):
                raise ObjectifException()
        
        # on traite le signal du capteur si il y en a
        if self.robot.capteur.detect_solides(world): 
            print("Attention obstacle !")  # on pourra trouver d'autre taches qu'un simple affichage
        
        # on teste si le robot a heurte un solide
        for elem in world.solides():
            
            if elem is not self.robot:  # on ne teste pas le robot contre lui meme
                
                if geo.check_proximite(elem, self.robot):  # on regarde si les elements sont suffisemment proches pour justifier un test
                    
                    if geo.intersection_polygones(elem, self.robot):  # le test en lui meme
                        raise CollisionException()
    
