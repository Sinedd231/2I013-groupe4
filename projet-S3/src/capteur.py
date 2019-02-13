"""
@author : Denis, Mouad, Alexandre
"""
import formules as fm


class Capteur:

    def __init__(self, longueur, robot):
        """initialise le capteur
        les champs du capteur seront un robot sur lequel il agira, un point x et y, une longueur, et deux autres points x1 et y1
        qui seront determine mathematiquement et qui delimiteront la portee du capteur
        """
        
        self.robot = robot
        self.x = self.robot.A[0]
        self.y = self.robot.A[1]
        self.longueur = longueur
    
        self.x1 = self.x + self.longueur * fm.cos(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))
        self.y1 = self.y + self.longueur * fm.sin(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))
        
    def disp_capteur(self, canvas):
        """affichage du dessin, retourne un objet tkinter"""
        
        line = canvas.create_line(self.x, self.y, self.x1, self.y1)
        return line
    
    def update_coords(self, canvas, item):
        """mise a jour des coordonnees absolues du capteur + mise a jour de l'affichage"""
        
        self.x = self.robot.A[0]
        self.y = self.robot.A[1]
        self.x1 = self.x + self.longueur * fm.cos(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))
        self.y1 = self.y + self.longueur * fm.sin(fm.convertir_direction_angle(self.robot.direction[0], self.robot.direction[1]))
        
        canvas.coords(item, self.x, self.y, self.x1, self.y1)
    
    def detect(self, canvas, item, obstacles):
        """fonction qui implemente les fonctionnalites du capteur, a savoir la mise a jour de ses coordonnees et le test de collision sur une liste d'obstacles"""
        # la complexite de ce code tel qu'il est ecrit actuellement est mauvais, a corriger si necessaire
        
        self.update_coords(canvas, item)
        
        points = fm.points_segment((self.x, self.y), (self.x1, self.y1))
        
        if fm.ensemble_points_est_obstacle(points, obstacles) == True:
            canvas.itemconfig(item, fill='orange')
            return True
            
        else:
            canvas.itemconfig(item, fill='black')
            return False
    
    
    
    def get_pas_restant(self,obstacles):
        """ compte le nombre de pas restant avant collision, 10 etant la plus haute valeur possible
            on utilise les points du segment du capteur pour compter
            si la fonction renvoie 10 c'est que le robot a touche un bord de la fenetre
        """
            #la fonction n'est pas finie et un peu inutile actuellement
            #j'y travaille
        
        
        points = fm.points_segment((self.x, self.y), (self.x1, self.y1))
        compteur=0
        
        for p in points:
            
            if fm.point_est_obstacle(p, obstacles)==False:
                compteur +=1
        
        return compteur
