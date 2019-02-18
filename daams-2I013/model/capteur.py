'''
Created on 14 févr. 2019

@author: Denis
'''


class Capteur:
    
    def __init__(self, robot):
        
        self.robot = robot;
        self.update_points_triangle()
    
    
    def update_points_triangle(self):
        
        self.direction= ( -1 * self.robot.direction[0], -1 * self.robot.direction[1] )
        self.A = [ self.robot.A[0], self.robot.A[1] ]
        self.B = [ self.A[0] - 20, self.A[1] + 20 ]
        self.C = [ self.B[0], self.A[1] - 20 ]