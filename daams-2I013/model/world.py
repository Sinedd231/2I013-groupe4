'''
Created on 14 févr. 2019

@author: Denis
'''

class World:
    
    def __init__(self):
        
        self.world_temps=0.0
        self.dt = 0.01
        
        self.robots= []
        self.obstacles= []
        self.capteurs= []
        self.superviseurs=[]
    
    
    def step(self):
        
        for robot in self.robots:
            
            robot.capteur.work()
        
        for superviseur in self.superviseurs:
            
            superviseur.step()
        
        self.world_temps += self.dt
    
    
    def add_robot(self,robot):
        
        self.robots.append(robot)
        self.capteurs.append(robot.capteur)
        self.superviseurs.append(robot.superviseur)
    
    def add_obstacle(self,obstacle):
        
        self.obstacles.append(obstacle)
    
    def elem_collision(self):
        
        return self.robots + self.obstacles
    