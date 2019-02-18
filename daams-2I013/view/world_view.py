'''
Created on 18 févr. 2019

@author: Denis
'''
from model.robot import *
from model.obstacle import *

class WorldView():
    
    def __init__(self, world, viewer):
        
        self.viewer = viewer;
        
        self.robots= []
        for robot in world.robots:
            self.robots.append(robot)
        
        self.obstacles=[]
        for obstacle in world.obstacles:
            self.obstacles.append(obstacle)
            
        self.capteurs=[]
        for capteur in world.capteurs:
            self.capteurs.append(capteur)
        
    
    def draw_robots(self):
        
        for robot in self.robots:
            self.viewer.fenetre.create_polygon(robot.A, robot.B, robot.C, fill=robot.couleur)
    
    def draw_obstacles(self):
        
        for obstacle in self.obstacles:
            self.viewer.fenetre.create_rectangle(obstacle.x, obstacle.y, obstacle.x1, obstacle.y1, fill='red')
    
    def draw_capteurs(self):
        
        for capteur in self.capteurs:
            self.viewer.fenetre.create_polygon(capteur.A, capteur.B, capteur.C)
    
    def draw_world(self):
        
        self.draw_robots()
        self.draw_obstacles()
        self.draw_capteurs()
        