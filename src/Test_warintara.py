from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *
from Simulation import *

capteur = Capteur_de_distance(5,0) #si on ne sait pas encore la position de distance comment on fait?
dexter = Robot(3,7, capteur,10)
simulation = Simulation(dexter)  # l'obstacle 1 dans la simulation.py avec le rayon en param ne marche pas
print(dexter)
print(simulation.obs2)