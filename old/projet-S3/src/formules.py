'''
Created on 7 fevr. 2019

@author: Denis, Alexandre
'''

"""fichier qui regroupe toutes les formules et fonctions utiles pour les autres classes"""

from math import *


def somme_vecteur(a, b):
    """retourne la somme vectorielle de a et b"""
    
    return [a[0] + b[0], a[1] + b[1]]


def difference_vecteur(a, b):
    """retourne la difference de deux vecteurs a et b"""
    
    return [a[0] - b[0], a[1] - b[1]]


def produit_scalaire(a, b):
    """retourne le produit scalaire de deux vecteurs a et b"""
    
    return a[0] * b[0] + a[1] * b[1]


def produit_vectoriel(a, b):
    """retourne le produit vectoriel de deux vecteurs a et b"""
    
    return a[0] * b[1] - a[1] * b[0]


def norme_vecteur(a):
    """retourne la norme du vecteur a"""
    
    return sqrt(a[0] ** 2 + a[1] ** 2)


def rotation_vecteur(a, angle):
    """retourne a partir d'un vecteur a, un nouveau vecteur issu de la rotation d'un angle 'angle' en radians"""
    
    a0 = a[0] * cos(angle) - a[1] * sin(angle)
    a1 = a[0] * sin(angle) + a[1] * cos(angle)

    return [ a0, a1 ]


def rotation_degree(a, angle):
    """retourne a partir d'un vecteur a, un nouveau vecteur issu de la rotation d'un angle 'angle' en degree"""
    
    a0 = a[0] * cos(radians(angle)) - a[1] * sin(radians(angle))
    a1 = a[0] * sin(radians(angle)) + a[1] * cos(radians(angle))

    return [ a0, a1 ]


def scale(a, scalaire):
    """retourne le produit entre un vecteur et un scalaire"""
    
    return [ scalaire * a[0], scalaire * a[1] ]


def convertir_direction_angle(a, b):
    """retourne l'angle en radians correspondant a la direction (a,b) du robot"""
        
    return atan2(a, b)


def tourner_point(ox, oy, angle, P):
    """ retourne un nouveau point qui est la rotation du point P autour d'un point d'origine O (ox,oy) de 'angle' radians
    puisque les points du triangle sont stockes sous forme de tableau, ici on retourne alors un tableau
    """
    
    return [ cos(angle) * (P[0] - ox) - sin(angle) * (P[1] - oy) + ox , sin(angle) * (P[0] - ox) + cos(angle) * (P[1] - oy) + oy ]


def signe_determinant (u, v):
    """
    prend en parametre 2 vecteur et renvoie le signe du determinant de la
    matrice composee par ces 2 vecteurs
    """
    if (u[0] * v[1] - u[1] * v[0]) > 0:
        return 1
    if (u[0] * v[1] - u[1] * v[0]) < 0:
        return -1

    
def angle_entre_vecteurs(u, v):
    """
    prend en parametre 2 vecteur et renvoie l'angle oriente entre les 2 vecteurs
    en radiants 
    """
    return signe_determinant(u, v) * (acos((produit_scalaire(u, v)) / (norme_vecteur(u) * norme_vecteur(v))))


def point_appartient_obstacle(p, obst):
        """
        prend en parametre un point p et un obstacle obst et renvoie true si p
        appartient a l'obstacle obst sinon renvoie false
        """
        
        if (((p[0] >= obst.x)and(p[0] <= obst.x1))and((p[1] >= obst.y)and(p[1] <= obst.y1))):
            return True
        else :
            return False
 

def point_est_obstacle(p, listeObst):
    """
    prend en parametre un point p et une liste d obstacle listeObst et renvoie true
    si p appartient a un des obstacles de la liste sinon renvoie false
    """
    for i in listeObst :
        if point_appartient_obstacle(p, i) == True:
            return True
    return False


def ensemble_points_est_obstacle(P, listeObst):
    """
    prend en parametre un ensemble de point P et une liste d'obstacle et renvoie true si au moins un des points
    appartient a un obstacle de la liste listeObst sinon renvoie false
    """
    
    for p in P:
        if point_est_obstacle(p, listeObst) == True:
            return True
    return False



def points_segment(a, b):
    """retourne 10 points du segment ab sous forme de tableau, avec un pas de 0.1"""
    # le nombre de point et le pas est fixe actuellement, meme si toutes les combinaisons sont possibles,
    # un plus grand nombre de points avec un pas plus petit rendrait le programme actuel vraiment trop lourd en calcul
    # il faudrait d'abord optimiser le code ailleurs avant d'augmenter ici 
    
    res = []  # tableau resultat
    t = 0  # coefficient qui nous permettra de calculer un point precis, NOTE: 0<= t <=1
    
    for i in range(0, 10):
        p = ((1 - t) * a[0] + t * b[0], (1 - t) * a[1] + t * b[1])
        res.append(p)
        t += 0.1
    
    return res

