#coding: utf-8
class Obstacle :
	def __init__ (self, rayon,x,y) :
		""" permet de créer des obstacles cerculaires de rayon rayon et a la position de coordonnées x et y """
		self.rayon=rayon
		self.x=x
		self.y=y

	
	def __init__ (self, longueur , largeur , x , y) :
		""" permet de créer des obstacles rectangulaires de longueur longueur et de largeur largeur a la position x , y , possibilité de créer des carrés aussi """
		self.longueur=longueur
		self.largeur=largeur
		self.x=x
		self.y=y

	def __str__ (self) : 
		""" redefinition de la méthode print(Instance)"""

		res="Obstacle à la position : " + str(self.x) + " , "+ str(self.y) 
		if hasattr(self , 'rayon') : #si l'obstacle est un cercle 
			res+="  est un cercle de rayon " + str(self.rayon) + "  cm"
		else :
			if self.longueur == self.largeur :
				res+="  est un carré de longueur : "+ str(self.longueur)
			else : 
				res+=" est un rectangle de longueur : " + str(self.longueur) + "  et de largeur : " + str(self.largeur) 

