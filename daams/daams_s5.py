'''
Created on 18 févr. 2019

@author: Denis
'''

from MVC.view.viewer import Viewer
from MVC.model.world import World
from MVC.model.robotsim import Robotsim
from MVC.view.world_view import WorldView
from MVC.model.map_builder import MapBuilder
from MVC.exceptions.collision_exception import CollisionException
from MVC.exceptions.objectif_atteint_exception import ObjectifException
import time


class Simulateur:
    
    def __init__(self):
        
        self.viewer = Viewer(self)
        self.init_sim()
    
    def init_sim(self):
        
        self.world = World()
        robot = Robotsim(450, 450, "astroboy", "blue")
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
    
