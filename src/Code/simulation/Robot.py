from Code.simulation import constantes as cs
from math import pi,sqrt,sin,cos

class Robot :
	def __init__ (self, rayonRouesCm,rayonDuRobotCm,vMaxDegParSec,distance_captable,l=1) :
		"""
		:param rayonRouesCm : rayon des roues en cm
		:param rayonDuRobotCm : rayon du cercle dans lequel s'inscrit le robot en cm
		:param capteur : Capteur utilise
		:param vMaxRadParSec : vitesse maximale possible pour les roues en rad/s
        :param distance_captable : distance maximale que le capteur peut calculer
		Cette fonction instancie deux roues de la meme taille et de meme vitesse maximale, ainsi qu'un capteur de position
		"""
		assert(rayonRouesCm > 0)# Ne peut pas avoir un rayon < 0
		assert(vMaxDegParSec > 0) # Ne peut pavoir une vitesse max < 0
		assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
		self.roue_gauche = Roue(rayonRouesCm, vMaxDegParSec)
		self.roue_droite = Roue(rayonRouesCm, vMaxDegParSec)
		self.capteurDistance = Capteur_de_distance(distance_captable)
		self.rayonDuRobotCm = rayonDuRobotCm
		self.v = 0
		self.new_orientation = 0
		self.l=l*2*rayonDuRobotCm	

	def setMotorDps(self, ANG_G, ANG_D):
		"""
		cette methode suppose que les deux roues possede le meme rayon
		:param ANG_G : vitesse en deg/s pour la roue gauche
		:param ANG_D : vitesse deg/s pour la roue droite
        cette methode donne la vitesse demandee aux roues
		"""
		self.roue_gauche.vDegParSec = ANG_G
		self.roue_droite.vDegParSec = ANG_D
	
####------------------------ ROUE --------------------------##

class Roue :
	def __init__ (self, taille_cm, vMaxDegParSec) :
		"""
		:param taille_cm : taille de la roue en cm
		:param vMaxTourParSec : vitesse maximale possible pour les roues en rad/s
		"""
		self.taille_cm = taille_cm
		self.vMaxDegParSec = vMaxDegParSec
		self.vDegParSec = 0

####------------------------ Capteur_de_distance --------------------------##

from math import pi,sqrt,sin,cos
import logging

class Capteur_de_distance :
    def __init__(self, distanceCaptable) :
       """
       :param distanceCaptable : distance maximale captable possible
       """
       self.distanceCaptable=distanceCaptable
    
    def distance(self,x,y,obstacle):
        """
        :param x : abscisse du robot
        :param y : ordonnee du robot
        :param obstacle : obstacle avec lequel la distance est calculee
        """
        xr = x
        yr = y
        xo = obstacle.x
        yo = obstacle.y
        return sqrt((xo-xr)**2+(yo-yr)**2)

    def senseur_de_distance(self,pos_x,pos_y,angle_robot,le_pas,l_obstacle):
        """
        Aide page 16 du td2
        on suppose que les obstacles sont des cercles
        :param l_obstacle : liste d'obstacles
        :param pos_y : abscisse du robot
        :param pos_y : ordonnee du robot
        :param angle : permet au capteur de savoir dans quelle direction lancer le laser
        :param le_pas : permet de couper en plusieurs morceaux la distance avant de rencontrer un obstacle 
        """
        k=0
        x = pos_x
        y = pos_y
        print("Distance Captable = ",self.distanceCaptable)
        while k*le_pas < self.distanceCaptable :
            x = x + cos(angle_robot) * le_pas #Lance le laser dans la bonne direction
            y = y + sin(angle_robot) * le_pas #Lance le laser dans la bonne direction
            logging.debug(f"capteur -> ({x},{y})") 
            # Verification si les coordonées du laser se trouve dans un obstacle(cercle)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                
                # Si a un moment le laser se trouve dans un obstacle
                if(self.distance(x,y,obstacle)) <= obstacle.longueur : #obstacle.longueur car dans obstacle attribut longueur m¨
                    logging.debug(f"obstacle à : {sqrt((x-pos_x)**2+(y-pos_y)**2)}")

                    return sqrt((x-pos_x)**2+(y-pos_y)**2)-cs.RAYON_ROBOT_CM
            k +=1
        logging.debug("**** Rien à l'horizon ****")
        return self.distanceCaptable-cs.RAYON_ROBOT_CM     
