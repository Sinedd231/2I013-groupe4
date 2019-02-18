'''
Created on 18 févr. 2019

@author: Denis
'''

from tkinter import *
HAUTEUR = 900
LARGEUR = 900

class Viewer():
    
    def __init__(self, simulateur):
        
        self.simulateur= simulateur
        self.master = Tk()  # racine de l'interface
        self.fenetre = Canvas(self.master, width=LARGEUR, height=HAUTEUR, bg="white")  # fond de couleur blanc, choisie arbitrairement
        self.master.title("DAAMS")
        self.fenetre.pack()  # permet d'afficher la fenetre
        
    def actualiser(self):  # permet d'actualiser l'image
        self.master.update()
    
    
        
        