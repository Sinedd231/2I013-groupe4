'''
Created on 18 févr. 2019

@author: Denis
'''

from tkinter import *
HAUTEUR = 900
LARGEUR = 900


class Viewer():
    """cette classe permet de gerer la fenetre tkinter en tant que telle
    l'affichage des elements de la simulation se fera dans world_view
    """
    
    def __init__(self, simulateur):
        
        self.simulateur = simulateur  # pas sur de l'utilite de lier le simulateur et le viewer comme 
                                        # le veut la structure de base des MVC dans notre cas
        self.master = Tk()  # racine de l'interface
        self.fenetre = Canvas(self.master, width=LARGEUR, height=HAUTEUR, bg="white")  # fond de couleur blanc, choisie arbitrairement
        self.master.title("DAAMS")
        
    def actualiser(self):  # permet d'actualiser l'image
        self.master.update()
        
    def afficher(self):  # permet d'afficher la bonne fenetre
        self.fenetre.pack()
