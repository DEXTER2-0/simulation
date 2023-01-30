from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import math
import numpy as np
class Robot :
    def __init__ (self, rayonRouesCm,rayonDuRobotCm,vMaxTourParSec,r=0, angle = 0, pos_x = 0, pos_y = 0, estEnTrainDeRouler = False) :
        """
        Le robot instancie ses deux roues de la meme taille et de meme vitesse maximal
        """
        assert(rayonRouesCm > 0) # Ne peut pas avoir un rayon < 0
        assert(vMaxTourParSec > 0) # Ne peut pavoir une vitesse max < 0
        assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
        self.roue_gauche = Roue(rayonRouesCm, vMaxTourParSec)
        self.roue_droite = Roue(rayonRouesCm, vMaxTourParSec)
        self.angle = angle
        self.r = r
        self.rayonDuRobotCm = rayonDuRobotCm 
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.estEnTrainDeRouler = estEnTrainDeRouler # Permet de savoir si le robot est en train de rouler
    
    def avancer(self,vitesseVoulue_kmh) :
        """
        Fonction permet le robot à avancer avec la vitesse passée en paramètre
        """
        assert(vitesseVoulue_kmh > 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) # Permet de vérifier si les deux roues ont la même vitesse maximale     
        print("le robot avance à la vitesse ",(self.roue_droite.setVitesse(vitesseVoulue_kmh)),"km/h")
        self.roue_gauche.setVitesse(vitesseVoulue_kmh)
        self.estEnTrainDeRouler = True
    
    def reculer(self,vitesseVoulue_kmh) :
        """
        Fonction permet le robot à reculer avec la vitesse passée en paramètre
        """
        assert(vitesseVoulue_kmh > 0)
        assert(self.roue_droite.vMaxTourParSec == self.roue_gauche.vMaxTourParSec) # Permet de vérifier si les deux roues ont la même vitesse maximale
        print("le robot recule à la vitesse ",(self.roue_droite.setVitesse(vitesseVoulue_kmh)),"km/h")
        self.roue_gauche.setVitesse(vitesseVoulue_kmh)
        self.estEnTrainDeRouler = True
                
    def arreter_urgence(self):
        """
        Arrete les roues en urgence
        """
        self.roue_gauche.setVitesse(0)
        self.roue_droite.setVitesse(0)
        self.estEnTrainDeRouler = False
        print("Le robot est à l'arret")

    def tourner(self,angleEnRad,tempsDonneEnSec):
        """
        Modifier les vitesses des deux roues en étant donné l'ongle qu'on souhaite retourner
        en un certain temps(tempsDonne) en seconde. Si ongle est positive 
        alors le robot tourne à droite de 'ongle' dégré, on tourne à la gauche sinon
        """
        self.arreter_urgence()
        assert(angleEnRad!= 0)
        vitesseAng = angleEnRad/tempsDonneEnSec
        vitessekmh = 3.6*self.roue_droite.taille_cm*(10**(-2))*vitesseAng
        if(angleEnRad<0):
            self.roue_droite.setVitesse(0)
            self.roue_gauche.setVitesse(vitessekmh)
            print("le robot tourne à gauche")
        if(angleEnRad>0):
            self.roue_droite.setVitesse(vitessekmh)
            self.roue_gauche.setVitesse(0)
            print("le robot tourne à droite")
        self.angle += angleEnRad 


    def conversion_polaire_vers_cartesien(self,r, theta):
        """
		Fait la conversion de donnée polaire en donnees cartesienne
        """
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

    def nouvelle_position(self, vitesse,orientation, duree):
        """
        Renvoie la distance parcourue (m), pour une vitesse (km)
        et une durée (s)
        Augmente la distance si vitesse est supérieur a zero
        Diminue la distance sinon
        """
        pol=self.conversion_polaire_vers_cartesien(self.r,orientation)
        self.pos_x=pol[0]+((vitesse/3.6)*duree)
        self.pos_y=pol[1]
        print("Le robot a avancé tout droit et est maintenant à la position : x=",self.pos_x," y=",self.pos_y)
        
    def __str__ (self) :
        """
        Equivalent methode toString(Java)
        Permet de redéfinir la methode print(monInstance)
        """ 
        res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")"
	    # Le test suivant permet de faire un affichage du robot selon s'il roule ou pas# 
        if (self.estEnTrainDeRouler) :
            res += "est en train de rouler"
        else :
            res += " est à l'arret"
        return res


