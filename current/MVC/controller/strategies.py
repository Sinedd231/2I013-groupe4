# -*- coding: utf-8 -*-
'''
Created on 5 mars 2019

@author: Denis
'''

from math import *
from MVC.utiles import formules as fm

""" les strategies prennent tous un superviseur. On joue avec les encoders et selon la strategie,
on essaie d'en tirer une certaine vitesse et vitesse angulaire qu'on transmettra au superviseur
"""

class LigneStrat():
    """cette strategie consiste a faire avancer le robot en ligne droite
    sur une certaine distance donnee en parametre
    """

    def __init__(self,superviseur,distancemax):

        self.superviseur=superviseur
        self.distance=0
        self.distancemax=distancemax

    def get_command(self):

        #si on a pas atteint la distance fixee
        if (self.distance < self.distancemax):
            self.distance= self.superviseur.robot.get_encoder()[0]*self.superviseur.robot.rayonroue*pi/180
            #print("distance parcourue : {}/{}".format(self.distance,self.distancemax))
            return self.superviseur.robot.vmax, 0
        else:
            return 0,0


class SquareStrat():
    """on fait dessiner un carre au robot
    """

    def __init__(self,superviseur):

        self.superviseur= superviseur

        #on a besoin de sous strategies ici
        self.strat_avancer = LigneStrat(self.superviseur,5)
        self.strat_tourner= TournerGaucheStrat(self.superviseur,30)
        
        self.reset=True #on a besoin de cette variable pour reinitialiser correctement
                        #les encodeurs

    def get_command(self):
        #on fait alterner les sous strategies et on
        #base notre raisonnement sur leurs reponses respectives,
        #si une sous strategie renvoie 0,0 on passe a la sous strategie
        #suivante

        v_avancer, omega_avancer = self.strat_avancer.get_command()

        if (v_avancer==0 and omega_avancer==0):
            
            if (self.reset):    #on ne doit reinitialiser qu'une
                                #seule fois, sinon le robot tournera a l'infini
                self.superviseur.robot.reset_encoder()
                self.reset=False
           
            v_tourner, omega_tourner = self.strat_tourner.get_command()

            if (v_tourner==0 and omega_tourner==0):
                self.superviseur.robot.reset_encoder()
                self.strat_avancer=LigneStrat(self.superviseur,5)

            return v_tourner, omega_tourner

        else:
            #on actualise le vecteur rotation au cas ou on commencerait la
            #rotation le prochain tour

            self.strat_tourner=TournerGaucheStrat(self.superviseur,30)
            self.reset= True

        return v_avancer,omega_avancer



class ApprochStrat():
    """on fait s'approcher le robot d'un obstacle avec une marge passee en parametre
    """

    def __init__(self,superviseur,marge):

        self.superviseur = superviseur
        self.distance_obs = None
        self.strat_avancer = LigneStrat(self.superviseur,marge)


    def get_command(self):
        self.distance_obs = self.superviseur.robot.get_distance()
        if self.distance_obs > marge :
            return self.strat_avancer.get_command()
        else :
            return 0,0

class TournerDroiteStrat():
    """on fait tourner le robot vers la droite d'un degree passe en parametre en degree
    """

    def __init__(self,superviseur,angle):

        self.superviseur = superviseur
        self.distance_parcourue = 0
        self.distance_a_parcourir = (angle/360)*self.superviseur.robot.circonference

        #print("Angle={}, D a parcourir: {}/{}".format(angle, self.distance_a_parcourir, self.superviseur.robot.circonference))

    def get_command(self):
        self.distance_parcourue = (self.superviseur.robot.get_encoder()[0]*pi*self.superviseur.robot.rayonroue)/180
        #print("distance parcourue {}/{}".format(self.distance_parcourue, self.distance_a_parcourir))
        if abs(self.distance_parcourue) < self.distance_a_parcourir :
            return 0, -2
        else:
            return 0,0



