'''
Created on 5 mars 2019

@author: Denis
'''

from .go_to_goal import GoToGoalControlleur
from .move_forward import MoveForwardControlleur
from .turn_90 import Turn90Controlleur
from .stop import StopControlleur
from MVC.view.viewer import HAUTEUR, LARGEUR

class Strategie:
    
    def __init__(self,superviseur):
        """classe qui regroupe toutes les strategies pour le robot
        on donnera en argument un superviseur
        """
        
        self.superviseur= superviseur
        
        #on doit creer ici tous nos controlleurs, pour pouvoir les manipuler et creer des strats
        self.gotogoal= GoToGoalControlleur(self.superviseur)
        self.moveforward = MoveForwardControlleur(self.superviseur)
        self.turn90 = Turn90Controlleur(self.superviseur)
        self.stop= StopControlleur(self.superviseur)
        
        self.controlleuractuel=None
        
        #ces 2 parametres servent a dessiner le carre
        self.compteur_forward=1 #compteur pour les deplacements horizontaux
        self.compteur_turn=1    #compteur pour les rotations
    
    def change_controlleur(self, controlleur):
        self.controlleuractuel = controlleur
    
    def aller_vers_goal(self):
        
        self.change_controlleur(self.gotogoal)
        self.controlleuractuel.execute()
    
    def dessiner_carre(self):
        
        if self.compteur_forward%100==0:    #si le robot s'est deplace horizontalement pendant 100 tours (cad si il a fini de tracer un cote du carre)
                self.change_controlleur(self.turn90)    #on change le controlleur pour qu'il puisse tourner
                self.compteur_turn +=1   #on compte aussi les tours ou il est en rotation
                if self.compteur_turn%300==0:   #quand il a fini la rotation, on renitialise compteur forward
                    self.compteur_forward=1
        else:
                self.avancer_droit()
                self.compteur_forward +=1
                self.compteur_turn=1                    #on renitialise compteur turn a chaque tour ou il n'est pas en rotation
                self.turn90= Turn90Controlleur(self.superviseur)    #a chaque nouvelle position (x,y) on doit calculer son nouveau vecteur de rotation, on creer donc
                                                                    #a chaque tour un nouveau controlleur turn90
                                                        
        self.controlleuractuel.execute()
    
    def avancer_droit(self):
        
        self.change_controlleur(self.moveforward)
        self.stop_bords()
        self.controlleuractuel.execute()
    
    #cette strategie est plutot destinee a etre utilisee par les autres strategies que par le superviseur lui meme
    def stop_bords(self):
        
        if self.superviseur.robot.A[0] >= LARGEUR or self.superviseur.robot.A[0] <= 0 or self.superviseur.robot.A[1] <= 0 or self.superviseur.robot.A[1] >= HAUTEUR:
            self.change_controlleur(self.stop)
            
                                                        