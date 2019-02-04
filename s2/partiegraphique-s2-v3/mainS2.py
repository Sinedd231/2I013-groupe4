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

ma_fenetre=Fenetre(800,800)

#on creer le robot
mon_robot=Robot(400,400, [1,0] )

#on creer son controlleur
controlleur = Controlleur(mon_robot)

#une premiere mise a jour avec la direction initiale
controlleur.update_coords_dir()

#on dessine le robot
triangle = ma_fenetre.fenetre.create_polygon(mon_robot.A,mon_robot.B,mon_robot.C)

#on creer les obstacles
dict_obstacles= {}  #on stockera ces obstacles dans un dictionnaire avec comme cle le nom et comme valeur l'objet qu'on creer via tkinter
                    # note: le dictionnaire m'a semble etre le plus intuitif sur le coup, notamment a cause du while dans la fonction check_obstacles du controlleur
                    # mais pourquoi pas essayer avec un tableau

for i in range(1,7):
    obstacle= Obstacle(random.randint(0,600), random.randint(0,600), random.randint(15,50), random.randint(15,50))
    rectangle = ma_fenetre.fenetre.create_rectangle(obstacle.get_coords(), fill='red')
    dict_obstacles["obstacle" + str(i)] = rectangle #str convertit i de int vers string donc les noms seront "obstacle1" "obstacle2" etc...

    
""" test
    note: on obtient une erreur en fermant la fenetre mais c'est a cause du while
    car le programme n'est pas passe par mainloop, on essaiera de trouver un meilleur moyen de boucler
"""
while True:
    controlleur.avancer(ma_fenetre.fenetre, triangle, dict_obstacles)
    ma_fenetre.actualiser()
    time.sleep(0.01)    #notre dt


ma_fenetre.master.mainloop()
