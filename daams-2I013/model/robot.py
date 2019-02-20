'''
Created on 14 févr. 2019

@author: Denis
'''

from .capteur import Capteur
from .superviseur import Superviseur
from utiles import formules as fm
from .abstract_polygone import Polygone


class Robot(Polygone):
    # le robot sera represente par un triangle
    
    def __init__(self, x, y , nom, couleur):
        """arguments: x,y, un nom et une couleur
        """
        self.nom = nom
        self.x = x  # coordonnees
        self.y = y  # absolues
        self.direction = [0, -1]  # fixee, mais ne pas mettre [0,0] ici
        self.couleur = couleur
        
        self.update_coords_dir()  # pour que le robot puisse avoir la bonne pose dès le début
        
        self.capteur = Capteur(self)  # on creer son capteur et son superviseur ici pour alleger le code ailleurs
        self.update_coords_capteur()
        
        self.superviseur = Superviseur(self)
    
    def update_points_triangle(self):
        # le robot sera represente par un triangle ABC avec A le sommet
        # on met a jour a chaque appel les points A,B,C et le centre de gravite avec les bonnes valeurs de x,y
        # cette fonction sert aussi d'initialisation de variable
        # on appellera ces points les coordonnees relatives 
        
        self.A = [ self.x, self.y ]
        self.B = [ self.A[0] - 20, self.A[1] + 20 ]
        self.C = [ self.B[0], self.A[1] - 20 ]
        self.centregravite = [ 1 / 3 * (self.A[0] + self.B[0] + self.C[0]), 1 / 3 * (self.A[1] + self.B[1] + self.C[1]) ]
    
    def update_coords_dir(self):
        """permet de mettre a jour les coordonnees relatives du robot suite a un changement de direction"""
        
        self.update_points_triangle()  # on met a jour ABC et le centre de gravite pour s'assurer d'avoir les bonnes valeurs pour les calculs,
                                        # meme si on ecrasera ces valeurs par les nouvelles
                                            
        self.A = fm.tourner_point(self.centregravite[0], self.centregravite[1], fm.convertir_direction_angle(self.direction[0], self.direction[1]), self.A)
        self.B = fm.tourner_point(self.centregravite[0], self.centregravite[1], fm.convertir_direction_angle(self.direction[0], self.direction[1]), self.B)
        self.C = fm.tourner_point(self.centregravite[0], self.centregravite[1], fm.convertir_direction_angle(self.direction[0], self.direction[1]), self.C)
        # on fait donc la rotation des 3 points autour du centre de gravite
    
    def update_coords_capteur(self):
        """permet de mettre a jour les coordonnees relatives du capteur suite a un changement de direction du robot"""
        
        self.capteur.update_points_triangle() 
                                            
        self.capteur.A = fm.tourner_point(self.capteur.A[0], self.capteur.A[1], fm.convertir_direction_angle(self.capteur.direction[0], self.capteur.direction[1]), self.capteur.A)
        self.capteur.B = fm.tourner_point(self.capteur.A[0], self.capteur.A[1], fm.convertir_direction_angle(self.capteur.direction[0], self.capteur.direction[1]), self.capteur.B)
        self.capteur.C = fm.tourner_point(self.capteur.A[0], self.capteur.A[1], fm.convertir_direction_angle(self.capteur.direction[0], self.capteur.direction[1]), self.capteur.C)
        # similaire a update_coords_dir mais ici on effectue la rotation autour du sommet
        
    def getVecteurs(self):
        return [self.A, self.B, self.C]
    
    def nbrCotes(self):
        return 3  # parce que triangle
    
    def getCotes(self):
        return super(Robot, self).getCotes()
     
    
