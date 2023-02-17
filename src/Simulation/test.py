#!/usr/bin/python
import time as t #pour pouvoir controler le temps de la boucle while True
import numpy as np
import math as m
# -*- coding: latin-1 -*
class Capteur_de_distance :
    def __init__(self, distanceCaptable) :
       """
       Fonction d'initialisation prenant en paramètre la distance maximale captable possible
       """
       self.distanceCaptable=distanceCaptable
    
    
    def distance(self,x,y,obstacle):
        """
        Fonction prenant en paramètre le robot et l'obstacle afin de calculer leur distance 
        (racine carrée des carré des différences entre les positions selon x et selon y) et la retourner.
        """
        xr = x
        yr = y
        xo = obstacle.x
        yo = obstacle.y
        return m.sqrt((xo-xr)**2+(yo-yr)**2)

    def senseur_de_distance(self,ia_pos_x,ia_pos_y,angle_robot,le_pas,l_obstacle):
        """
        Aide page 16 du td2
        Suppose que la liste d'obstacle sont des cercles
        l_obstacle : est une liste d'obstacle
        ia.pos_y et ia.pos_y : permettent de récuperer les coordonnée actuelles du robot
        angle : permet au capteur de savoir dans quelle direction lancer le laser
        le_pas : permet de couper en plusieurs morceaux la distance avant de rencontrer un obstacle 
        """
        k=0
        x = ia_pos_x
        y = ia_pos_y
        #print("Distance Captable = ",self.distanceCaptable)
        while k*le_pas < self.distanceCaptable :
            x = x + m.cos(angle_robot) * le_pas #Lance le laser dans la bonne direction
            y = y + m.sin(angle_robot) * le_pas #Lance le laser dans la bonne direction
            ##print("capteur -> (",x,",",y,")") 
            # Verification si les coordonées du laser se trouve dans un obstacle(cercle)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                
                # Si a un moment le laser se trouve dans un obstacle
                if (self.distance(x,y,obstacle)) < obstacle.longueur: #obstacle.longueur car dans obstacle attribut longueur m¨
                    ###print("obstacle à : ", sqrt((x-ia_pos_x)**2+(y-ia_pos_y)**2))
                    return m.sqrt((x-ia_pos_x)**2+(y-ia_pos_y)**2)
            k +=1
        ###print("Rien à l'horizon")
        return self.distanceCaptable


#coding: utf-8
class Obstacle :

	def __init__ (self, *args) :
		""" 
		Fonction d'initialisation prenant en paramètre:
			: 2 arguments : création un obstacle de type mur 
			: 3 arguments : création un obstacle de type cercle
			: 4 arguments : création un obstacle de type rectangle

		"""
		if (len(args)<2 |len(args)>4 ):
			if(len(args)<2):
				print("error : il faut au moins 2 arguments")
			else:
				print("error : il faut au plus 4 arguments")
		if len(args)==2 :
			self.longueur = -1 #permettre de dire que c'est un obstacle qui a le trou (ça pourrait être util pour simulation?)
			self.largeur = -1 #permettre de dire que c'est un obstacle qui a le trou (ça pourrait être util pour simulation?)
			self.x = range(args[0])
			self.y = range(args[1])
			self.type = 'mur'
		elif len(args)==3 :
			self.longueur = args[0]
			self.largeur = args[0]
			self.type = 'cercle'
			self.x = args[1]
			self.y = args[2]
		else :
			self.longueur = args[0]
			self.largeur = args[1]
			self.type = 'rectangle'
			self.x = args[2]
			self.y = args[3]
		

	def __str__ (self) : 
		"""
		Fonction de redefinition de la méthode print(Instance)
		"""
		if(self.type == 'mur'):
			res="le mur de ",len(self.longueur)," * ",len(self.largeur)," cm."
		else:
			res="Obstacle à la position : " + str(self.x) + " , "+ str(self.y) 
			if(self.type == 'cercle'):
				res+="  est un cercle de rayon " + str(self.rayon) + "  cm"
			else :
				if self.longueur == self.largeur :
					res+="  est un carré de longueur : "+ str(self.longueur)
				else : 
					res+=" est un rectangle de longueur : " + str(self.longueur) + "  et de largeur : " + str(self.largeur) 
		return res
