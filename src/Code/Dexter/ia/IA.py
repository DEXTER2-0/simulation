from Dexter import Robot
from Dexter import Obstacle
from math import *
import constantes as cs
import time


class IA_avancer :
	def __init__ (self, robot) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
	
	def start(self,d_voulue):
		"""
		:param d_voulue : ditance voulue à effectuer en m
		"""
		self.t0=time()
		self.d=0
		self.d_voulue=d_voulue
		self.robot. #méthode de contrôle de la vitesse des roues
		self.fonctionne=True
		self.arret=False
	
	def step(self):
		if self.arret:
			return
		if (self.d<self.d_voulue):
			duree=time()-self.t0
			self.d+=duree* #vitesse convertie en m/s
		else:
			self.stop()
	
	def stop(self):
		self.robot. #méthode de contrôle de la vitesse des roues appelée avec 0 comme vitesse
		self.fonctionne=False
		self.arret=True

class IA_tourner:
	def __init__(self, robot) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
	
	def start(self,a_voulu):
		"""
		:param a_voulu : angle voulu à effectuer en 
		"""
		self.t0=time()
		self.a=0
		self.a_voulu=a_voulu
		self.robot. #méthode de contrôle de la vitesse des roues
		self.fonctionne=True
		self.arret=False

	def step(self):
		if self.arret:
			return
		if (self.a<self.a_voulu):
			duree=time()-self.t0
			self.a+=duree* #vitesse angulaire
		else:
			self.stop()
	
	def stop(self):
		self.robot. #méthode de contrôle de la vitesse des roues appelée avec 0 comme vitesse
		self.fonctionne=False
		self.arret=True

class IAEvite:

	def __init__ (self, robot, v=0, w=0) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.v=v #vitesse moyenne du robot initialisé a 0
		self.w=w #angle à ajouter à l'angle au temps t-1


	def setVitesseRobot(self, ANG_G, ANG_D):
		"""
		cette methode suppose que les deux roues possede le meme rayon
		ANG_G prend une vitesse angulaire pour la roue gauche
		ANG_D prend une vitesse angulaire pour la roue droite
		"""	
		# vitesse moyenn du robot
		self.v = (self.robot.roue_gauche.taille_cm*0.01/2)*(ANG_D + ANG_G)	
		#angle de rotation du robot en fonction des vitesses des roues
		self.w = (self.robot.roue_gauche.taille_cm*0.01/(self.robot.l*0.01))*(ANG_D - ANG_G)
		self.robot.setMotorDps(ANG_D,ANG_D)


	def evite(self):
		"""
		Permet d'eviter un obstacle
		Pour le moment uniquement orientation de pi/2 
		tourne de pi/2
		Appele bouger avec les vitesse nécessaire pour faire la rotation
		"""
		self.setVitesseRobot(0,(pi*self.robot.l)/(2*self.robot.roue_droite.taille_cm*0.01))

	def arreter_urgence(self):		
		"""
		Fonction arretant le robot en mettant la vitesses des roues à 0 d'un coup
		"""
		self.robot.roue_gauche.setVitesse(0)
		self.robot.roue_droite.setVitesse(0)
	
	
	
	


	#def accelerer(self,vitesseVoule):
	#	"""
	#	:param vitesseVoulue : vitesse du robot en km/h voulue
	#	puis transmets des vitesses aux roues par pas de 0,1 km/h tant que la vitesse voulue n'est pas atteinte
	#	"""	
	#	#assert(self.roue_gauche.vTourParSec==self.roue_droite.vTourParSec)
	#	assert(self.roue_gauche.vTourParSec != 0)
	#	assert(self.roue_gauche.vTourParSec==self.roue_gauche.vTourParSec)
	##	print(self.roue_gauche.vTourParSec)	
	#	vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
	#	print(self.roue_gauche.vTourParSec)
	#	if (self.roue_gauche.vTourParSec > 0) :
	#			vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
	#	else :
	#			vitesse_actuelle = 0
	#	"""while(vitesse_actuelle <= vitesseVoule):
	#				self.roue_gauche.setVitesse(vitesse_actuelle+1)
	#			self.roue_gauche.setVitesse(vitesse_actuelle+1)
	#			vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)	"""
