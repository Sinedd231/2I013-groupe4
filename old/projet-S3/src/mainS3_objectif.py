'''
@author: Alexandre
@test: Denis
'''

from fenetre import *
from robot import *
from controlleur import *
import time
from obstacle import *
from objectif import *


#on creer la fenetre

ma_fenetre=Fenetre(900,900) #a ne pas changer, ou alors reflechir a comment creer des constantes inter-fichiers

#on creer les robots
mon_robot=Robot("robocop",400,400, [1,0] ) #ne pas mettre 0,0 en direction initiale ou les fonctions tourner ne marcheront pas

#on creer leur controlleur
controlleur = Controlleur(mon_robot)

#on dessine les robot
triangle = mon_robot.disp_robot(ma_fenetre.fenetre, None)

#on dessine les capteurs (NOTE: les capteurs ont ete crees en meme temps que les robots)
ligne=mon_robot.capteur.disp_capteur(ma_fenetre.fenetre)

#on creer les obstacles, qui seront stocke dans un dictionnaire et on realise l'affichage en meme temps
obstacles= Obstacle.create_and_disp_obstacle(ma_fenetre.fenetre, 10)

objectif= Objectif.create_and_disp_objectif(ma_fenetre.fenetre) #NOTE: objectif est un 2uplet compose de l'objet reel objectif et d'un objet tkinter
controlleur.tourner_vers_objectif(objectif[0])

while controlleur.pause==False:
    
    controlleur.avancer(ma_fenetre.fenetre, triangle, ligne, obstacles)
    ma_fenetre.actualiser()
    time.sleep(0.01)
        
          
print("FINI")
ma_fenetre.master.mainloop()