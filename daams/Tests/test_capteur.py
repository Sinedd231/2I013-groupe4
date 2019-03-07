"""
Created on 7 mars 2019
@author : Alexandre
"""

import unittest
from MVC.model.capteur import Capteur
from MVC.model.robotsim import Robotsim
from MVC.model.world import World
from MVC.model.obstacle import Obstacle
from MVC.model.abstract_polygone import Polygone


class TestCapteur(unittest.TestCase):

    def setUp(self):
        self.R = Robotsim(450,450,"test","blue")
        self.capteur = Capteur(self.R)

    def test_init(self):
        self.assertIs(self.capteur.robot,self.R)

    def test_update_points_triangle(self):
        self.capteur.update_points_triangle()
        self.assertTupleEqual(self.capteur.direction,(-1,0))
        self.assertListEqual(self.capteur.A,[450,450])
        self.assertListEqual(self.capteur.B,[350,455])
        self.assertListEqual(self.capteur.C,[350,445])


    def test_getVecteurs(self):
        self.capteur.update_points_triangle()
        self.assertListEqual(self.capteur.getVecteurs(),[[450,450],[350,455],[350,445]])


    def TestNbrCotes(self):
        self.assertEqual(self.capteur.nbrCotes(),3)

    def TestGetCotes(self):
        self.assertListEqual(self.capteur.getCotes(),[[450,450],[350,455],[350,445]])

    def TestDetect_solides(self):
        obs1=Obstacle(450,470,10,15)
        obs2=Obstacle(800,800,10,10)
        W1=World()
        W2=World()
        W1.add_obstacle(obs1)
        W2.add_obstacle(obs2)
        self.assertTrue(self.capteur.detect_solides(W1))
        self.assertFalse(self.capteur.detect_solides(W2))



if __name__ =='__main__':
    unittest.main()
