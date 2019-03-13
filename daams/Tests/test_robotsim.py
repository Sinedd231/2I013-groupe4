'''
Created on 13 mars 2019

@author: Denis
'''

import unittest
from MVC.model.robotsim import Robotsim
from math import cos, sin, atan2

class Test_robotsim (unittest.TestCase):

    def setUp(self):
        self.robot=Robotsim(450,450,"robot1","green")

    def test_init(self):
        self.assertEqual(self.robot.nom,"robot1")
        self.assertEqual(self.robot.couleur,"green")
        self.assertEqual(self.robot.x,450)
        self.assertEqual(self.robot.y,450)

    def test_update_points_triangle(self):
        self.robot.update_points_triangle()
        self.assertListEqual(self.robot.A,[450,450])
        self.assertListEqual(self.robot.B,[430,470])
        self.assertListEqual(self.robot.C,[430,430])
        self.assertListEqual(self.robot.centregravite,[1/3*1310,1/3*1350])

    def test_update_coords_dir(self):
        ancienA= self.robot.A
        ancienB= self.robot.B
        ancienC= self.robot.C
        self.robot.update_coords_dir()

        angle= atan2(self.robot.direction[1],self.robot.direction[0])
        self.assertListEqual(self.robot.A, [cos(angle)*(ancienA[0]-self.robot.centregravite[0])- sin(angle)*(ancienA[1]-self.robot.centregravite[1])+self.robot.centregravite[0],
                                            sin(angle)*(ancienA[0]-self.robot.centregravite[0])+ cos(angle)*(ancienA[1]-self.robot.centregravite[1])+self.robot.centregravite[1]])

        self.assertListEqual(self.robot.B, [cos(angle)*(ancienB[0]-self.robot.centregravite[0])- sin(angle)*(ancienB[1]-self.robot.centregravite[1])+self.robot.centregravite[0],
                                            sin(angle)*(ancienB[0]-self.robot.centregravite[0])+ cos(angle)*(ancienB[1]-self.robot.centregravite[1])+self.robot.centregravite[1]])

        self.assertListEqual(self.robot.C, [cos(angle)*(ancienC[0]-self.robot.centregravite[0])- sin(angle)*(ancienC[1]-self.robot.centregravite[1])+self.robot.centregravite[0],
                                            sin(angle)*(ancienC[0]-self.robot.centregravite[0])+ cos(angle)*(ancienC[1]-self.robot.centregravite[1])+self.robot.centregravite[1]])




    def test_update_coords_capteur(self):
        ancienA= self.robot.capteur.A
        ancienB= self.robot.capteur.B
        ancienC= self.robot.capteur.C
        self.robot.update_coords_capteur()

        angle= atan2(self.robot.capteur.direction[1],self.robot.capteur.direction[0])
        self.assertListEqual(self.robot.capteur.A, [cos(angle)*(ancienA[0]-ancienA[0])- sin(angle)*(ancienA[1]-ancienA[1])+ancienA[0],
                                            sin(angle)*(ancienA[0]-ancienA[0])+ cos(angle)*(ancienA[1]-ancienA[1])+ancienA[1]])

        self.assertListEqual(self.robot.capteur.B, [cos(angle)*(ancienB[0]-ancienB[0])- sin(angle)*(ancienB[1]-ancienB[1])+ancienB[0],
                                            sin(angle)*(ancienB[0]-ancienB[0])+ cos(angle)*(ancienB[1]-ancienB[1])+ancienB[1]])

        self.assertListEqual(self.robot.capteur.C, [cos(angle)*(ancienC[0]-ancienC[0])- sin(angle)*(ancienC[1]-ancienC[1])+ancienC[0],
                                            sin(angle)*(ancienC[0]-ancienC[0])+ cos(angle)*(ancienC[1]-ancienC[1])+ancienC[1]])

    def test_getVecteurs(self):

        self.assertListEqual(self.robot.getVecteurs(), [[450,450],[430,470],[430,430]])

    def test_getCotes(self):
        
        self.assertListEqual(self.robot.getCotes(),[ [[450,450],[430,470]],
                                                    [[430,470],[430,430]],
                                                    [[430,430],[450,450]] ])
    
    def testNbrCotes(self):
        self.assertEqual(self.robot.nbrCotes(),3)
        

if __name__=='__main__':
    unittest.main()