'''
Created on 18 févr. 2019

@author: Denis
'''

from view.viewer import *
from model.world import *
from model.robot import *
from model.obstacle import *
from view.world_view import *

class Simulateur:
    
    def __init__(self):
        
        self.viewer = Viewer(self)
        self.init_sim()
        
    
    def init_sim(self):
        
        self.world= World()
        
        robot = Robot("astroboy", "blue")
        self.world.add_robot(robot)
        
        for i in range(10):
            obstacle = Obstacle()
            self.world.add_obstacle(obstacle)
        
        self.worldview = WorldView(self.world, self.viewer)
        
        self.worldview.draw_world()


if __name__ == '__main__':
    test=Simulateur()
    test.viewer.master.mainloop()