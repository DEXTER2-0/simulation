from Module import Robot
from Module import Obstacle
from math import *
from TestScript import constantes as cs

class IA_avancer :
	def __init__ (self, robot, v=0, w=0) :
		"""
		:param robot : Robot utilisé
		"""
		self.robot = robot
		self.v=v #vitesse moyenne du robot initialisé a 0
		self.w=w #angle à ajouter à l'angle au temps t-1
		
#	def est_entrain_de_rouler(robot) :
#		"""
#		Fonction testant la vitesse des roues afin de retourner un booléen corresponsant à si le robot roule ou non
#		"""
#		if robot.roue_droite.vTourParSec==0 and robot.roue_gauche.vTourParSec==0 :
#			return False
#		else :
#			return True
	
	def arreter_urgence(self):		
		"""
		Fonction arretant le robot en mettant la vitesses des roues à 0 d'un coup
		"""
		self.robot.roue_gauche.setVitesse(0)
		self.robot.roue_droite.setVitesse(0)
	
	def arreter(self):
		"""
		Fonction arretant le robot par décélération jusqu'à l'arrêt
		"""
		self.decelerer(0)

	def bouger(self, ANG_G, ANG_D):
		"""
		cette methode suppose que les deux roues possede le meme rayon
		ANG_G prend une vitesse angulaire pour la roue gauche
		ANG_D prend une vitesse angulaire pour la roue droite
		"""	
		# vitesse moyenn du robot
		self.v = (self.robot.roue_gauche.taille_cm*0.01/2)*(ANG_D + ANG_G)	
		#angle de rotation du robot en fonction des vitesses des roues
		self.w = (self.robot.roue_gauche.taille_cm*0.01/(self.robot.l*0.01))*(ANG_D - ANG_G)
		#Donne l'information aux roues de la vitesse en rad/seconde de la vitesse qu'elles doivent avoir
		self.robot.roue_gauche.vTourParSec = ANG_G
		self.robot.roue_droite.vTourParSec = ANG_D

	#def nouvelle_position2(self, duree):
		#"""
		#Doit etre appelé apres la methode bouger() pour pouvoir mettre a jours les 
		#coordonées du robot ainsi que son angle d'orientation
		#"""
		#self.pos_x = self.pos_x + self.v * cos(self.angle)*duree
		#self.pos_y = self.pos_y + self.v * sin(self.angle)*duree
		#self.angle = self.angle + self.w * duree

	def evite(self):
		"""
		Permet d'eviter un obstacle
		Pour le moment uniquement orientation de pi/2 
		tourne de pi/2
		Appele bouger avec les vitesse nécessaire pour faire la rotation
		"""
		self.bouger(0,(pi*self.robot.l)/(2*self.robot.roue_droite.taille_cm*0.01))
##-------------------------------------------------------
	
