#!/usr/bin/python
# -*- coding: latin-1 -*-
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
from Robot import *
from Capteur_de_distance import * # Permet d'utiliser la classe Capteur_de_distance se trouvant dans le meme repertoire
import math
import numpy as np

roue = Roue(4,50)

roue.setVitesse(20)

robot = Robot(5,20,10,50)

print("l'état du robot : " , robot.est_entrain_de_rouler())
robot.roue_gauche.setVitesse(0.1)
robot.roue_droite.setVitesse(0.1)
robot.avancer(4,5)
robot.reculer(-4,-5)
robot.arreter_urgence()
robot.tourner(math.pi,3)
#robot.accelerer(5)
#robot.decelerer(3)
#robot.arreter()
#print("les coordonnées polaires du robot : ", robot.conversion_cartesienne_vers_polaire())
#print("les coordonnées cartesiennes du robot : ", robot.conversion_polaire_vers_cartesienne())





