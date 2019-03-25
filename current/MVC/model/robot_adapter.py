'''
Created on 20 mars 2019

@author: Denis
'''

#from MVC.model.robot2I013.robot2I013 import Robot2I013

MOTOR_LEFT=1
MOTOR_RIGHT=2

class RobotAdapter:
    """cette classe servira de pont entre le l'api du robot reel et notre code, qui s'est avere etre trop
    eloigne du reel
    On va concretement utiliser cette classe pour appeler les fonctions du robot reel avec nos variables a nous
    """
    
    def __init__(self,Robot2I013):

        self.robot= Robot2I013

        #le robot doit avoir un attribut self.capteur sinon il y aura une erreur dans world.py
        self.capteur = None

        self.rayonroue= self.robot.WHEEL_DIAMETER/2
        self.largeur= self.robot.WHEEL_BASE_WIDTH
        self.vdroite= 0 #deg/s
        self.vgauche=0  #deg/s

        self.rotation_moteur_droite=0
        self.rotation_moteur_gauche=0
        #self.vmax = ??

    def set_dps(self,vdroite, vgauche):

        self.vdroite=vdroite
        self.vgauche=vgauche

    def step(self,dt):

        self.robot.set_motor_dps(MOTOR_LEFT, self.vgauche)
        self.robot.set_motor_dps(MOTOR_RIGHT, self.vdroite)

        self.rotation_moteur_droite+=self.vdroite*dt
        self.rotation_moteur_gauche+=self.vgauche*dt

    def get_encoder(self):

        return self.rotation_moteur_droite, self.rotation_moteur_gauche

    def reset_encoder(self):
        
        self.robot.offset_motor_encoder(MOTOR_RIGHT,self.get_encoder()[0])
        self.robot.offset_motor_encoder(MOTOR_LEFT,self.get_encoder()[1])

    def stop(self):

        self.robot.stop()
