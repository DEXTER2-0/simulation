from math import *
from Code.simulation import constantes as cs
from . import Traducteur
import time as time
from threading import Thread

class IA(Thread):
	def __init__(self,traducteur,list_ia,dt):
		super(IA, self).__init__()
		self.list_ia=list_ia
		self.dt = dt
		self.ia_actuel=-1
		self.trad=traducteur

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
	def __init__ (self,traducteur,d_voulue) :
		"""
		:param robot : Robot utilisé
		:param d_voulue : ditance voulue à effectuer en m
		"""
		self.trad=traducteur
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)
		self.arret=False	
		self.d=self.trad.resetdistance()
		self.d_voulue=d_voulue
		self.t0=0

	def start(self):
		"""
		"""
		self.t0=time.time()
		self.trad.setMotorDps(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
		self.fonctionne=True
		self.arret=False
		self.trad.calcul_v(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
		self.trad.calcul_new_orientation(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)

	def step(self):
		if self.arret:
			return
		if (self.d<self.d_voulue):
			self.dt=time.time()-self.t0
			self.d+=self.trad.getdistance(dt)
		else:
			self.stop()
	
	def stop(self):
		self.trad.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)

class IA_tourner:
	def __init__(self,traducteur,a_voulue) :
		"""
		:param robot : Robot utilisé
		"""
		self.trad=traducteur
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)
		self.arret=False
		self.a=self.trad.resetangle()
		self.a_voulu=a_voulue
		self.t0 = 0
	
	def start(self):
		"""
		:param a_voulu : angle voulu à effectuer en deg
		"""
		self.t0=time.time()
		self.trad.setMotorDps(cs.V_ANGULAIRE_G,-cs.V_ANGULAIRE_D)
		self.fonctionne=True
		self.arret=False
		self.trad.calcul_v(cs.V_ANGULAIRE_G,0)
		self.trad.calcul_new_orientation(cs.V_ANGULAIRE_G,0)
		

	def step(self):
		if self.arret:
			return
		if (self.a<=self.a_voulu):
			self.dt=time.time()-self.t0
			self.a+=self.trad.getangle(dt)
		else:
			self.stop()
			self.a=0
	
	def stop(self):
		self.trad.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)
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
		self.avancer.start()

	
	def step(self):
		if(self.robot.capteur<=self.d_evitement) and (self.tourner.arret):
			self.tourner.start()
		elif(self.robot.capteur<=self.d_evitement) and (self.tourner.fonctionne):
			self.tourner.step()
		elif(self.avancer.arret) and (self.tourner.arret):
			self.avancer.start()
		else:
			self.avancer.step()

	def stop(self):
		self.avancer.stop()
		self.tourner.stop()
		self.arret=True
