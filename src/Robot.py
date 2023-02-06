from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
from Capteur_de_distance import * # Permet d'utiliser la classe Capteur_de_distance se trouvant dans le meme repertoire
import math
import numpy as np
class Robot :
    def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteur,vMaxTourParSec, r=0,angle = 0, pos_x = 0, pos_y = 0) :
        """
        Le robot instancie ses deux roues de la meme taille et de meme vitesse maximal
        """
        assert(rayonRouesCm > 0) # Ne peut pas avoir un rayon < 0
        assert(vMaxTourParSec > 0) # Ne peut pavoir une vitesse max < 0
        assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
        self.roue_gauche = Roue(rayonRouesCm, vMaxTourParSec)
        self.roue_droite = Roue(rayonRouesCm, vMaxTourParSec)
        self.r=r
        self.capteurDistance = Capteur_de_distance(capteur,capteur)
        self.angle = angle
        self.rayonDuRobotCm = rayonDuRobotCm 
        self.pos_x = pos_x
        self.pos_y = pos_y
	
    def est_entrain_de_rouler(self) :
        """
        Fonction permet de savoir si le robot est entrain de rouler
        """
        if self.roue_droite.getvitessetourparsec()==0 and self.roue_gauche.getvitessetourparsec()==0 :
            return False
        else :
            return True

    def avancer(self,vitesseVoulue_kmh_er,vitesseVoulue_kmh_et) :
        """
        Fonction permet le robot à reculer avec la vitesse passée en paramètre  
        en vérifiant si les deux roues ont la même vitesse maximale et si la vitesse est supérieur à 0
        :vitesseVouluekm: la vitesse en km/h que l'on souhaite modifier pour les deux roues de robot
        """
        vitesseVoulue_kmh=np.sqrt(vitesseVoulue_kmh_er**2+vitesseVoulue_kmh_et**2)
        assert(vitesseVoulue_kmh > 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) # Permet de vérifier si les deux roues ont la même vitesse maximale     
        self.roue_gauche.setVitesse(vitesseVoulue_kmh)

    def reculer(self,vitesseVoulue_kmh) :
        """
        Fonction permet le robot à reculer avec la vitesse passée en paramètre  
        en vérifiant si les deux roues ont la même vitesse maximale et si la vitesse est supérieur à 0
        :vitesseVouluekm: la vitesse en km/h que l'on souhaite modifier pour les deux roues de robot
        """
        assert(vitesseVoulue_kmh < 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) 
        self.roue_gauche.setVitesse(vitesseVoulue_kmh)
                       
    def arreter_urgence(self):
        """
        Arrete les roues en urgence
        """
        self.roue_gauche.setVitesse(0)
        self.roue_droite.setVitesse(0)

    def tourner(self,angleEnRad,tempsDonneEnSec):
        """
        Modifier la vitesse des deux roues à 0 kh/m puis calculer la vitesse en km/h afin de faire tourner le robot
        :tempsDonne: le robot tourne en un certain temps en seconde. 
        :angleEnRad: Si l'angle est positive alors le robot tourne à droite, on tourne à la gauche sinon.
        """
        self.arreter_urgence() 
        vitesseAng = angleEnRad/tempsDonneEnSec 
        vitessekmh = 3.6*self.roue_droite.taille_cm*(10**(-2))*vitesseAng
        if(angleEnRad<0):
            self.roue_droite.setVitesse(vitessekmh)
            self.roue_gauche.setVitesse(0)
        if(angleEnRad>0):
            self.roue_droite.setVitesse(0)
            self.roue_gauche.setVitesse(vitessekmh)

    def accelerer(self,vitesseVoule):
        """
        Permet d'accélérer le robot jusqu'à la vitesse voulue
        :vitesseVoule: la vitesse voulue en km/h
        """
        assert(self.roue_gauche.vTourParSec!=self.roue_gauche.vTourParSec)
        vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
        while(vitesse_actuelle < vitesseVoule):
                self.roue_gauche.setVitesse(vitesse_actuelle+0.1)
                self.roue_gauche.setVitesse(vitesse_actuelle+0.1)
                vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
    
    def decelerer(self,vitesseVoule):
        """
        Permet de décélérer le robot
        :vitesseVoule: la vitesse à laquelle on veut que le robot ralentisse
        """
        assert(self.roue_gauche.vTourParSec!=self.roue_gauche.vTourParSec)
        vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
        while(vitesse_actuelle > vitesseVoule):
            self.roue_gauche.setVitesse(vitesse_actuelle-0.1)
            self.roue_gauche.setVitesse(vitesse_actuelle-0.1)
            vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)

    def arreter(self):
        """
        Permet d'arrêter le robot
        """
        self.decelerer(0)

    
    def conversion_polaire_vers_cartesienne(self):
        """
		Fait la conversion de donnée polaire en donnees cartesienne
        """
        self.pos_x = self.r * np.cos(self.angle)
        self.pos_y = self.r * np.sin(self.angle)
        return self.pos_x, self.pos_y
    
    def conversion_cartesienne_vers_polaire(self):
        """
        Fait la conversion de donnée cartesienne en donnees polaire
        """
        self.r = np.sqrt(self.pos_x**2 + self.pos_y**2)
        self.angle= np.arctan(self.pos_y/self.pos_x)
        return self.r, self.angle
        

    def nouvelle_position(self, vitesse_er, vitesse_et,orientation, duree):
        """
        Renvoie la distance parcourue (m), pour une vitesse (km)
        et une durée (s)
        Augmente la distance si vitesse est supérieur a zero
        Diminue la distance sinon
        """
        self.r+=vitesse_er*duree
        self.angle+=vitesse_et*duree/self.r
        print("Le robot a avancé et est maintenant à la position : x=",self.conversion_polaire_vers_cartesienne()[0]," y=",self.conversion_polaire_vers_cartesienne()[1])
    

    def evite_obstacles(self,capteur,Obstacle):
        #if(self.pos_x == monde.mur_x |self.pos_y == monde.mur_y ) à modifier, comment peut on faire pour éviter la borne x,y? np.array? 
        #self.arrete_urgence
        bool=True
        while(bool):
            val=np.random.randint(-360,360)
            if(self.capteurDistance.distance(self,Obstacle) < 10):
                self.tourner(val,1)
            
    
    def __str__ (self) :
        """
        Equivalent methode toString(Java)
        Permet de redéfinir la methode print(monInstance)
        """ 
        res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")"
	    # Le test suivant permet de faire un affichage du robot selon s'il roule ou pas# 
        if (self.est_entrain_de_rouler()) :
            res += "est en train de rouler"
        else :
            res += " est à l'arret"
        return res


