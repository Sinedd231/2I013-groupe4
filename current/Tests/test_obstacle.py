'''
Created on 4 mars 2019

@author: Denis
'''
import unittest
from MVC.model.obstacle import Obstacle

class TestObstacle(unittest.TestCase):
    
    def setUp(self):
        self.obstacle = Obstacle(15,0,50,50)
        
    def testPoints(self):
        self.assertEqual(self.obstacle.x, 15)
        self.assertEqual(self.obstacle.y,0)
        self.assertEqual(self.obstacle.largeur,50)
        self.assertEqual(self.obstacle.hauteur,50)
        self.assertEqual(self.obstacle.x1, 15+50)
        self.assertEqual(self.obstacle.y1,0+50)
    
    def testVecteurs(self):
        
        self.assertListEqual([ [self.obstacle.x, self.obstacle.y],
                              [self.obstacle.x1, self.obstacle.y],
                              [self.obstacle.x1, self.obstacle.y1],
                              [self.obstacle.x, self.obstacle.y1] ], 
                              self.obstacle.getVecteurs())
    
    def testNbrCote(self):
        self.assertEqual(self.obstacle.nbrCotes(),4)
    
    def testCotes(self):
        
        self.assertListEqual( [ [ [self.obstacle.x, self.obstacle.y],[self.obstacle.x1, self.obstacle.y]],
                               [[self.obstacle.x1, self.obstacle.y],[self.obstacle.x1, self.obstacle.y1]],
                               [[self.obstacle.x1, self.obstacle.y1], [self.obstacle.x, self.obstacle.y1]],
                              [[self.obstacle.x, self.obstacle.y1], [self.obstacle.x, self.obstacle.y]] ], self.obstacle.getCotes())
    
        
if __name__ == '__main__':
    unittest.main()
    
    