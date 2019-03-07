"""
@author: Alexandre
"""

import unittest
from MVC.model.abstract_robot import Robot


class test_robot(unittest.TestCase):
    def setUp(self):
        self.a = Robot(1,2)

    def test_init(self):
        self.assertEqual(self.a.x,1)
        self.assertEqual(self.a.y,2)


    def test_set_dps(self):
        self.a.set_dps(2.0,3.0)
        self.assertEqual(self.a.vdroite,2.0)
        self.assertEqual(self.a.vgauche,3.0)

if __name__=='__main__':
    unittest.main()
