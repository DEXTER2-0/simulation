import pygame

class Obstacle :
	def __init__ (self, type, pos,args) :
		""" 
		Fonction d'initialisation prenant en parametre:
			: type : si type = 0 c'est un mur 
						type = 1 c'est un cercle
						type = 2 c'est un rectangle 
			: pos  : positon de l'obstacle (une liste de 2 elements ) 
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

	def draw(self,disp,couleur):
		if self.type == 0 :
			pygame.draw.line(disp,couleur ,self.pos, self.end)
		elif self.type == 1 :
			pygame.draw.circle(disp,couleur ,self.pos, self.rayon)
		else:
			pygame.draw.rect(disp, couleur, (self.pos, (self.longueur, self.largeur)))
	