'''
Created on 14 fevr. 2019

@author: Denis
'''

class Superviseur:
    
    def __init__(self, robot, strategie):
        """le superviseur sert d'intermediaire entre les controlleurs et le robot
        le superviseur prendra une strategie en argument et executera une etape
        a chaque appel de step.
        Il traduira aussi les commandes pour faire bouger le robot
        arguments : un robot, une strategie
        """
        self.robot = robot
        self.strategie = strategie
           
    def step(self,dt):
        
        v, omega = self.strategie.get_command()
        self.translate_command(v, omega)
        self.robot.step(dt)

    def translate_command(self,v,omega):
        
        v_droite, v_gauche = self.calcul_dps(v, omega)
        self.robot.set_dps(v_droite, v_gauche)
        
    def calcul_dps(self,v ,omega):
        
        v_droite = ((2*v)+(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        v_gauche = ((2*v)-(omega*self.robot.largeur))/ 2*self.robot.rayonroue
        
        return v_droite, v_gauche
    
    def redefine_strat(self,strategie):
        
        self.strategie= strategie
    