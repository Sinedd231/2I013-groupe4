"""@author : Denis
"""

from math import sqrt
import random

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
	
	
	@staticmethod
	def create_dict(canvas,nbr):
		""" permet de creer un dictionnaire d'obstacles qu'on retournera par la suite
			la fonction prendra en argument un canvas qui permettra de creer les obstacles et 'nbr' pour nombre d'obstacles voulu
			j'ai passe la fonction en static pour enlever le self et faciliter l'appel dans le main
		"""
		
		dictionnaire=dict()
			
		for i in range(1,nbr+1):
			
			obstacle= Obstacle(random.uniform(*random.choice( [(0,310),(430,720)] )), random.uniform(0,720), random.uniform(15,50), random.uniform(15,50))
			""" petite astuce pour eviter le probleme de l'obstacle qui spawn sur le robot, on va juste empecher la creation d'obstacle
			sur l'intervalle ]310,430[ de l'axe x, la ou notre robot se trouvera
			on va donc selectionner au hasard l'intervalle [0,310] ou [430,720] avec random.choice, ce qui exclut l'intervalle ]310,430[
			note: * devant random.choice car on renverra une liste en argument pour random.uniform, c'est le langage qui veut ca
			"""
			
			rectangle = canvas.create_rectangle(obstacle.get_coords(), fill='red')
			
			if not(len(canvas.find_overlapping(canvas.coords(rectangle)[0], canvas.coords(rectangle)[1], canvas.coords(rectangle)[2], canvas.coords(rectangle)[3]))>1):
			#voir les explications sur find overlapping dans Controlleur.py
				dictionnaire["obstacle" + str(i)] = rectangle 	#str convertit i de int vers string donc les noms seront "obstacle1" "obstacle2" etc...
			else:
				canvas.delete(rectangle)
			#en gros je supprime les doublons, c'est a dire les obstacles qui se chevauchent
		
		return dictionnaire
			
