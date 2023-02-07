from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
from Robot import *
from Capteur_de_distance import * # Permet d'utiliser la classe Capteur_de_distance se trouvant dans le meme repertoire
import math
import numpy as np

roue = Roue(4,50)

roue.setVitesse(20)

robot = Robot(5,20,10,50)

printf("l'état du robot : " , robot.est_entrain_de_rouler())

robot.avancer(0.4,0.5)



