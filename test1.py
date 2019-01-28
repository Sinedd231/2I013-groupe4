'''
Created on 28 janv. 2019

@author: Denis
'''

from tkinter import *

#petit code pour tester l'affichage et le deplacement d'un robot represente sous forme d'un triangle isocele avec comme tete le sommet


#code pour l'affichage

root = Tk() #on initialise la racine de l'interface

root.title("Fenetre test 1") #le titre de la fenetre graphique

Width=500
Height=600
canvas = Canvas(root, width=Width, height=Height, bg="white") #on creer la fenetre

canvas.pack() #on l'affiche

#coordonnees du triangle
x0=Width/2
y0=Height/2
x1=x0-20
y1=y0+20
x2=x0+20
y2=y1

robot1= canvas.create_polygon(x0,y0,x1,y1,x2,y2)    #notre robot

#code pour le deplacement

#deplacement relatif du robot
dx=0
dy=-1   #donc vers le haut

def deplacement():
    global dx, dy
    
    ox,oy = [Width/2, 100]  #point objectif que le robot cherchera a atteindre, avec ox la coordonnee en x et oy la coordonnee en y, ici l'objectif sera en (250,100)
    if canvas.coords(robot1)[1]<0:  #si la coordonnee y du sommet atteint le bord de la fenetre, alors son dy change de sens
        dy=-dy
    
    canvas.move(robot1,dx,dy)
    if canvas.coords(robot1)[0]!=ox or canvas.coords(robot1)[1]!=oy:    #si il n'a pas atteint l'objectif alors on fait un appel recursif apres 20 millisecondes
        root.after(20,deplacement)


#on lance la fonction
deplacement()

#on boucle pour garder l'affichage sur l'ecran
root.mainloop()

