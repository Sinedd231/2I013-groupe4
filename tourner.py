from Robot import *
from math import *




def tourner_radiant (robot,angle):
    """
    la fonction prend un objet de la classe robot et un angle en radiant
    en paramètre.
    Elle modifie l'attribut direction de l'objet robot
    """
    a=robot.direction[0]*cos(angle)-robot.direction[1]*sin(angle)#on utilise la formule de la matrice de rotation
    b=robot.direction[0]*sin(angle)+robot.direction[1]*cos(angle)
    robot.direction = (a,b) 


#c=Robot(0,0,(6,2))
#print(c.direction)
#tourner_radiant(c,pi/4)
#print(c.direction)


def tourner_degree (robot,angle):
    """
    la fonction prend un objet de la classe robot et un angle en degree
    en paramètre.
    Elle modifie l'attribut direction de l'objet robot
    """
    a=robot.direction[0]*cos(radians(angle))-robot.direction[1]*sin(radians(angle)) #on utilise la formule de la matrice de rotation
    b=robot.direction[0]*sin(radians(angle))+robot.direction[1]*cos(radians(angle))
    robot.direction = (a,b)

#r=Robot(0,0,(3,5))
#print(r.direction)
#tourner_degree(r,degrees(-pi/6))
#print(r.direction)


