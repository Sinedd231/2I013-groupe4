'''
Created on 25 févr. 2019

@author: Denis
'''
from MVC.utiles import formules as fm
i=0

class DrawSquareController:
    
    def __init__(self, superviseur):
        """ce controlleur cherchera a dessiner un carre
        arguments : un superviseur
        """
        self.superviseur = superviseur
        
        self.point1 = [self.superviseur.robot.x+50, self.superviseur.robot.y]
        self.point2 = [self.superviseur.robot.x+50, self.superviseur.robot.y+50]
        self.point3 = [self.superviseur.robot.x, self.superviseur.robot.y+50]
        self.point4 = [self.superviseur.robot.x, self.superviseur.robot.y]
        
        self.points= [self.point1, self.point2, self.point3, self.point4]
        self.chemin_vers_goal = [0,0]  # on initialise le vecteur objectif au hasard, il sera correctement mis a jour par la suite  
    
    def calcul_chemin(self):
        
        global i
        
        if i==0:
            if self.superviseur.robot.x >= self.points[0][0]:
                i+=1
        if i==1:
            if self.superviseur.robot.y >= self.points[1][1]:
                i+=1
        if i==2:
            if self.superviseur.robot.x <= self.points[2][0]:
                i+=1
        if i==3:
            if self.superviseur.robot.y <= self.points[3][1]:
                i=0
        
        c=self.points[i]    
        u = c[0] - self.superviseur.robot.x
        v = c[1] - self.superviseur.robot.y
        
        return [u, v]
    
    def set_chemin(self):
        
        self.chemin_vers_goal = self.calcul_chemin()
        
    def execute(self):
    
        self.set_chemin()
        angle=fm.convertir_direction_angle(self.chemin_vers_goal[0], self.chemin_vers_goal[1])-fm.convertir_direction_angle(self.superviseur.robot.direction[0], self.superviseur.robot.direction[1])
        
        v=500 #m/s
        
        self.superviseur.v=v
        self.superviseur.omega=angle/0.1 #rad/s
        
    