class TournerGaucheStrat():
    """on fait tourner le robot vers la gauche d'un degree passe en parametre en degree
    """

    def __init__(self,superviseur,angle):

        self.superviseur = superviseur
        self.distance_parcourue = 0
        self.distance_a_parcourir = (angle/360)*self.superviseur.robot.circonference

    def get_command(self):
        self.distance_parcourue = (self.superviseur.robot.get_encoder()[1]*pi*self.superviseur.robot.rayonroue)/180
        #print("distance parcourue {}/{}".format(self.distance_parcourue, self.distance_a_parcourir))
        if abs(self.distance_parcourue) < self.distance_a_parcourir :
           return 0 ,2
        else:
           return 0,0
       
        
class TriangleStrat():
    
    def __init__(self,superviseur):
        
        self.superviseur = superviseur
        self.strat_avancer = LigneStrat(self.superviseur,10)
        self.strat_tourner= TournerGaucheStrat(self.superviseur,40)
        self.resest = True
        
    def get_command(self):
        
        v_avancer, omega_avancer = self.strat_avancer.get_command()

        if (v_avancer==0 and omega_avancer==0):
            #print([self.superviseur.robot.x,self.superviseur.robot.y])
            
            if (self.reset):    #on ne doit reinitialiser qu'une
                                #seule fois, sinon le robot tournera a l'infini
                self.superviseur.robot.reset_encoder()
                self.reset=False
           
            v_tourner, omega_tourner = self.strat_tourner.get_command()

            if (v_tourner==0 and omega_tourner==0):
                self.superviseur.robot.reset_encoder()
                self.strat_avancer=LigneStrat(self.superviseur,10)

            return v_tourner, omega_tourner

        else:
            print([self.superviseur.robot.x,self.superviseur.robot.y])
            #on actualise le vecteur rotation au cas ou on commencerait la
            #rotation le prochain tour

            self.strat_tourner=TournerGaucheStrat(self.superviseur,40)
            self.reset= True

        return v_avancer,omega_avancer
    
    
class PolygoneStrat():
    
    def __init__(self,superviseur,cotes):
        
        self.cotes = cotes
        self.angle = (360/self.cotes)/3
        self.superviseur = superviseur
        self.strat_avancer = LigneStrat(self.superviseur,30/self.cotes)
        self.strat_tourner= TournerGaucheStrat(self.superviseur,self.angle)
        self.resest = True
        
    def get_command(self):
        
        v_avancer, omega_avancer = self.strat_avancer.get_command()

        if (v_avancer==0 and omega_avancer==0):
            #print([self.superviseur.robot.x,self.superviseur.robot.y])
            
            if (self.reset):    #on ne doit reinitialiser qu'une
                                #seule fois, sinon le robot tournera a l'infini
                self.superviseur.robot.reset_encoder()
                self.reset=False
           
            v_tourner, omega_tourner = self.strat_tourner.get_command()

            if (v_tourner==0 and omega_tourner==0):
                self.superviseur.robot.reset_encoder()
                self.strat_avancer=LigneStrat(self.superviseur,30/self.cotes)

            return v_tourner, omega_tourner

        else:
            print([self.superviseur.robot.x,self.superviseur.robot.y])
            #on actualise le vecteur rotation au cas ou on commencerait la
            #rotation le prochain tour

            self.strat_tourner=TournerGaucheStrat(self.superviseur,self.angle)
            self.reset= True

        return v_avancer,omega_avancer
    
    
    
class TourStrat():
    
    def __init__(self,superviseur):
        
        self.superviseur = superviseur
        self.strat_tourner= TournerGaucheStrat(self.superviseur,30)
        self.strat_avancer1 = LigneStrat(self.superviseur,400)
        self.strat_avancer2 = LigneStrat(self.superviseur,800)
        self.etape = 1
        
    def get_command(self):
        
        v_avancer, omega_avancer = self.strat_avancer1.get_command()
        
        if self.etape==1:
            self.strat_avancer1.get_command()
            self.etape = 2
        
        if self.etape==2:
            self.strat_tourner.get_command()
            self.etape = 3
            
            

