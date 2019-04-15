'''
Created on 18 fevr. 2019

@author: Denis
'''

from MVC.model.obstacle import Obstacle
from MVC.view.viewer import Viewer
from MVC.model.world import World
from MVC.model.robot_sim import Robotsim
from MVC.view.world_view import WorldView
from MVC.model.map_builder import MapBuilder
from MVC.exceptions.collision_exception import CollisionException
from MVC.exceptions.objectif_atteint_exception import ObjectifException
from MVC.model.superviseur import Superviseur
import time
from MVC.controller.strategies import SquareStrat, LigneStrat, TournerDroiteStrat, TriangleStrat, PolygoneStrat, TourStrat
from MVC.model.robot_adapter import RobotAdapter


class Main:

    def __init__(self,robot):

        self.robot=robot
        self.robot.x=50
        self.robot.y=50

        if isinstance(self.robot, Robotsim):
            self.init_sim()
        else:
            self.init_reel()

    def init_sim(self):
        obstacle1 = Obstacle(150,0,50,50)
        obstacle2 = Obstacle(150,100,50,50)
        obstacle3 = Obstacle(150,200,50,50)
        obstacle4 = Obstacle(600,600,50,50)
        obstacle5 = Obstacle(600,600,50,50)
        obstacle6 = Obstacle(600,600,50,50)
        self.viewer = Viewer(self)
        self.world = World()
        self.world.add_robot(self.robot)
        self.world.add_obstacle(obstacle1)
        self.world.add_obstacle(obstacle2)
        self.world.add_obstacle(obstacle3)

        self.map_builder = MapBuilder()
        self.map_builder.build_random(self.world)

        self.superviseur= Superviseur(self.robot, LigneStrat(self,100))

        self.worldview = WorldView(self.world, self.viewer)
        self.worldview.draw_world() #ligne a commenter si vous voulez debrancher l'affichage


    def init_reel(self):

        self.world = World()
        self.world.add_robot(self.robot)

        #on evitera GoalStrat tout simplement parce que world n'a pas d'objectif (pour l'instant)
        self.superviseur= Superviseur(self.robot, LigneStrat(self,50))


    def run(self):

        if isinstance(self.robot, Robotsim):
            self.run_sim()
        else:
            self.run_reel()

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

    def run_reel(self):

        while True:
            self.superviseur.step(self.world.dt)
            if self.robot.get_distance() < 3000:
                self.robot.stop()
                break
            time.sleep(self.world.dt)


if __name__ == '__main__':

    main = Main(Robotsim(450,450,"aa","pink")) #on creer le robot ici

    main.run()

    print("la simulation a dure %d tours" % (main.world.world_temps / main.world.dt))
