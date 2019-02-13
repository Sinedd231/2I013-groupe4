"""@author : Alexandre
@test : Denis
"""
import random

class Objectif :
    
    def __init__(self,x,y,r):
        """l'objectif sera represente par un cercle
        le constructeur prendra un point xy, et un rayon"""
        
        self.x = x
        self.y = y
        self.r = r

    
    
    @staticmethod
    def create_and_disp_objectif(canvas):
        """similaire a create_and_disp_obstacle, on donne en parametre un canvas pour realiser l'affichage
        la fonction retourne l'objet reel objectif ET l'objet tkinter cercle, pour pouvoir garder un controle sur le dessin
        """
        
        while True:
            objectif=Objectif(random.uniform(0,900),random.uniform(0,900),10)
            cercle = canvas.create_oval(objectif.x-objectif.r, objectif.y-objectif.r, objectif.x+objectif.r, objectif.y+objectif.r,fill='green')
            
            if len(canvas.find_overlapping(canvas.coords(cercle)[0], canvas.coords(cercle)[1], canvas.coords(cercle)[2], canvas.coords(cercle)[3]))>1:
                canvas.delete(cercle)
            else:
                break
            
        return objectif,cercle
