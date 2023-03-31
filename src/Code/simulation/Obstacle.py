class Obstacle :

	def __init__ (self, args, type, pos) :
		""" 
		Fonction d'initialisation prenant en parametre:
			: type : si type = 0 c'est un mur 
						type = 1 c'est un cercle
						type = 2 c'est un rectangle 
			: pos  : positon de l'obstacle (une liste de 2 éléments ) 
			: args : pour definir la longueur et largeur
		"""
		self.pos = pos
		self.type = type 
		if type == 0 :
			self.end = args 
		elif type == 1 :
			self.rayon = args
		else :
			self.longueur = args[0]
			self.largeur = args[1]

	