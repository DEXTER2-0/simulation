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
		self.robot.setMotorDps(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
		self.fonctionne=True
		self.arret=False
	
	def step(self):
		if self.arret:
			return
		if (self.d<self.d_voulue):
			duree=time()-self.t0
			self.d+=duree*cs.V_ANGULAIRE_G*cs.RAYON_ROBOT_CM #vitesse convertie en m/s
		else:
			self.stop()
	
	def stop(self):
		self.robot.setMotorDps(0,0)
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
		:param a_voulu : angle voulu à effectuer en rad
		"""
		self.t0=time()
		self.a=0
		self.a_voulu=a_voulu
		self.robot.setMotorDps(cs.V_ANGULAIRE_G,0)
		self.fonctionne=True
		self.arret=False

	def step(self):
		if self.arret:
			return
		if (self.a<self.a_voulu):
			duree=time()-self.t0
			self.a+=duree*cs.V_ANGULAIRE_G
		else:
			self.stop()
	
	def stop(self):
		self.robot.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True

class IA_eviter:
	def __init__ (self, robot) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot

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
