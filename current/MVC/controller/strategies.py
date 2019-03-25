'''
Created on 5 mars 2019

@author: Denis
'''


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
        self.superviseur.robot.reset_encoder()

    def get_command(self):

        #si on a pas atteint la distance fixee
        if (self.distance < self.distancemax):
            self.distance+= self.superviseur.robot.get_encoder()[0]*self.superviseur.robot.rayonroue
            return self.superviseur.robot.vmax, 0
        else:
            return 0,0


#on met de cote cette strategie la en attendant de l'adapter pour le reel

#class GoalStrat():
#    """on se dirige vers l'objectif donne en parametre, quoi qu'il arrive
#    """

    #def __init__(self,superviseur,goal):
        
    #    self.superviseur=superviseur
    #    self.goal=goal
        
    #def get_command(self):
         


class Turn90Strat():
    """on tourne de 90 degrees
    """

    def __init__(self,superviseur):

        self.superviseur=superviseur
        self.superviseur.robot.reset_encoder()
        self.angle_parcouru=0

    def get_command(self):

        if (self.angle_parcouru < 82):  #on a une imprecision de 8 degrees dans la simulation et 
                                        #il faut 82 degrees pour en faire 90, la source du probleme
                                        #doit encore etre trouvee
            self.angle_parcouru += self.superviseur.robot.get_encoder()[0]
            print(self.angle_parcouru)
            return 0,10
        else:
            return 0,0

class SquareStrat():
    """on fait dessiner un carre au robot
    """

    def __init__(self,superviseur):

        self.superviseur= superviseur

        #on a besoin de sous strategies ici
        self.strat_avancer = LigneStrat(self.superviseur,5)
        self.strat_tourner= Turn90Strat(self.superviseur)

    def get_command(self):
        #on fait alterner les sous strategies et on
        #base notre raisonnement sur leurs reponses respectives,
        #si une sous strategie renvoie 0,0 on passe a la sous strategie
        #suivante

        v_avancer, omega_avancer = self.strat_avancer.get_command()

        if (v_avancer==0 and omega_avancer==0):
            v_tourner, omega_tourner = self.strat_tourner.get_command()

            if (v_tourner==0 and omega_tourner==0):
                self.strat_avancer=LigneStrat(self.superviseur,5)

            return v_tourner, omega_tourner

        else:
            #on actualise le vecteur rotation au cas ou on commencerait la
            #rotation le prochain tour

            self.strat_tourner=Turn90Strat(self.superviseur)

        return v_avancer,omega_avancer