class Roue :
	def __init__ (self, taille_cm, vMaxTourParSec) :
		"""
		Fonction d'initialisation prenant en paramètre le rayon en cm et la vitesse maximale possible pour les roues
		"""
		self.taille_cm = taille_cm
		self.vMaxTourParSec = vMaxTourParSec
		self.vTourParSec = 0

	def __str__ (self) :
		"""
		Fonction de redéfinition de la methode print(monInstance)
		""" 
		res = "Roue de taille " + str(self.taille_cm) + " cm"
		if self.vTourParSec == 0: # Si la roue est à l'arret
			res += " est à l'arret" 

		else : # Si la roue tourne
			res += " roule à " + str(self.vTourParSec) + "tour/seconde"
		return res
	
	def setVitesse(self,vitesseVoulue_kmh) :
		"""
		Formule prenant en paramètre la vitesse voulue en km/h et calculant sa converion en vitesse de rotation n en tr/s et la retourne
		puis donnant évaluant si la vitesse demandée est possible et de donner soit cette vitesse soit la vitesse maximale aux roues
		formule de conversion utilisée : N=(5*v)/(36*pi*rayon_en_metre)
		"""
		#print("la vitesse de la roue était de:  ",self.vTourParSec)
		vVoulueTourParSec= (5*vitesseVoulue_kmh)/(36*m.pi*self.taille_cm*0.01)
		if (vVoulueTourParSec<=self.vMaxTourParSec):# Si la vitesse est possible pour la roue 
			self.vTourParSec=vVoulueTourParSec

		else : # Si la vitesse voulue est plus grande que la vitesse maximale possible
			self.vTourParSec=self.vMaxTourParSec
		#print("la nouvelle vitesse de la roue est de:  ",self.vTourParSec)

		return self.vTourParSec
	

class Robot :
	def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteur,vMaxTourParSec,l=1) :
		"""
		Fonction d'initialisation prenant en paramètre le rayon des roues en cm, le rayon du robot en cm,
		la distance maximale captable par le capteur de distance, la vitesse maximale possible pour les roues,
		les coordonnées polaires et les coordonnées cartésiennes du robot
		Cette fonction instancie deux roues de la même taille et de même vitesse maximale, ainsi qu'un capteur de position
		"""
		assert(rayonRouesCm > 0)# Ne peut pas avoir un rayon < 0
		assert(vMaxTourParSec > 0) # Ne peut pavoir une vitesse max < 0
		assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
		self.roue_gauche = Roue(rayonRouesCm, vMaxTourParSec)
		self.roue_droite = Roue(rayonRouesCm, vMaxTourParSec)
		self.capteurDistance = Capteur_de_distance(capteur)
		self.rayonDuRobotCm = rayonDuRobotCm
		#self.pos_x = pos_x
		#self.pos_y = pos_y
        #self.robot = robot
		#self.r=r
        #self.angle = angle
		# l = 2*rayon du robot
		self.l=l*2*rayonDuRobotCm	




class Terrain:
        def __init__ (self, WIDTH_MIN, WIDTH_MAX, HEIGHT_MIN, HEIGHT_MAX,liste_obstacle) :
            self.WIDTH_MIN = WIDTH_MIN
            self.WIDTH_MAX = WIDTH_MAX
            self.HEIGHT_MIN = HEIGHT_MIN
            self.HEIGHT_MAX = HEIGHT_MAX
            self.liste_obstacle = liste_obstacle

RAYON_DES_ROUES_CM=1 #en cm
VITESSE_MAX_TOUR_PAR_SEC=30 #en km/h
RAYON_ROBOT_CM=10 #en cm
WIDTH = 600 # axe des x
HEIGHT = 600 # axe des y
V_ANGULAIRE_G = 250.17
V_ANGULAIRE_D = 250
DISTANCE_MIN_ARRET = 7#en metre



