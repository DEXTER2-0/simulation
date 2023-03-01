#coding: utf-8
import logging
class Obstacle :

	def __init__ (self, *args) :
		""" 
		Fonction d'initialisation prenant en paramètre:
			: 2 arguments : création un obstacle de type mur 
			: 3 arguments : création un obstacle de type cercle
			: 4 arguments : création un obstacle de type rectangle

		"""
		if (len(args)<2 |len(args)>4 ):
			if(len(args)<2):
				logging.debug("error : il faut au moins 2 arguments")
			else:
				logging.debug("error : il faut au plus 4 arguments")
		if len(args)==2 :
			self.longueur = -1 #permettre de dire que c'est un obstacle qui a le trou (ça pourrait être util pour simulation?)
			self.largeur = -1 #permettre de dire que c'est un obstacle qui a le trou (ça pourrait être util pour simulation?)
			self.x = range(args[0])
			self.y = range(args[1])
			self.type = 'mur'
		elif len(args)==3 :
			self.longueur = args[0]
			self.largeur = args[0]
			self.type = 'cercle'
			self.x = args[1]
			self.y = args[2]
		else :
			self.longueur = args[0]
			self.largeur = args[1]
			self.type = 'rectangle'
			self.x = args[2]
			self.y = args[3]
		

	def __str__ (self) : 
		"""
		Fonction de redefinition de la méthode print(Instance)
		"""
		if(self.type == 'mur'):
			res="le mur de ",len(self.longueur)," * ",len(self.largeur)," cm."
		else:
			res="Obstacle à la position : " + str(self.x) + " , "+ str(self.y) 
			if(self.type == 'cercle'):
				res+="  est un cercle de rayon " + str(self.rayon) + "  cm"
			else :
				if self.longueur == self.largeur :
					res+="  est un carré de longueur : "+ str(self.longueur)
				else : 
					res+=" est un rectangle de longueur : " + str(self.longueur) + "  et de largeur : " + str(self.largeur) 
		return res

