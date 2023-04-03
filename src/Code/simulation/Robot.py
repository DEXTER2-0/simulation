from Code.simulation import constantes as cs
from Code.simulation import Vecteur as vect
from math import pi,sqrt,sin,cos

class Robot :
    def __init__ (self,px=0,py=0,) :
        """
        :param rayonRouesCm : rayon des roues en cm
        :param rayonDuRobotCm : rayon du cercle dans lequel s'inscrit le robot en cm
        :param capteur : Capteur utilise
        :param vMaxRadParSec : vitesse maximale possible pour les roues en rad/s
        :param distance_captable : distance maximale que le capteur peut calculer
        Cette fonction instancie deux roues de la meme taille et de meme vitesse maximale, ainsi qu'un capteur de position
        """
        self.centre=vect.Point(px,py)
        #assert(rayonRouesCm > 0)# Ne peut pas avoir un rayon < 0
        #assert(vMaxDegParSec > 0) # Ne peut pavoir une vitesse max < 0
        #assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
        #self.rayon_roue=rayonDuRobotCm
     
        #self.roue_gauche = Roue(self.rayon_roue, self.gspeed)
        #self.roue_droite = Roue(self.rayon_roue, self.dspeed)
        #self.capteurDistance = Capteur_de_distance(distance_captable)
        #self.rayonDuRobotCm = rayonDuRobotCm
        #self.l=l*2*rayonDuRobotCm
        
        self.vec=vect.Vecteur.get_vect_from_angle(0)
        self.update()
        self.gspeed = 0
        self.dspeed = 0
        self.MOTOR_GAUCHE = 1
        self.MOTOR_DROIT = 2
        self.pos_roue_g=0
        self.pos_roue_d=0
        self.dessin=False

    def setMotorDps(self, port, dps):
        """
        :param int port: Moteur
        :param float dps: Vitesse
        """
        if port == self.MOTOR_GAUCHE:
            self.gspeed = dps
        elif port == self.MOTOR_DROIT:
            self.dspeed = dps
        elif port == self.MOTOR_GAUCHE + self.MOTOR_DROIT:
            self.dspeed = dps
            self.gspeed = dps
    

    def get_pos_roues(self):
        return self.pos_roue_g, self.pos_roue_d
    
    def update(self):
        """
        Mets a jour les coordonnes du robot
        """
        vec_normal=vect.Vecteur(vect.Point(0,0),vect.Point(-self.vec.vect[1],self.vec.vect[0]))
        self.cote_haut_gauche=vect.Point(self.centre.x-(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[0]-(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[0],self.centre.y -(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[1]-(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[1])
        self.cote_bas_gauche=vect.Point(self.centre.x-(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[0]+(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[0],self.centre.y-(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[1]+(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[1])
        self.cote_haut_droite=vect.Point(self.centre.x+(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[0]-(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[0],self.centre.y+(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[1]-(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[1])
        self.cote_bas_droite=vect.Point(self.centre.x+(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[0]+(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[0],self.centre.y+(cs.RAYON_DES_ROUES_CM//2)*self.vec.vect[1]+(cs.RAYON_DES_ROUES_CM//2)*vec_normal.vect[1])

    def dessine(self,b):
        self.dessin=b

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
    def __init__(self, distanceCaptable) :
       """
       :param distanceCaptable : distance maximale captable possible
       """
       self.distanceCaptable=distanceCaptable+cs.RAYON_ROBOT_CM
    
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
        k=0
        x = pos_x
        y = pos_y
        while k*le_pas < self.distanceCaptable :
            x = x + cos(angle_robot) * le_pas #Lance le laser dans la bonne direction
            y = y + sin(angle_robot) * le_pas #Lance le laser dans la bonne direction
            #print("x =",x,"y =",y)
            # Verification si les coordonees du laser se trouve dans un obstacle(cercle)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                # Si a un moment le laser se trouve dans un obstacle
                if(self.distance(x,y,obstacle)) <= obstacle.rayon : #obstacle.longueur car dans obstacle attribut longueur m
                    print("boucle : ",sqrt((x-pos_x)**2+(y-pos_y)**2) - cs.RAYON_ROBOT_CM)
                    return sqrt((x-pos_x)**2+(y-pos_y)**2) - cs.RAYON_ROBOT_CM
            k +=1
        print("fin fct : ",self.distanceCaptable- cs.RAYON_ROBOT_CM)
        return self.distanceCaptable - cs.RAYON_ROBOT_CM
