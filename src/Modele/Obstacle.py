#coding: utf-8
class Obstacle :

	def __init__ (self, *args) :
		""" 
		Fonction d'initialisation prenant en paramètre la longuer, la largeur et les coordonnées cartésiennes d'un obstacle rectangulaire
		"""
		if len(args)==3 :
			self.longueur = args[0]
			self.largeur = args[0]
			self.type = 'cercle'
			self.x = args[1]
			self.y = args[2]
		


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

