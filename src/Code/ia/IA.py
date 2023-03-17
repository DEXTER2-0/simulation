#from Code.simulation.Robot import Robot
#from simulation import Obstacle
from math import *
from Code.simulation import constantes as cs
import time
from threading import Thread

class IA(Thread):
	def __init__(self, list_ia):
		super(IA, self).__init__()
		self.list_ia=list_ia




class IA_avancer :
	def __init__ (self, robot) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.v=0
		self.new_orientation=0
	
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
		self.robot.v=cs.RAYON_DES_ROUES/2*(cs.V_ANGULAIRE_G+cs.V_ANGULAIRE_D)
		self.robot.new_orientation=cs.RAYON_DES_ROUES/cs.RAYON_ROBOT_CM*(cs.V_ANGULAIRE_G-cs.V_ANGULAIRE_D)

	def step(self):
		if self.arret:
			return
		if (self.d<self.d_voulue):
			duree=time()-self.t0
			self.d+=duree*cs.V_ANGULAIRE_G*cs.RAYON_ROBOT_CM*360 #vitesse convertie en m/s
		else:
			self.stop()
	
	def stop(self):
		self.robot.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.robot.v=0
		self.robot.new_orientation=0

class IA_tourner:
	def __init__(self, robot) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.robot.v=0
		self.robot.new_orientation=0
	
	def start(self,a_voulu):
		"""
		:param a_voulu : angle voulu à effectuer en deg
		"""
		self.t0=time()
		self.a=0
		self.a_voulu=a_voulu
		self.robot.setMotorDps(cs.V_ANGULAIRE_G,0)
		self.fonctionne=True
		self.arret=False
		self.robot.v=cs.RAYON_DES_ROUES/2*(cs.V_ANGULAIRE_G+0)
		self.robot.new_orientation=cs.RAYON_DES_ROUES/cs.RAYON_ROBOT_CM*(cs.V_ANGULAIRE_G-0)
		

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
		self.robot.v=0
		self.robot.new_orientation=0

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
		self.avancer.start(cs.WIDTH)
	
	def step(self):
		if(self.robot.capteur<=self.d_evitement) and (self.tourner.arret):
			self.tourner.start(pi/2)
		elif(self.robot.capteur<=self.d_evitement) and (self.tourner.fonctionne):
			self.tourner.step()
		elif(self.avancer.arret) and (self.tourner.arret):
			self.avancer.start(cs.WIDTH)
		else:
			self.avancer.step()

	def stop(self):
		self.avancer.stop()
		self.tourner.stop()


class IA_carre:
	def __init__ (self,robot,IA_avancer,IA_tourner) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.avancer=IA_avancer
		self.tourner=IA_tourner
	
	def start(self,d_cote):
		"""
		:param d_cote : longueur s'un côté du carré en m
		"""
		self.cote=d_cote
		self.avancer.start(self.cote)
		self.cpta=1 #compteur de cêtés faits
		self.cptt=0 #compteur d'angles effectués
	
	def step(self):
		if self.cpta<=4:
			if self.avancer.arret and self.cptt<self.cpta:
				self.tourner.start(90)
				self.cptt+=1
			elif self.tourner.fonctionne:
				self.tourner.step()
			elif self.tourner.arret and self.avancer.arret:
				self.avancer.start(self.cote)
				self.cpta+=1
			elif self.avancer.fonctionne:
				self.avancer.step()
		else:
			self.stop

	def stop(self):
		self.avancer.stop()
		self.tourner.stop()
