'''
Created on 2 fevr. 2019

@author: Denis,Alexandre
'''
from robot import *
import random
import formules as fm

class Controlleur:
    """le controlleur prendra en variable un robot, qu'il controlera
        il aura un booleen pause qui determinera si le robot est en mouvement ou a l'arret, il est
        a False initialement
    """
    
    def __init__(self, robot):
        self.robot= robot
    
        self.update_coords_dir()
        self.pause=False
    
    def tourner_radiant (self,angle):
        """
        la fonction prend un objet de la classe robot et un angle en radiant
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        self.robot.direction = fm.rotation_vecteur(self.robot.direction, angle)
        
        
    def tourner_degree (self,angle):
        """
        la fonction prend un objet de la classe robot et un angle en degree
        en parametre.
        Elle modifie l'attribut direction de l'objet robot
        """
        self.robot.direction = fm.rotation_degree(self.robot.direction, angle)
        
    
    def update_coords_dir(self):
        """permet de mettre a jour les coordonnees relatifs du robot suite a un changement de direction"""
        
        self.robot.update_points_triangle() #on met a jour ABC et le centre de gravite pour s'assurer d'avoir les bonnes valeurs pour les calculs,
                                            #meme si on ecrasera ces valeurs par les nouvelles
                                            
        self.robot.A= fm.tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]), self.robot.A)
        self.robot.B= fm.tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]), self.robot.B)
        self.robot.C= fm.tourner_point(self.robot.centregravite[0], self.robot.centregravite[1], fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]), self.robot.C)
        
        #on fait donc la rotation des 3 points autour du centre de gravite
        
    
    
    def avancer(self, canvas, item, dessin_capteur, obstacles):
        """ fonction qui permet au robot d'avancer selon sa direction,
            on donnera comme argument un canvas sur lequel representer le mouvement, un item ,qui sera ici notre robot, sur lequel appliquer le mouvement,
            un dessin_capteur, c'est a dire le dessin de notre capteur pour le mettre a jour et une liste d'obstacles qui faudra potentiellement eviter
        """
        
        if self.pause==False:
            self.robot.dx = fm.cos(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))  #on calcule d'abord le deplacement relatif du robot dx dy
            self.robot.dy = fm.sin(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))  #EN FONCTION DE SA DIRECTION
            
            self.robot.x += self.robot.dx   #puis on incremente x et y
            self.robot.y += self.robot.dy
            
            # et on met a jour les points relatifs pour avoir un affichage coherent
            
            self.update_coords_dir() 
            canvas.coords(item , self.robot.A[0], self.robot.A[1], self.robot.B[0], self.robot.B[1], self.robot.C[0], self.robot.C[1])
                
            #on fait marcher le capteur
            if (self.robot.capteur.detect(canvas, dessin_capteur, obstacles)==True 
            or self.robot.A[0]>=900 or self.robot.A[0]<=0 or self.robot.A[1]>=900 or self.robot.A[1]<=0):
            
                self.arreter()
                self.afficher_pas_restant(obstacles)
            
    
    
    def arreter(self):
        
        self.pause=True
        
    
    def afficher_pas_restant(self, obstacles):
        """ fonction qui affiche le nombre de pas restant avant collision, en se basant sur get_pas_restant
        
        """
        
        if not self.pause:
            print("robot encore en deplacement")
        else:
            print("%s : il reste %d pas" % (self.robot.nom, self.robot.capteur.get_pas_restant(obstacles)))
            
            
    
    
    
    
    def tourner_vers_objectif (self,obj):
        u=obj.x-self.robot.x
        v=obj.y-self.robot.y
        self.tourner_radiant(fm.convertir_direction_angle(u,v))
            
            