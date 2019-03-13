'''
Created on 11 mars 2019

@author: Alexandre
'''

import unittest
from MVC.model.superviseur import Superviseur
from MVC.model.abstract_robot import Robot
from MVC.controller.strategie import Strategie
from MVC.model.objectif import Objectif


class testSuperviseur(unittest.TestCase):

    def setUp(self):
        self.R = Robot(450,450)
        self.superviseur = Superviseur (self.R)
    
    def testInit(self):
        self.assertIs(self.superviseur.robot,self.R)
        self.assertIsNone(self.superviseur.goal)
        self.assertIsInstance(self.superviseur.strategie,Strategie)

    def testTranslateCommand(self):
        self.superviseur.v = 2
        self.superviseur.omega = 10 
        self.superviseur.translate_command()
        self.assertEqual(self.superviseur.robot.vdroite,0.2)
        self.assertEqual(self.superviseur.robot.vgauche,0.12)

    def testCalculDps(self):
        self.assertTupleEqual(self.superviseur.calcul_dps(2,10),(0.2,0.12))
        
    def testDefineGoal(self):
        G1 = Objectif(600,600)
        self.superviseur.define_goal(G1)
        self.assertIs(G1,self.superviseur.goal)


if __name__ =='__main__':
    unittest.main()