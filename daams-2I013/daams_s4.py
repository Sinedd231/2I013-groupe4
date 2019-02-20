'''
Created on 18 févr. 2019

@author: Denis
'''

from view.viewer import Viewer
from model.world import World
from model.robot import Robot
from view.world_view import WorldView
from model.map_builder import MapBuilder
from exceptions.collision_exception import CollisionException
from exceptions.objectif_atteint_exception import ObjectifException
import time


class Simulateur:
    
    def __init__(self):
        
        self.viewer = Viewer(self)
        self.init_sim()
    
    def init_sim(self):
        
        self.world = World()
        robot = Robot(450, 450, "astroboy", "blue")
        self.world.add_robot(robot)
        
        self.map_builder = MapBuilder()
        self.map_builder.build_random(self.world)
        
        self.worldview = WorldView(self.world, self.viewer)
        
        self.worldview.draw_world()

    def run_sim(self):
            
        while True:
            try:
                self.world.step()
            except CollisionException:
                print("Collision !")
                break
            except ObjectifException:
                print("Objectif atteint !")
                break
        
            self.worldview.update_world()
            time.sleep(self.world.dt)
    
    
if __name__ == '__main__':
    
    sim = Simulateur()
    
    sim.run_sim()
    
    print("la simulation a dure %d tours" % (sim.world.world_temps / sim.world.dt))
        
    sim.worldview.viewer.fenetre.mainloop()
    