#	def avancer(self,vitesseVoulue_kmh_er,vitesseVoulue_kmh_et) :
#		"""
#		Fonction prenant en paramètre la vitesse voulue en km/h projetée sur l'axe er et la vitesse voulue en km/h projetée sur l'axe et
#		puis vérifiant que les vitesses permettent d'avancer (>0) afin de calculer la vitesse voulue en km/h
#		et de la transmettre aux roues
#		"""
#		assert(vitesseVoulue_kmh_er > 0)
#		assert(vitesseVoulue_kmh_et > 0)
#		self.vitesse_er=vitesseVoulue_kmh_er
#		self.vitesse_et=vitesseVoulue_kmh_et
#		vitesseVoulue_kmh=np.sqrt(vitesseVoulue_kmh_er**2+vitesseVoulue_kmh_et**2)
#		self.accelerer(vitesseVoulue_kmh)
#		#print("le robot avance à une vitesse ", vitesseVoulue_kmh)	
#	def reculer(self,vitesseVoulue_kmh_er,vitesseVoulue_kmh_et) :
#		"""
#		Fonction prenant en paramètre la vitesse voulue en km/h projetée sur l'axe er et la vitesse voulue en km/h projetée sur l'axe et
#		puis vérifiant que les vitesses permettent d'avancer (<0) afin de calculer la vitesse voulue en km/h
#		et de la transmettre aux roues
#		"""
#		assert(vitesseVoulue_kmh_er < 0)
#		assert(vitesseVoulue_kmh_et < 0)
#		self.vitesse_er=vitesseVoulue_kmh_er
#		self.vitesse_et=vitesseVoulue_kmh_et
#		vitesseVoulue_kmh=-(np.sqrt(vitesseVoulue_kmh_er**2+vitesseVoulue_kmh_et**2))
#		self.accelerer(vitesseVoulue_kmh)
#		#print("le robot recule à une vitesse de ",vitesseVoulue_kmh)	
#	def tourner(self,angleEnRad,tempsDonneEnSec):
#		"""
#		Fonction prenant en paramètre l'angle en rad que le robot doit effectuer et le temps qu'il a pour faire cette rotation
#		commençant par arrêter le robot puis calculant la vitesse angulaire et la vitesse en km/h de cette rotation
#		avant de tester si l'angle est positif, dans ce cas la vitesse est transmise à la roue gauche pour tourner à droite, 
#		ou négatif, dans ce cas la vitesse est transmise à la roue droite pour tourner à gauche
#		"""
#		self.arreter_urgence()
#		vitesseAng = angleEnRad/tempsDonneEnSec
#		vitessekmh = 3.6*self.roue_droite.taille_cm*(10**(-2))*vitesseAng
#		if(angleEnRad<0):
#			self.roue_droite.setVitesse(vitessekmh)
#			self.roue_gauche.setVitesse(0)
#		#	print("le robot tourne vers la gauche d'un angle de : ", angleEnRad)
#		if(angleEnRad>0):
#			self.roue_droite.setVitesse(0)
#			self.roue_gauche.setVitesse(vitessekmh)
#		#	print("le robot tourne vers la droite d'un angle de :  " ,angleEnRad)	
		


	def accelerer(self,vitesseVoule):
		"""
		:param vitesseVoulue : vitesse du robot en km/h voulue
		puis transmets des vitesses aux roues par pas de 0,1 km/h tant que la vitesse voulue n'est pas atteinte
		"""	
		#assert(self.roue_gauche.vTourParSec==self.roue_droite.vTourParSec)
		assert(self.roue_gauche.vTourParSec != 0)
		assert(self.roue_gauche.vTourParSec==self.roue_gauche.vTourParSec)
	#	print(self.roue_gauche.vTourParSec)	
		vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
		print(self.roue_gauche.vTourParSec)
		if (self.roue_gauche.vTourParSec > 0) :
				vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
		else :
				vitesse_actuelle = 0
		"""while(vitesse_actuelle <= vitesseVoule):
					self.roue_gauche.setVitesse(vitesse_actuelle+1)
				self.roue_gauche.setVitesse(vitesse_actuelle+1)
				vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)	"""
	#	print("le robot roule à la vitesse voulue apres acceleration :  " , vitesse_actuelle)	
	def decelerer(self,vitesseVoule):
		"""
		:param vitesseVoulue : vitesse du robot en km/h voulue
		puis transmets des vitesses aux roues par pas de 0,1 km/h tant que la vitesse voulue n'est pas atteinte
		"""
		assert(self.roue_gauche.vTourParSec>0)
		vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
		while(vitesse_actuelle >= vitesseVoule):
			self.roue_gauche.setVitesse(vitesse_actuelle-1)
			self.roue_gauche.setVitesse(vitesse_actuelle-1)
			vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)	
	
	# def conversion_polaire_vers_cartesienne(self):
		# 	"""
		# 	Fait la conversion de donnée polaire en donnees cartesienne
		#     """
		# 	pos_x = self.r * np.cos(self.angle)
		# 	pos_y = self.r * np.sin(self.angle)
		# 	return pos_x, pos_y	
		# def conversion_cartesienne_vers_polaire(self):	
		# 	""" convertit les coordonnées cartesiennes en coordonnées polaires """
		# 	r=np.sqrt((self.pos_x * self.pos_x) + (self.pos_y * self.pos_y))
		# 	o=2*math.atan(self.pos_y / (self.pos_x + r))
		# 	return r,
		# def conversion_polaire_vers_cartesienne(self):
		# 	"""
		# 	Fonction faisant la conversion des coordonnées polaires en coordonées cartésiennes
		# 	formules utilisées : x=r*cos(theta) et y=r*sin(theta)
		# 	"""
		# 	pos_x = self.r * np.cos(self.angle)
		# 	pos_y = self.r * np.sin(self.angle)
		# 	return pos_x, pos_y	
		# def conversion_cartesienne_vers_polaire(self):
		# 	"""
		# 	Fonction faisant la conversion des coordonnées cartésiennes en coordonées polaires
		# 	formules utilisées : r=(x²+y²)^(1/2) et theta=arctan(y/x)
		# 	"""
		# 	r = np.sqrt(self.pos_x**2 + self.pos_y**2)
		# 	angle= np.arctan(self.pos_y/self.pos_x)
		# 	return r, angle
	def nouvelle_position4(self, vitesse_er, vitesse_et,orientation, duree):
		"""
		Renvoie la distance parcourue (m), pour une vitesse (km)
		et une durée (s)
		Augmente la distance si vitesse est supérieur a zero
		Diminue la distance sinon
		"""
		self.r+=vitesse_er*duree
		self.angle+=vitesse_et*duree/self.r
		print("Le robot a avancé et est maintenant à la position : x=",self.conversion_polaire_vers_cartesienne()[0]," y=",self.conversion_polaire_vers_cartesienne()[1])		
	def nouvelle_position5(self,duree):
		"""
		Fonction prenant en paramètre la durée en s depuis le calcul de la dernière position
		puis calcul le nouveau r et le nouvel angle
		formules utilisées : r+=vitesse projetée sur l'axe er*t et theta+=vitesse projetée sur l'axe et*t/r
		"""
		self.r+=self.vitesse_er*duree
		self.angle+=self.vitesse_et*duree/self.r
		val = self.conversion_polaire_vers_cartesienne()
		self.pos_x = val[0]
		self.pos_y = val[1]	
	def evite_obstacles2(self,Obstacle):
		"""
		Fonction prenant en paramètre l'obstacle et si la distance captée par le capteur entre le robot et l'obstacle est 
		inférieure à 10 cm, alors le robot effectue une rotation d'un quart de tour vers la gauche
		"""
		val=np.pi/2
		if(self.capteurDistance.distance(self,Obstacle) < 10):
			self.tourner(val,1)
			print("le robot a évité l'obstacle")
		else :
			print("pas de danger , no worries")	

	#def __str__ (self) :	
	#	"""
	#	Fonction de redéfinition de la methode print(monInstance)
	#	"""
	#	res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")" +" angle = "+str(self.angle)
	#
	#	# Le test suivant permet de faire un affichage du robot selon s'il roule ou pas#
	#	
	#	return res
