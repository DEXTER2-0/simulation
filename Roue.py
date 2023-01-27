from math import pi

class Roue :
	def __init__ (self, taille_cm, vMaxTourParSec) :
		self.taille_cm = taille_cm
		self.vMaxTourParSec = vMaxTourParSec
		self.vTourParSec = 0

	def __str__ (self) :
		"""
		Equivalent methode toString(Java)
		Permet de redéfinir la methode print(monInstance)
		""" 
		res = "Roue de taille " + str(self.taille_cm) + " cm"
		
		if self.vTourParSec == 0: # Si la roue est à l'arret
			res += " est à l'arret" 

		else : # Si la roue tourne
			res += " roule à " + str(self.vTourParSec) + "tour/seconde"
		return res
	
	def setVitesse(self,vitesseVoulue_kmh) :
		"""
		Formule de conversion de la vitesse v en km/h en vitesse de rotation n en tr/s :
		N=(25*v)/(3*60*pi*rayon_en_metre)
		"""
		vVoulueTourParSec= (25*vitesseVoulue_kmh/(3*pi*self.taille_cm*0.01))/60

		if (vVoulueTourParSec<=self.vMaxTourParSec):# Si la vitesse est possible pour la roue 
			self.vTourParSec=vVoulueTourParSec

		else : # Si la vitesse voulue est plus grande que la vitesse maximale possible
			self.vTourParSec=self.vMaxTourParSec
			print("La vitesse voulue est trop grande, les roues tournent à leur vitesse maximale")

		return self.vTourParSec

