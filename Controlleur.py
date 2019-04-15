'''
Created on 2 fevr. 2019

@author: Denis,Alexandre
'''
from Robot import *
from math import *
import random

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
    
    
    def avancer(self, canvas, item, obstacles):
        """ fonction qui permet au robot d'avancer selon sa direction,
            on donnera comme argument un canvas sur lequel representer le mouvement, un item ,qui sera ici notre robot, sur lequel appliquer le mouvement
            et des obstacles (stockes dans un dictionnaire) qui faudra potentiellement eviter
        """
        
        self.robot.dx = cos(self.convertir_direction_angle())   #on calcule d'abord le deplacement relatif du robot dx dy EN FONCTION DE SA DIRECTION
        self.robot.dy = sin(self.convertir_direction_angle())
        
        canvas.move(item, self.robot.dx, self.robot.dy) #code Tkinter, on deplace l'item de dx dy
        
        self.robot.x += self.robot.dx   #puis on incremente x et y
        self.robot.y += self.robot.dy
        
        # et on met a jour les points relatifs pour avoir un affichage coherent
        
        self.update_coords_dir() 
        canvas.coords(item , self.robot.A[0], self.robot.A[1], self.robot.B[0], self.robot.B[1], self.robot.C[0], self.robot.C[1])
        
        #on teste les collisions    
                                                    #note: on met ces tests en dernier car on a pas encore les capteurs
        self.check_bord()                           #donc une collision implique juste un changement de direction
        self.check_obstacles(canvas, obstacles)     #mais avec les capteurs il faudra repenser ces tests
    
    
    
    def check_bord(self):
        """implemente les rebonds sur les extremites de la fenetre"""
        
        if self.robot.A[0] >= 800 or self.robot.A[0] <=0 or self.robot.A[1]>=800 or self.robot.A[1]<0:   #si il atteint les bords, alors il fait demi tour
            self.tourner_degree(random.uniform(150,190))                                                 #avec un angle aleatoire
    
    
    
    def check_obstacles(self,canvas, obstacles):
        """implemente les rebonds sur les obstacles"""
        
        for obstacle in obstacles.values(): #on doit verifier pour chaque obstacle si il y a collision, on itere donc sur les valeurs du dictionnaire
            
            if len(canvas.find_overlapping(canvas.coords(obstacle)[0], canvas.coords(obstacle)[1], canvas.coords(obstacle)[2], canvas.coords(obstacle)[3]))>1:
                """ find overlapping c'est une simple fonction qui retourne les elements qui chevauchent le canvas
                    le canvas etant ici notre fenetre, en appliquant find overlapping a un obstacle, la fonction doit 
                    renvoyer constamment 1 element car cet obstacle chevauchera bien continuellement la fenetre
                    
                    mais si notre robot touche l'obstacle, la fonction en renverra 2 car a l'emplacement precis de l'obstacle, determine
                    par canvas.coords(obstacle), un autre element s'est rajoute
                    
                    on teste donc si le nombre d'element renvoye est plus grand que 1, si oui alors notre robot est rentre en
                    collision avec l'obstacle
                """ 
                   
                self.tourner_degree(random.uniform(150,190))    #note : on doit trouver une meilleure reponse aux collisions, a voir avec
                                                                #l'arrivee des capteurs
    
