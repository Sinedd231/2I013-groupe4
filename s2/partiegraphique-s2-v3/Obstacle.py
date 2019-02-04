"""@author : Denis
"""

from math import sqrt

class Obstacle:
	"""permet de construire les obstacles pour notre robot"""
	
	
	def __init__(self, x,y, largeur, hauteur):
		""" les obstacles seront rectangulaires
			on a besoin de x,y qui sera ici le coin en haut a gauche, d'une hauteur et d'une largeur
		"""
		
		self.x = x
		self.y = y
		self.largeur = largeur
		self.hauteur = hauteur
	
	def get_coords(self):
		""" sur tkinter il faut 2 points pour dessiner un rectangle
			le coin en haut a gauche, donc xy chez nous, et le coin en bas a droite
			on doit donc determiner le coin en bas a droite, puis on renverra les 4
			coordonnees
		"""
			
		x0 = self.x
		y0 = self.y
		
		x1 = x0+ sqrt(self.largeur**2 + self.hauteur**2)	#longueur de la diagonale = racine de (hauteur^2 + largeur^2)
		y1 = y0+ self.hauteur
		
		return x0,y0,x1,y1