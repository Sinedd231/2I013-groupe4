'''
Created on 1 fevr. 2019

@author: Denis
'''

from Fenetre import *
from Robot import *
from Controlleur import *
import time, random
from Obstacle import *

#on creer la fenetre

ma_fenetre=Fenetre(900,900) #a ne pas changer, ou alors reflechir a comment creer des constantes inter-fichiers

#on creer les robots
mon_robot=Robot(400,400, [1,-1] ) #ne pas mettre 0,0 en direction initiale ou les fonctions tourner ne marcheront pas
mon_robot2= Robot(320,420, [0,1] )

#on creer leur controlleur
controlleur = Controlleur(mon_robot)
controlleur2 = Controlleur(mon_robot2)

#une premiere mise a jour avec la direction initiale
controlleur.update_coords_dir()
controlleur2.update_coords_dir()

#on dessine les robot
triangle = ma_fenetre.fenetre.create_polygon(mon_robot.A,mon_robot.B,mon_robot.C)
triangle2= ma_fenetre.fenetre.create_polygon(mon_robot2.A,mon_robot2.B,mon_robot2.C, fill='blue')

#on creer les obstacles, qui seront stocke dans un tableau et on realise l'affichage en meme temps
obstacles= Obstacle.create_and_disp_obstacle(ma_fenetre.fenetre, 20) 


for i in range(2000):
    controlleur.avancer(ma_fenetre.fenetre, triangle)
    controlleur2.avancer(ma_fenetre.fenetre, triangle2)
    ma_fenetre.actualiser()
    time.sleep(0.01)    #notre dt

print("FINI")
ma_fenetre.master.mainloop()
