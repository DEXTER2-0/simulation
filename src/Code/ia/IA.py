#from Code.simulation.Robot import Robot
#from simulation import Obstacle
from math import *
from Code.simulation import constantes as cs
import time as time
from threading import Thread

class IA(Thread):
	def __init__(self, robot,list_ia,dt):
		super(IA, self).__init__()
		self.list_ia=list_ia
		self.dt = dt
		self.ia_actuel=-1
		self.robot=robot

	def run(self):
		self.encours = True
		while self.encours:   #tant qu'on run 
			self._lastTime = time.time()    # on sauvegarde l'instant du run 
			time.sleep(self.dt)     #on fait un sleep de dt afin de calculer l'intervalle de temps
			self._ITemps = time.time() - self._lastTime   #on calcule l'intervalle de temps 
			self.step() #on met à jour la simulation 
           
	def step(self):
		""" met à jour la simulation selon le temps écoulé """
		if self.list_ia[self.ia_actuel].arret:
			self.ia_actuel+=1
			if self.ia_actuel>= 0 and self.ia_actuel <len(self.list_ia):
				self.list_ia[self.ia_actuel].stop()
			if self.ia_actuel>=len(self.list_ia):
				self.ia_actuel=0
				self.encours=False
				return
			self.list_ia[self.ia_actuel].start()
			
		else:
			self.list_ia[self.ia_actuel].step()
			



class IA_avancer :
	def __init__ (self, robot,d_voulue) :
		"""
		:param robot : Robot utilisé
		:param d_voulue : ditance voulue à effectuer en m
		"""
		self.robot = robot
		self.v=0
		self.new_orientation=0
		self.arret=False	
		self.d=0
		self.d_voulue=d_voulue
		self.t0=0
	def start(self):
		"""
		"""
		self.t0=time.time()
		self.d=0
		self.robot.setMotorDps(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
		self.fonctionne=True
		self.arret=False
		self.robot.v=(cs.RAYON_DES_ROUES_CM/2)*(cs.V_ANGULAIRE_G+cs.V_ANGULAIRE_D)
		self.robot.new_orientation=(cs.RAYON_DES_ROUES_CM/cs.RAYON_ROBOT_CM)*(cs.V_ANGULAIRE_G-cs.V_ANGULAIRE_D)

	def step(self):
		if self.arret:
			return
		if (self.d<self.d_voulue):
			self.dt=time.time()-self.t0
			self.d+=self.dt*cs.V_ANGULAIRE_G*cs.RAYON_ROBOT_CM*360 #vitesse convertie en m/s
		else:
			self.stop()
	
	def stop(self):
		self.robot.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.robot.v=0
		self.robot.new_orientation=0

class IA_tourner:
	def __init__(self, robot,a_voulue) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.robot.v=0
		self.robot.new_orientation=0
		self.arret=False
		self.a=0
		self.a_voulu=a_voulue
		self.t0 = 0
	
	def start(self):
		"""
		:param a_voulu : angle voulu à effectuer en deg
		"""
		self.t0=time.time()
		self.a=0
		self.robot.setMotorDps(cs.V_ANGULAIRE_G,0)
		self.fonctionne=True
		self.arret=False
		self.robot.v=(cs.RAYON_DES_ROUES_CM/2)*(cs.V_ANGULAIRE_G+0)
		self.robot.new_orientation=(cs.RAYON_DES_ROUES_CM/cs.RAYON_ROBOT_CM)*(cs.V_ANGULAIRE_G-0)
		

	def step(self):
		if self.arret:
			return
		if (self.a<self.a_voulu):
			self.dt=time.time()-self.t0
			self.a+=self.dt*cs.V_ANGULAIRE_G
		else:
			self.stop()
	
	def stop(self):
		self.robot.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.robot.v=0
		self.robot.new_orientation=0
		self.arret=True

class IA_eviter:
	def __init__ (self,robot,IA_avancer,IA_tourner,d_evitement) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.avancer=IA_avancer
		self.tourner=IA_tourner
		self.arret=False
		self.d_evitement=d_evitement

	
	def start(self):
		"""
		:param d_evitement : distance voulue entre l'obstacle et le robot lors de l'évitement
		"""
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
		self.arret=True


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