class IA :
	def __init__ (self, robot,r=0,angle = 0, pos_x = 0, pos_y = 0, v=0, w=0) :
		"""
		"""
		self.r=r
		self.angle = angle
		#self.vitesse_er 
		#self.vitesse_et
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.robot = robot
		self.v=v #vitesse moyenne du robot initialisé a 0
		self.w=w #angle à ajouter à l'angle au temps t-1
		
	def est_entrain_de_rouler(robot) :
		"""
		Fonction testant la vitesse des roues afin de retourner un booléen corresponsant à si le robot roule ou non
		"""
		if robot.roue_droite.vTourParSec==0 and robot.roue_gauche.vTourParSec==0 :
			return False
		else :
			return True
	
	def arreter_urgence(self):		
		"""
		Fonction arretant le robot en mettant la vitesses des roues à 0 d'un coup
		"""
		self.roue_gauche.setVitesse(0)
		self.roue_droite.setVitesse(0)
	
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

	def nouvelle_position2(self, duree):
		"""
		Doit etre appelé apres la methode bouger() pour pouvoir mettre a jours les 
		coordonées du robot ainsi que son angle d'orientation
		"""
		self.pos_x = self.pos_x + self.v * m.cos(self.angle)*duree
		self.pos_y = self.pos_y + self.v * m.sin(self.angle)*duree
		self.angle = self.angle + self.w * duree

	def evite(self):
		"""
		Permet d'eviter un obstacle
		Pour le moment uniquement orientation de pi/2 
		tourne de pi/2
		Appele bouger avec les vitesse nécessaire pour faire la rotation
		"""
		self.bouger(0,(m.pi*self.robot.l*0.01)/(2*self.robot.roue_droite.taille_cm*0.01))

	#def faire_carre(self):


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
		Fonction prenant en paramètre la vitesse à atteindre en km/h
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
		Fonction prenant en paramètre la vitesse à atteindre en km/h
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
	# def nouvelle_position4(self, vitesse_er, vitesse_et,orientation, duree):
	# 	"""
	# 	Renvoie la distance parcourue (m), pour une vitesse (km)
	# 	et une durée (s)
	# 	Augmente la distance si vitesse est supérieur a zero
	# 	Diminue la distance sinon
	# 	"""
	# 	self.r+=vitesse_er*duree
	# 	self.angle+=vitesse_et*duree/self.r
	# 	print("Le robot a avancé et est maintenant à la position : x=",self.conversion_polaire_vers_cartesienne()[0]," y=",self.conversion_polaire_vers_cartesienne()[1])		
	#def nouvelle_position5(self,duree):
	#	"""
		# Fonction prenant en paramètre la durée en s depuis le calcul de la dernière position
		# puis calcul le nouveau r et le nouvel angle
		# formules utilisées : r+=vitesse projetée sur l'axe er*t et theta+=vitesse projetée sur l'axe et*t/r
		# """
		# self.r+=self.vitesse_er*duree
		# self.angle+=self.vitesse_et*duree/self.r
		# val = self.conversion_polaire_vers_cartesienne()
		# self.pos_x = val[0]
		# self.pos_y = val[1]	
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

	def __str__ (self) :	
		"""
		Fonction de redéfinition de la methode print(monInstance)
		"""
		res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")" +" angle = "+str(self.angle)

		# Le test suivant permet de faire un affichage du robot selon s'il roule ou pas#
		
		return res

class Simulation :
    def __init__ (self, ia, robot, terrain, duree_boucle) :
        """
        """
        #self.mur_x = range(10) 
        #self.mur_y = range(10)
        self.ia = ia
        self.robot = robot
        self.terrain = terrain
        self.duree_boucle = duree_boucle
        #self.obs1 = Obstacle(6,2,2)
        #self.obs2 = Obstacle(3,4,7)
        
    
    def collision(self):
        for obstacle in self.terrain.liste_obstacles: #pour chaque obstacle
            d=np.sqrt((self.ia.robot.x-obstacle.x)**2+(self.ia.robot.y-obstacle.y)**2) #distance euclidienne entre le robot et l'obstacle
            if(d<=(self.ia.robot.rayon)): # collision de deux cercles
                self.ia.robot.arreter_urgence()
            elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
                self.ia.robot.arret_urgence()
	    
    
    def update_simulation(self):
        distance = self.robot.capteurDistance.senseur_de_distance(self.ia.pos_x, self.ia.pos_y, self.ia.angle, 0.5, self.terrain.liste_obstacle)
        if distance > DISTANCE_MIN_ARRET:
            self.ia.bouger(V_ANGULAIRE_G,V_ANGULAIRE_D)
            self.ia.nouvelle_position2(self.duree_boucle)
            t.sleep(1)
            print(self.ia)
        else :
            self.ia.evite()
            self.ia.nouvelle_position2(self.duree_boucle)

    #def update_simulation(self):
    #    self.ia.evite()
    #    self.ia.nouvelle_position2(self.duree_boucle)
    #    print(self.ia)
        
              
            #print("obstacle à ",distance ,"mettre ARRET !!")
    

    #def simul(self):
    #    i=0
    #    t=
    #    self.ia.robot.bouger(vr,vl)
    #    while (i<t):
    #        for i in self.terrain.liste_obstacle:
    #            self.ia.robot.eviter(i)
    #        self.collision()
    #        i+=0.1
    #self.robot.arret()

#Initialisation du Robot
robot = Robot(RAYON_DES_ROUES_CM, RAYON_ROBOT_CM, 15,VITESSE_MAX_TOUR_PAR_SEC)

#Initilaisation de l'IA
ia = IA(robot)

#Initialisation d'une liste d'obstacle
obstacle1 = Obstacle(1,30,0)
obstacle2 = Obstacle(2,0,4)
obstacle3 = Obstacle(3,220,1)
obstacle4 = Obstacle(1,15,15)
liste_obstacle = []
liste_obstacle.append(obstacle1)
liste_obstacle.append(obstacle2)
liste_obstacle.append(obstacle3)
liste_obstacle.append(obstacle4)

#Initialisation d'un terrain
terrain = Terrain(0,WIDTH,0,HEIGHT, liste_obstacle)



simulation = Simulation(ia,robot,terrain,1)

while True :
    simulation.update_simulation()
    #simulation.update_carre()
    

