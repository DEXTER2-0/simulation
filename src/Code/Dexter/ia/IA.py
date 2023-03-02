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
	def __init__ (self,robot,IA_avancer,IA_tourner) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.avancer=IA_avancer
		self.tourner=IA_tourner
	
	def start(self,d_evitement):
		"""
		:param d_evitement : distance voulue entre l'obstacle et le robot lors de l'évitement
		"""
		self.d_evitement=d_evitement
		self.avancer.start()
