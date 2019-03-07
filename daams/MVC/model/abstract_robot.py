'''
Created on 24 févr. 2019

@author: Denis
'''
#CLASSE ABSTRAITE


class Robot(object):
    
    def __init__(self,x,y):
        
        self.x=x    #coordonnees
        self.y=y    #absolues
        self.direction=[1,0]
        self.vdroite=0.0    #vitesses angulaire en rad/s
        self.vgauche=0.0
        self.rayonroue=0.08 #rayon des roues, choisie au hasard pour l'instant, il faudra le remplacer par la veritable valeur plus tard (en metres)
        self.largeur=0.1 #longueur du robot, choisie au hasard pour l'instant, il faudra le remplacer par la veritable valeur plus tard (en metres)
        self.vmax=500 #vitesse maximale du robot, il faudra le remplacer par la veritable valeur plus tard
    
    def set_dps(self,vdroite, vgauche):
        
        self.vdroite=vdroite
        self.vgauche=vgauche
