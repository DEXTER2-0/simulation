from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *
from Simulation import *
import math
capteur = Capteur_de_distance(5) #si on ne sait pas encore la position de distance comment on fait?
dexter = Robot(3,7, capteur,10)


dexter.avancer(10,10)
dexter.nouvelle_position(2)
dexter.avancer(10,10)
dexter.nouvelle_position(2)
dexter.tourner(-math.pi,3)
print(dexter.angle)
dexter.avancer(1,1)
dexter.nouvelle_position(2)
print(dexter)