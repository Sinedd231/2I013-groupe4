'''
Created on 14 fevr. 2019

@author: Denis
'''
from MVC.utiles import geometrie as geo
from MVC.exceptions.collision_exception import CollisionException
from MVC.exceptions.objectif_atteint_exception import ObjectifException

class World:
    
    def __init__(self):
        """les elements de la simulation seront tous presents ici
        """
        self.world_temps = 0.0
        self.dt = 0.02 # a changer selon la vitesse de la simulation voulue
        
        self.robots = []
        self.obstacles = []
        self.capteurs = []
        self.goal = None
    
    # on effectue un tour de simulation, dans le lequel on met a jour les coordonnees des objets mobiles
    #et ou on verifie les collisions
    def update(self):
        
        for robot in self.robots:
            robot.update_coords_dir()
            robot.update_coords_capteur()
            self.check_collisions(robot)

        self.world_temps += self.dt
    
    def add_robot(self, robot):
        
        self.robots.append(robot)
        self.capteurs.append(robot.capteur)
    
    def add_obstacle(self, obstacle):
        
        self.obstacles.append(obstacle)
    
    # les espace reserves sont les zones ou on veut pas d'obstacle, donc typiquement la zone du robot et de l'objectif
    def espace_reserve(self):
        """retourne un tableau"""
        return self.robots + [self.goal] 
    
    # les solides sont les elements susceptibles de se cogner, on ne met pas l'objectif ici pour ne pas renvoyer la meme
    # exception
    
    def solides(self):
        """retourne un tableau"""
        return self.robots + self.obstacles
    
    def define_goal(self, goal):
        self.goal = goal
        
    
    def check_collisions(self, robot):
        
        # on teste si on a atteint l'objectif
        if geo.check_proximite(robot, self.goal):
            if geo.intersection_polygones(robot, self.goal):
                raise ObjectifException()
        
        # on traite le signal du capteur si il y en a
        if robot.capteur.detect_solides(self): 
            print("Attention obstacle !")  # on pourra trouver d'autre taches qu'un simple affichage
        
        # on teste si le robot a heurte un solide
        for elem in self.solides():
            
            if elem is not robot:  # on ne teste pas le robot contre lui meme
                
                if geo.check_proximite(elem, robot):  # on regarde si les elements sont suffisemment proches pour justifier un test
                    
                    if geo.intersection_polygones(elem, robot):  # le test en lui meme
                        raise CollisionException()
    
