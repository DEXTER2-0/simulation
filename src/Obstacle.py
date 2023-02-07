#coding: utf-8
class Obstacle :

	def __init__ (self, longueur , largeur , x , y) :
		""" 
		Fonction d'initialisation prenant en paramètre la longuer, la largeur et les coordonnées cartésiennes d'un obstacle rectangulaire
		"""
		self.longueur=longueur
		self.largeur=largeur
		self.x=x
		self.y=y
	
	def __init__ (self, rayon,x,y) :
	                 """ 
			   Fonction d'initialisation prenant en paramètre le rayon et les coordonnées cartésiennes d'un obstacle circulaire 
			   """
	                self.rayon=rayon
		        self.x=x
		        self.y=y
	def __str__ (self) : 
		"""
		Fonction de redefinition de la méthode print(Instance)
		"""

		res="Obstacle à la position : " + str(self.x) + " , "+ str(self.y) 
		if hasattr(self , 'rayon') : #si l'obstacle est un cercle 
			res+="  est un cercle de rayon " + str(self.rayon) + "  cm"
		else :
			if self.longueur == self.largeur :
				res+="  est un carré de longueur : "+ str(self.longueur)
			else : 
				res+=" est un rectangle de longueur : " + str(self.longueur) + "  et de largeur : " + str(self.largeur) 
		return res

