'''
Created on 18 fevr. 2019

@author: Denis
'''

from MVC.view.viewer import Viewer
from MVC.model.world import World
from MVC.model.robotsim import Robotsim
from MVC.view.world_view import WorldView
from MVC.model.map_builder import MapBuilder
from MVC.exceptions.collision_exception import CollisionException
from MVC.exceptions.objectif_atteint_exception import ObjectifException
from MVC.model.superviseur import Superviseur
import time


class Simulateur:
    
    def __init__(self):
        
        self.viewer = Viewer(self)
        self.robot = Robotsim(450, 450, "astroboy", "blue") #on creer notre robot
        self.superviseur = Superviseur(self.robot)  #on creer son superviseur
                                                    #NOTE: on doit creer un superviseur pour chaque robot
                                                    #si il ya plusieurs robots, on devra sans doute passer par des tableaux
        self.init_sim()
    
    def init_sim(self):
        
        self.world = World()
        self.world.add_robot(self.robot)
        
        self.map_builder = MapBuilder()
        self.map_builder.build_random(self.world)
        self.superviseur.define_goal(self.world.goal)   #on donne l'objectif au superviseur, sinon on perd des strategies
                                                        #on passe par une fonction au lieu du simple affectation pour faciliter le cas
                                                        #ou on a plusieurs superviseurs
        
        self.worldview = WorldView(self.world, self.viewer)
        
        self.worldview.draw_world() #ligne a commenter si on veut debrancher l'affichage

    def run_sim(self):
            
        while True:
            try:
                self.superviseur.step(self.world.dt)
                self.world.update()
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
    
