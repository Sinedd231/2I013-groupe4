'''
Created on 14 févr. 2019

@author: Denis
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


def rotation_degree(a, angle):
    """retourne a partir d'un vecteur a, un nouveau vecteur issu de la rotation d'un angle 'angle' en degree"""
    
    a0 = a[0] * cos(radians(angle)) - a[1] * sin(radians(angle))
    a1 = a[0] * sin(radians(angle)) + a[1] * cos(radians(angle))

    return [ a0, a1 ]


def scale(a, scalaire):
    """retourne le produit entre un vecteur et un scalaire"""
    
    return [ scalaire * a[0], scalaire * a[1] ]


def rotation_vecteur(a, angle):
    """retourne a partir d'un vecteur a, un nouveau vecteur issu de la rotation d'un angle 'angle' en radians"""
    
    a0 = a[0] * cos(angle) - a[1] * sin(angle)
    a1 = a[0] * sin(angle) + a[1] * cos(angle)

    return [ a0, a1 ]


def rotation_vecteurs(alist,angle):
    """applique rotation_vecteur a une liste de vecteur alist
    retourne un tableau de vecteurs
    """
    
    res=[]
    for a in alist:
        res.append(rotation_vecteur(a, angle))
    
    return res

def rotation_et_somme_vec(a, angle, b):
    """retourne un vecteur issu de la rotation de a de angle radians puis de la somme avec le vecteur b"""
    
    return somme_vecteur(rotation_vecteur(a, angle), b)


def rotation_et_somme_vecs(alist, angle, b):
    """applique rotation_et_somme_vec a une liste de vecteur alist
    retourne un tableau de vecteurs
    """
    
    res=[]
    for a in rotation_vecteurs(alist, angle):
        res.append(somme_vecteur(a, b))
    
    return res

def normalise_angle(angle):
    """permet de normaliser 'angle' pour qu'il reste dans [-pi, pi] """
    
    return atan2(sin(angle),cos(angle))


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
