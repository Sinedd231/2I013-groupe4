'''
Created on 11 mars 2019

@author: Alexandre
@correction: Denis
'''

import unittest
from MVC.model.superviseur import Superviseur
from MVC.model.abstract_robot import Robot
from MVC.controller.strategies import LigneStrat, Turn90Strat


class testSuperviseur(unittest.TestCase):

    def setUp(self):
        self.R = Robot(450,450)
        self.superviseur = Superviseur(self.R,LigneStrat(self,50))
    
    def testInit(self):
        self.assertIs(self.superviseur.robot,self.R)
        self.assertIsInstance(self.superviseur.strategie,LigneStrat)

    def testTranslateCommand(self):
        v = 2
        omega = 10 
        self.superviseur.translate_command(v,omega)
        self.assertEqual(self.superviseur.robot.vdroite,0.2)
        self.assertEqual(self.superviseur.robot.vgauche,0.12)

    def testCalculDps(self):
        self.assertTupleEqual(self.superviseur.calcul_dps(2,10),(0.2,0.12))
        
    def testRedefineStrat(self):
        new_strat = Turn90Strat(self.superviseur)
        self.superviseur.redefine_strat(new_strat)
        self.assertIs(new_strat,self.superviseur.strategie)


if __name__ =='__main__':
    unittest.main()
    