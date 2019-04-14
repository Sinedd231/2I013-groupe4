'''
Created on 19 fevr. 2019

@author: Denis
'''

import MVC.utiles.formules as fm


# fonctions issues de l'ancienne implementation, je sais pas encore si on les gardera vu qu'ils
# ne sont utilises nul part maintenant
def point_appartient_obstacle(p, obstacle):
        """
        prend en parametre un point p et un obstacle obst et renvoie true si p
        appartient a l'obstacle obst sinon renvoie false
        """
        
        if (((p[0] >= obstacle.x)and(p[0] <= obstacle.x1))and((p[1] >= obstacle.y)and(p[1] <= obstacle.y1))):
            return True
        else :
            return False
 

def point_est_obstacle(p, listeObst):
    """
    prend en parametre un point p et une liste d obstacle listeObst et renvoie true
    si p appartient a un des obstacles de la liste sinon renvoie false
    """
    for i in listeObst :
        if point_appartient_obstacle(p, i):
            return True
    return False


def ensemble_points_est_obstacle(P, listeObst):
    """
    prend en parametre un ensemble de point P et une liste d'obstacle et renvoie true si au moins un des points
    appartient a un obstacle de la liste listeObst sinon renvoie false
    """
    
    for p in P:
        if point_est_obstacle(p, listeObst):
            return True
    return False

#------------------------------------------------------------------------------------------------------------------------------------

# permet de determiner si oui ou non deux segments s'intersectent,
# l'algorithme a ete pris au hasard sur internet, ca a l'air de marcher mais je saurais pas expliquer
# il faudra s'y interesser plus tard pour comprendre precisement pourquoi ca marche


def intersection_segments(seg1, seg2):
    
    p1, r1 = seg1[0], fm.difference_vecteur(seg1[1], seg1[0])
    p2, r2 = seg2[0], fm.difference_vecteur(seg2[1], seg2[0])
    
    r1xr2 = fm.produit_vectoriel(r1, r2)
    if r1xr2 == 0:
        return False
    
    p2moinsp1 = fm.difference_vecteur(p2, p1)
    
    d1 = fm.produit_vectoriel(p2moinsp1, r2) / r1xr2
    d2 = fm.produit_vectoriel(p2moinsp1, r1) / r1xr2
    
    if d1 >= 0 and d1 <= 1 and d2 >= 0 and d2 <= 1:
        return True
    else:
        return False

# permet de determiner si oui ou non deux polygones s'intersectent
# algorithme naif qui consiste a tester chaque cote de polygone1 avec chaque cotes de polygones2
# si il y a intersection des cotes, c'est qu'il y a intersection des polygones
# on a pas des polygones tres complexes donc ca va encore, mais la complexite est mauvaise

def intersection_polygones(polygone1, polygone2):
    
    cotes1 = polygone1.getCotes()
    cotes2 = polygone2.getCotes()
    
    for cote1 in cotes1:
        for cote2 in cotes2:
            
            if intersection_segments(cote1, cote2):
                return True
    return False

# permet d'approximer le centre d'un polygone
# on fait la moyenne des vecteurs
def centre_polygone(polygone):
    
    n = len(polygone.getVecteurs())
    x = 0.0
    y = 0.0
    
    for vecteur in polygone.getVecteurs():
        x += vecteur[0]
        y += vecteur[1]
    
    x /= n
    y /= n
    return [ x, y]


# permet d'approximer un cercle circonscrit au polygone, en utilisant
# les resultats de centre_polygone
def cercle_circonscrit(polygone):
    
    centre = centre_polygone(polygone)
    rayon = 0.0
    
    for i in polygone.getVecteurs():
        d = fm.distance(centre, i)
        
        if d > rayon:
            rayon = d
    
    return centre, rayon


# on verifie si deux polygones sont proches l'un de l'autre en
# reflechissant sur leurs cercles circonscrits
def check_proximite(polygone1, polygone2):
    
    c1, r1 = cercle_circonscrit(polygone1)
    c2, r2 = cercle_circonscrit(polygone2)
    
    return fm.distance(c1, c2) <= r1 + r2

