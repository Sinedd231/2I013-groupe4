'''
Created on 1 fevr. 2019

@author: Denis
'''
from tkinter import *

class fenetre:
    """Cette classe permet de creer une fenetre canvas et de l'afficher"""
    
    def __init__(self,master,largeur,hauteur):  #le constructeur aura besoin d'un master sur lequel baser la fenetre, d'une largeur et d'une hauteur
        self.fenetre= Canvas(master, width=largeur, height=hauteur, bg="white") #fond de couleur blanc, choisie arbitrairement
        self.master=master
        self.master.title("Fenetre")
        self.fenetre.pack()
        
    def actualiser(self):       #permet d'actualiser l'image
        self.master.update()    #note : peut etre inutile, a voir si on le garde