'''
Created on 2 fevr. 2019

@author: Denis,Alexandre
'''
from Robot import *
from math import *

class Controlleur:
    """le controlleur prendra en variable un robot, qu'il controlera"""
    
    def __init__(self, robot):
        self.robot= robot
        
    
    def tourner_radiant (self,angle):
        """
        la fonction prend un objet de la classe robot et un angle en radiant
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        a=self.robot.direction[0]*cos(angle)-self.robot.direction[1]*sin(angle) #on utilise la formule de la matrice de rotation
        b=self.robot.direction[0]*sin(angle)+self.robot.direction[1]*cos(angle)
        self.robot.direction = [a,b]
        
        
    def tourner_degree (self,angle):
        """
        la fonction prend un objet de la classe robot et un angle en degree
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        
        a=self.robot.direction[0]*cos(radians(angle))-self.robot.direction[1]*sin(radians(angle)) #on utilise la formule de la matrice de rotation
        b=self.robot.direction[0]*sin(radians(angle))+self.robot.direction[1]*cos(radians(angle))
        self.robot.direction = [a,b]
        
        
    def tourner_point(self, ox, oy, angle, P):
        """ retourne un nouveau point qui est la rotation du point P autour d'un point d'origine O (ox,oy) de 'angle' radians
            puisque les points du triangle sont stockes sous forme de tableau, ici on retourne alors un tableau
        """
        
        return [ cos(angle) * (P[0]-ox) - sin(angle) * (P[1]-oy) + ox , sin(angle) * (P[0]-ox) + cos(angle) * (P[1]-oy)+ oy ]
    
    
    def update_coords_dir(self):
        """permet de mettre a jour les coordonnees relatifs du robot suite a un changement de direction"""
        
        self.robot.update_points_triangle() #on met a jour ABC et le centre de gravite pour s'assurer d'avoir les bonnes valeurs pour les calculs,
                                            #meme si on ecrasera ces valeurs par les nouvelles
                                            
        self.robot.A= self.tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], self.convertir_direction_angle(), self.robot.A)
        self.robot.B= self.tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], self.convertir_direction_angle(), self.robot.B)
        self.robot.C= self.tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], self.convertir_direction_angle(), self.robot.C)
        
        #on fait donc la rotation des 3 points autour du centre de gravite
        
        
    def convertir_direction_angle(self):
        """retourne l'angle en radians correspondant a la direction du robot"""
        
        return atan2( self.robot.direction[0], self.robot.direction[1] )
    
    
    def avancer(self, canvas, item):
        """ fonction qui permet au robot d'avancer selon sa direction,
            on donnera comme argument un canvas sur lequel representer le mouvement et un item ,qui sera ici notre robot, sur lequel appliquer le mouvement
        """
        
        self.robot.dx = cos(self.convertir_direction_angle())   #on calcule d'abord le deplacement relatif du robot dx dy EN FONCTION DE SA DIRECTION
        self.robot.dy = sin(self.convertir_direction_angle())
        
        canvas.move(item, self.robot.dx, self.robot.dy) #code Tkinter, on deplace l'item de dx dy
        
        self.robot.x += self.robot.dx   #puis on incremente x et y
        self.robot.y += self.robot.dy
        
        self.update_coords_dir() # et on met a jour les points relatifs pour avoir un affichage coherent
       
        if self.robot.A[0] >= 800 or self.robot.A[0] <=0 or self.robot.A[1]>=800 or self.robot.A[1]<0:   #si il atteint les bords, alors il fait demi tour
            self.tourner_degree(180)                        #PARTIE NON FINIE                            
    
        