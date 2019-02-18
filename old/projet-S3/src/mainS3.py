'''
Created on 11 févr. 2019

@author: Denis
'''

from fenetre import *
from robot import *
from controlleur import *
import time
from obstacle import *


#on creer la fenetre

ma_fenetre=Fenetre(900,900) #a ne pas changer, ou alors reflechir a comment creer des constantes inter-fichiers

#on creer les robots
mon_robot=Robot("robocop",400,400, [1,0] ) #ne pas mettre 0,0 en direction initiale ou les fonctions tourner ne marcheront pas
mon_robot2= Robot("astroboy",320,420, [-1,1] )

#on creer leur controlleur
controlleur = Controlleur(mon_robot)
controlleur2 = Controlleur(mon_robot2)

#on dessine les robot
triangle = mon_robot.disp_robot(ma_fenetre.fenetre, None)
triangle2= mon_robot2.disp_robot(ma_fenetre.fenetre, 'blue')

#on dessine les capteurs (NOTE: les capteurs ont ete crees en meme temps que les robots)
ligne=mon_robot.capteur.disp_capteur(ma_fenetre.fenetre)
ligne2=mon_robot2.capteur.disp_capteur(ma_fenetre.fenetre)

#on creer les obstacles, qui seront stocke dans un dictionnaire et on realise l'affichage en meme temps
obstacles= Obstacle.create_and_disp_obstacle(ma_fenetre.fenetre, 200) 


while controlleur.pause==False or controlleur2.pause==False:
    controlleur.avancer(ma_fenetre.fenetre, triangle, ligne, obstacles)
    controlleur2.avancer(ma_fenetre.fenetre, triangle2, ligne2, obstacles)
    ma_fenetre.actualiser()
    time.sleep(0.01)
        
          
print("FINI")
ma_fenetre.master.mainloop()