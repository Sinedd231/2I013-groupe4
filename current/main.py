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
from MVC.controller.strategies import GoalStrat, SquareStrat
#from MVC.model.robot2I013.robot2I013 import Robot2I013


class Main:
    
    def __init__(self,robot):
        
        self.robot=robot
        
        if isinstance(self.robot, Robotsim):
            self.init_sim()
        else:
            self.init_reel() #reste a faire
    
    def init_sim(self):
        
        self.viewer = Viewer(self)
        self.world = World()
        self.world.add_robot(self.robot)
        
        self.map_builder = MapBuilder()
        self.map_builder.build_random(self.world)
        
        self.superviseur= Superviseur(self.robot, SquareStrat(self))
        
        #on peut mettre n'importe quel point de la fenetre comme objectif et pas seulement l'objectif de world
        #mais la simulation n'est pas faite pour, on ne traite en tout cas pas ce cas la.
        #mais si vous voulez, mettez self.world.goal en 2e parametre pour viser l'objectif de world, mettez [x,y] pour
        #viser le point x y
        
        self.superviseur.redefine_strat(GoalStrat(self,self.world.goal)) #ligne a commenter si vous voulez dessiner un carre
        
        self.worldview = WorldView(self.world, self.viewer)
        self.worldview.draw_world() #ligne a commenter si vous voulez debrancher l'affichage

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
    
    main = Main(Robotsim(450, 450, "astroboy", "blue")) #on creer le robot ici
    
    main.run_sim()
    
    print("la simulation a dure %d tours" % (main.world.world_temps / main.world.dt))
    
