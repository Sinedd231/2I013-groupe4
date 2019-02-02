'''
Created on 1 fevr. 2019

@author: Denis
'''
from tkinter import *
from fenetre import *
from Robot import *
from tourner import *
from controlleur import *

#on creer la fenetre
root= Tk()
ma_fenetre=fenetre(root, 800,800)

#on creer le robot
mon_robot=Robot(400,400, (10,25) )

#on creer son controlleur
controlleur = Controlleur(mon_robot)

#un premier coup de mise a jour avec la direction initiale
controlleur.update_coords_dir()

#on dessine le robot
triangle = ma_fenetre.fenetre.create_polygon(mon_robot.A,mon_robot.B,mon_robot.C)


angle=0
def test():
    """petit test pour les fonctions de rotation et d'actualisation"""
    
    global angle
    
    tourner_degree(mon_robot, angle)    #rotation puis mise a jour
    controlleur.update_coords_dir()
    
    ma_fenetre.fenetre.coords(triangle, mon_robot.A[0],mon_robot.A[1],mon_robot.B[0],mon_robot.B[1],mon_robot.C[0],mon_robot.C[1]) #application des changements
    
    angle += 1
    root.after(80,test)


test()
root.mainloop()
