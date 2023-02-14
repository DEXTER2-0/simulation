#coding: utf-8
class Obstacle :

	def __init__ (self, *args) :
		""" 
		Fonction d'initialisation prenant en paramètre la longuer, la largeur et les coordonnées cartésiennes d'un obstacle rectangulaire
		"""
		if (len(args)<2 |len(args)>4 ):
			if(len(args)<2):
				print("error : il faut au moins 2 arguments")
			else:
				print("error : il faut au plus 4 arguments")
			return 0
		if len(args)==2 :
			self.x = range(args[0])
			self.y = range(args[1])
			self.type = 'mur'
		if len(args)==3 :
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

