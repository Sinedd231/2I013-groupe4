'''
Created on 14 févr. 2019

@author: Denis
'''

class World:
    
    def __init__(self):
        """les elements de la simulation seront tous presents ici
        """
        self.world_temps = 0.0
        self.dt = 0.02  # a changer selon la vitesse de la simulation voulue
        
        self.robots = []
        self.obstacles = []
        self.capteurs = []
        self.superviseurs = []
        self.goal = None
    
    # on effectue un tour de simulation, on pourra trouver d'autre chose a faire durant ce tour
    def step(self):
        
        for superviseur in self.superviseurs:
            
            superviseur.step(self)
            print("Le robot %s avance en %d %d" %(superviseur.robot.nom, superviseur.robot.x, superviseur.robot.y))
        
        self.world_temps += self.dt
    
    def add_robot(self, robot):
        
        self.robots.append(robot)
        self.capteurs.append(robot.capteur)
        self.superviseurs.append(robot.superviseur)
    
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
    
