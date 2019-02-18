'''
Created on 1 fevr. 2019

@author: Denis
'''
from tkinter import *

class fenetre:
    """Cette classe permet de creer une fenetre canvas et de l'afficher"""
    
    def __init__(self,largeur,hauteur):  #le constructeur aura d'une largeur et d'une hauteur
        self.master=Tk()    #racine de l'interface
        self.fenetre= Canvas(self.master, width=largeur, height=hauteur, bg="white") #fond de couleur blanc, choisie arbitrairement
        self.master.title("Fenetre")
        self.fenetre.pack()
        
    def actualiser(self):       #permet d'actualiser l'image
        self.master.update()    