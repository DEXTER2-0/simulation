from Code.simulation import Vecteur as vect
from math import pi,sqrt,sin,cos
import logging

class Robot :
    def __init__ (self,rayonRouesCm,rayonDuRobotCm,distance_captable,px=0,py=0) :
        """
        :param rayonRouesCm : rayon des roues en cm
        :param rayonDuRobotCm : rayon du cercle dans lequel s'inscrit le robot en cm
        :param capteur : Capteur utilise
        :param vMaxRadParSec : vitesse maximale possible pour les roues en rad/s
        :param distance_captable : distance maximale que le capteur peut calculer
        Cette fonction instancie deux roues de la meme taille et de meme vitesse maximale, ainsi qu'un capteur de position
        """
        self.centre=vect.Point(px,py)
        self.rayonRouesCm=rayonRouesCm
        self.rayonDuRobotCm = rayonDuRobotCm
        #self.roue_gauche = Roue(self.rayon_roue, self.gspeed)
        #self.roue_droite = Roue(self.rayon_roue, self.dspeed)
        #self.l=l*2*rayonDuRobotCm
        self.vec=vect.Vecteur.get_vect_from_angle(0)
        self.gspeed = 0
        self.dspeed = 0
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2
        self.pos_roue_g=0
        self.pos_roue_d=0
        self.update()
        self.angle_fait=0
        self.d_captable=distance_captable
        self.capteurDistance=Capteur_de_distance(self.d_captable,self.rayonDuRobotCm)
        
    def capteur(self,obs):
        """
        :return: distance entre le robot et l'obstacle le plus proche
        """
        return self.capteurDistance.senseur_de_distance(self.centre.x,self.centre.y,self.angle_fait,0.01,obs)
    
    def set_motor_dps(self, port, dps):
        """
        :param int port: Moteur
        :param float dps: Vitesse
        """
        if port == self.MOTOR_LEFT:
            self.gspeed = dps
        elif port == self.MOTOR_RIGHT:
            self.dspeed = dps
        elif port == self.MOTOR_LEFT + self.MOTOR_RIGHT:
            self.dspeed = dps
            self.gspeed = dps
    
    def get_motor_position(self):
        return self.pos_roue_g, self.pos_roue_d
    
    def cotehg(self,vec_normal):
        self.cote_haut_gauche=vect.Point(self.centre.x-(self.rayonRouesCm//2)*self.vec.vect[0]-(self.rayonRouesCm//2)*vec_normal.vect[0],self.centre.y -(self.rayonRouesCm//2)*self.vec.vect[1]-(self.rayonRouesCm//2)*vec_normal.vect[1])

    def cotebg(self,vec_normal):
        self.cote_bas_gauche=vect.Point(self.centre.x-(self.rayonRouesCm//2)*self.vec.vect[0]+(self.rayonRouesCm//2)*vec_normal.vect[0],self.centre.y-(self.rayonRouesCm//2)*self.vec.vect[1]+(self.rayonRouesCm//2)*vec_normal.vect[1])

    def cotehd(self,vec_normal):
        self.cote_haut_droite=vect.Point(self.centre.x+(self.rayonRouesCm//2)*self.vec.vect[0]-(self.rayonRouesCm//2)*vec_normal.vect[0],self.centre.y+(self.rayonRouesCm//2)*self.vec.vect[1]-(self.rayonRouesCm//2)*vec_normal.vect[1])

    def cotebd(self,vec_normal):
        self.cote_bas_droite=vect.Point(self.centre.x+(self.rayonRouesCm//2)*self.vec.vect[0]+(self.rayonRouesCm//2)*vec_normal.vect[0],self.centre.y+(self.rayonRouesCm//2)*self.vec.vect[1]+(self.rayonRouesCm//2)*vec_normal.vect[1])

    def update(self):
        """
        Mets a jour les coordonnes du robot
        """
        vec_normal=vect.Vecteur(vect.Point(0,0),vect.Point(-self.vec.vect[1],self.vec.vect[0]))
        self.cotehg(vec_normal)
        self.cotebg(vec_normal)
        self.cotehd(vec_normal)
        self.cotebd(vec_normal)
        
####------------------------ ROUE --------------------------##

class Roue :
    def __init__ (self, taille_cm, vMaxDegParSec) :
        """
        :param taille_cm : taille de la roue en cm
        :param vMaxDegParSec : vitesse maximale possible pour les roues en deg/s
        """
        self.taille_cm = taille_cm
        self.vMaxDegParSec = vMaxDegParSec
        self.vDegParSec = 0

####------------------------ Capteur_de_distance --------------------------##

from math import pi,sqrt,sin,cos

class Capteur_de_distance :
    def __init__(self, distanceCaptable,rayon_robot) :
       """
       :param distanceCaptable : distance maximale captable possible
       """
       self.rayonDuRobotCm=rayon_robot
       self.distanceCaptable=distanceCaptable+self.rayonDuRobotCm
    
    def distance(self,x,y,obstacle):
        """
        :param x : abscisse du robot
        :param y : ordonnee du robot
        :param obstacle : obstacle avec lequel la distance est calculee
        """
        xr = x
        yr = y
        xo = obstacle.pos[0]
        yo = obstacle.pos[1]
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
        # ("posxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",pos_x)
        # ("posyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",pos_y)
        # ("angllllllllllllllleeeeeeeeeeeee ",angle_robot)
        k=0
        x = pos_x
        y = pos_y
        while k*le_pas < self.distanceCaptable :
            x = x + cos(angle_robot) * le_pas #Lance le laser dans la bonne direction
            y = y + sin(angle_robot) * le_pas #Lance le laser dans la bonne direction
            # ("x =",x,"y =",y)
            # Verification si les coordonees du laser se trouve dans un obstacle(cercle)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                # Si a un moment le laser se trouve dans un obstacle
                if(self.distance(x,y,obstacle)) <= obstacle.rayon : #obstacle.longueur car dans obstacle attribut longueur m
                    #logging. basicConfig()("boucle : ",sqrt((x-pos_x)**2+(y-pos_y)**2) - self.rayonDuRobotCm)
                    # (sqrt((x-pos_x)**2+(y-pos_y)**2) - self.rayonDuRobotCm)
                    return sqrt((x-pos_x)**2+(y-pos_y)**2) - self.rayonDuRobotCm
            k +=1
        #logging. basicConfig()("fin fct : ",self.distanceCaptable- self.rayonDuRobotCm)
        # (self.distanceCaptable - self.rayonDuRobotCm)
        return self.distanceCaptable - self.rayonDuRobotCm
