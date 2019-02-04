'''
@author : Alexandre, Denis'''

class Robot :
    """
        x represente l'abscisse du robot, scalaire
        y represente l'ordonne du robot, scalaire
        direction represente l'axe dans lequel le robot est oriente, vecteur
        dx represente la vitesse du robot selon l'axe des abscisses, scalaire
        dy represente la vitesse du robot selon l'axe des ordonnes, scalaire
    """
    
    def __init__(self,x,y,direction):
        self.x = x  #coordonnees
        self.y = y  #absolues
        self.direction = direction
        self.dx = 0.0
        self.dy = 0.0
        
    
        
    def update_points_triangle(self):
        """ le robot sera represente par un triangle ABC avec A le sommet
            on met a jour a chaque appel les points A,B,C et le centre de gravite avec les bonnes valeurs de x,y
            cette fonction sert aussi d'initialisation de variable
            on appellera ces points les coordonnees relatives 
        """
        
        self.A= [ self.x, self.y ]
        self.B= [ self.A[0]-20, self.A[1]+20 ]
        self.C= [ self.B[0], self.A[1]-20 ]
        self.centregravite = [ 1/3 * (self.A[0]+self.B[0]+self.C[0]), 1/3 * (self.A[1]+self.B[1]+self.C[1]) ]