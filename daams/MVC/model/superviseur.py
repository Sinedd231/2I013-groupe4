'''
Created on 14 févr. 2019

@author: Denis
'''

from MVC.controller.go_to_goal import GoToGoalControlleur
from MVC.controller.move_forward import MoveForwardControlleur
from MVC.controller.turn_90 import Turn90Controlleur

class Superviseur:
    
    def __init__(self, robot):
        """le superviseur sert d'intermediaire entre les controlleurs et le robot
        le superviseur choisira un comportement et appellera les bons controlleurs
        les controlleurs renverront une vitesse lineaire et une vitesse angulaire, que le superviseur traduira
        en commande pour le robot
        arguments : un robot
        """
        self.robot = robot;
        self.goal = None  # Chaque superviseur aura acces a l'objectif de world, on initialise a None puis on le mettra a jour plus tard
        
        self.gotogoal= GoToGoalControlleur(self)
        self.moveforward = MoveForwardControlleur(self)
        self.turn90 = Turn90Controlleur(self)
        
        self.controlleuractuel=None
        
        #ces 2 parametres servent a dessiner le carre
        self.compteur_forward=1 #compteur pour les deplacements horizontaux
        self.compteur_turn=1    #compteur pour les rotations
        
    def change_controlleur(self, controlleur):
        self.controlleuractuel = controlleur
    
    
    def update(self):
        
        carre=True #cette ligne permet a elle seule de determiner le comportement du superviseur: si True on dessinera un carre, si False on cherchera
                    #a atteindre l'objectif de world
                    #on pourra trouver encore d'autre comportements
        
        if carre:
            if self.compteur_forward%100==0:    #si le robot s'est deplace horizontalement pendant 100 tours (cad si il a fini de tracer un cote du carre)
                self.change_controlleur(self.turn90)    #on change le controlleur pour qu'il puisse tourner
                self.compteur_turn +=1   #on compte aussi les tours ou il est en rotation
                if self.compteur_turn%300==0:   #quand il a fini la rotation, on renitialise compteur forward
                    self.compteur_forward=1
            else:
                self.change_controlleur(self.moveforward)   
                self.compteur_forward +=1
                self.compteur_turn=1    #on renitialise compteur turn a chaque tour ou il n'est pas en rotation
                self.turn90= Turn90Controlleur(self)    #a chaque nouvelle position (x,y) on doit calculer son nouveau vecteur de rotation, on creer donc
                                                        #a chaque tour un nouveau controlleur turn90
        else:
            self.change_controlleur(self.gotogoal)
    
           
    def step(self,dt):
        self.update()
        self.controlleuractuel.execute()
        self.translate_command()
        self.robot.step(dt)

    
    def translate_command(self):
        
        v_droite, v_gauche = self.calcul_dps(self.v, self.omega)
        self.robot.set_dps(v_droite, v_gauche)
        
    def calcul_dps(self,v ,omega):
        
        v_droite = ((2*v)+(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        v_gauche = ((2*v)-(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        
        return v_droite, v_gauche
    