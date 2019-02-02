'''
@author : Alexandre'''

class Robot :
    """
        x represente l'abscisse du robot, scalaire
        y represente l'ordonne du robot, scalaire
        direction represente l'axe dans lequel le robot est oriente, vecteur
        dx represente la vitesse du robot selon l'axe des abscisses, scalaire
        dy represente la vitesse du robot selon l'axe des ordonnes, scalaire
        """
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.dx = 0.0
        self.dy = 0.0
        
        """@author: Denis"""
        
        #coordonnees initiaux du triangle qui le represente, fixees arbitrairement
        #note : on a besoin de tableaux ici car on aura besoin de faire des operations sur ces valeurs, ce qui est impossible avec des tuples
        self.A= [self.x, self.y]
        self.B= [self.A[0]-20, self.A[1]+20]
        self.C= [self.A[0]+20, self.B[1]]
        self.centregravite= 0,0
        