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

ma_fenetre=Fenetre(800,800) #a ne pas changer, ou alors reflechir a comment creer des constantes inter-fichiers

#on creer le robot
mon_robot=Robot(400,400, [1,1] ) #ne pas mettre 0,0 en direction initiale ou les fonctions tourner ne marcheront pas

#on creer son controlleur
controlleur = Controlleur(mon_robot)

#une premiere mise a jour avec la direction initiale
controlleur.update_coords_dir()

#on dessine le robot
triangle = ma_fenetre.fenetre.create_polygon(mon_robot.A,mon_robot.B,mon_robot.C)

#on creer les obstacles
dict_obstacles= Obstacle.create_and_disp_dict(ma_fenetre.fenetre, 100) # on stockera ces obstacles dans un dictionnaire avec comme cle le nom et comme valeur l'objet qu'on creer via tkinter
                                                            # note: le dictionnaire m'a semble etre le plus intuitif sur le coup, notamment 
                                                            # a cause du while dans la fonction check_obstacles du controlleur
                                                            # mais pourquoi pas essayer avec un tableau

    
""" test
    note: on obtient une erreur en fermant la fenetre mais c'est a cause du while
    car le programme n'est pas passe par mainloop, on essaiera de trouver un meilleur moyen de boucler
"""
while True:
    controlleur.avancer(ma_fenetre.fenetre, triangle, dict_obstacles)
    ma_fenetre.actualiser()
    time.sleep(0.01)    #notre dt


ma_fenetre.master.mainloop()
