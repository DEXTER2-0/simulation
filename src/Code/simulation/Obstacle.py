import logging
class Obstacle :

	def __init__ (self, *args) :
		""" 
		Fonction d'initialisation prenant en paramètre:
			: 2 arguments : création un obstacle de type mur 
			: 3 arguments : création un obstacle de type cercle
			: 4 arguments : création un obstacle de type rectangle
		"""
		if (len(args)<3 |len(args)>4 ):
			if(len(args)<3):
				logging.debug("error : il faut au moins 3 arguments")
			else:
				logging.debug("error : il faut au plus 4 arguments")
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
	