class Robot :
    """
        x représente l'abscisse du robot, scalaire
        y représente l'ordonné du robot, scalaire
        direction représente l'axe dans lequel le robot est orienté, vecteur
        dx représente la vitesse du robot selon l'axe des abscisses, scalaire
        dy représente la vitesse du robot selon l'axe des ordonnés, scalire
        """
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.dx = 0.0
        self.dy = 0.0

        
