'''
Created on 19 févr. 2019

@author: Denis
'''
from .obstacle import Obstacle
from .objectif import Objectif
import random
from MVC.view.viewer import HAUTEUR, LARGEUR
from MVC.utiles import geometrie as geo


class MapBuilder:
    """cette classe nous permettra de construire les obstacles et l'objectif
    """

    def __init__(self):
        pass
    
    def build_random(self, world):
        """construit un monde tout aleatoirement, on pourra definir d'autre fonctions qui le feront
        de maniere predefinie
        """
        # on genere l'objectif
        goal = Objectif(random.uniform(0, LARGEUR), random.uniform(0, HAUTEUR))
        
        world.define_goal(goal)  # on donne l'objectif a world pour qu'il le transmette a world view
        
        # on genere les obstacles
        for i in range(random.randint(0, 1)):
            obstacle = Obstacle(random.uniform(0, LARGEUR),
                                random.uniform(0, HAUTEUR),
                                random.uniform(15, 50),
                                random.uniform(15, 50))
            
            # on verifie que l'obstacle cree ne chevauche pas les robots ou l'objectif
            for elem in world.espace_reserve():
                    intersecte = geo.intersection_polygones(elem, obstacle)
                    if intersecte:
                        break

            if not intersecte:
                world.add_obstacle(obstacle)
        
            