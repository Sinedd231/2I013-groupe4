'''
Created on 1 fevr. 2019

@author: Denis
'''

from fenetre import *
from Robot import *
from controlleur import *
import time

#on creer la fenetre

ma_fenetre=fenetre(800,800)

#on creer le robot
mon_robot=Robot(400,400, [1,1] )

#on creer son controlleur
controlleur = Controlleur(mon_robot)

#une premiere mise a jour avec la direction initiale
controlleur.update_coords_dir()

#on dessine le robot
triangle = ma_fenetre.fenetre.create_polygon(mon_robot.A,mon_robot.B,mon_robot.C)

"""test"""
while True:
    controlleur.avancer(ma_fenetre.fenetre, triangle)
    ma_fenetre.fenetre.coords(triangle, mon_robot.A[0],mon_robot.A[1],mon_robot.B[0],mon_robot.B[1], mon_robot.C[0], mon_robot.C[1])
    ma_fenetre.actualiser()
    time.sleep(0.01)    #notre dt


ma_fenetre.master.mainloop()
