'''
Created on 6 mars 2019

@author: Denis
'''
import unittest
from MVC.model.objectif import Objectif

class TestObjectif(unittest.TestCase):
    
    def setUp(self):
        self.objectif = Objectif(10,10)
    
    def testPoints(self):
        
        self.assertEqual(self.objectif.x,10)
        self.assertEqual(self.objectif.y,10)
        self.assertEqual(self.objectif.x1,10+30)
        self.assertEqual(self.objectif.y1,10+30)
    
    def testCentre(self):
        
        self.assertListEqual([25,25], self.objectif.centre() )
    
    def testVecteurs(self):
        
        self.assertListEqual([ [self.objectif.x, self.objectif.y],
                              [self.objectif.x1, self.objectif.y],
                              [self.objectif.x1, self.objectif.y1],
                              [self.objectif.x, self.objectif.y1] ], 
                              self.objectif.getVecteurs())
    
    def testCotes(self):
        
        self.assertListEqual( [ [[self.objectif.x, self.objectif.y],[self.objectif.x1, self.objectif.y]],
                               [[self.objectif.x1, self.objectif.y],[self.objectif.x1, self.objectif.y1]],
                               [[self.objectif.x1, self.objectif.y1], [self.objectif.x, self.objectif.y1]],
                              [[self.objectif.x, self.objectif.y1], [self.objectif.x, self.objectif.y]] ], self.objectif.getCotes())
    
    def testNbrCote(self):
        self.assertEqual(self.objectif.nbrCotes(),4)

if __name__ == '__main__':
    unittest.main()
        