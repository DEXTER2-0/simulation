from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur_proxy as proxy
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
from Code.ia.robot2IN013 import Robot2IN013 
from math import radians
from time import time as time
import logging




if __name__=='__main__':
    Dexter=Robot2IN013()
    Dexter.set_motor_dps(Dexter.MOTOR_RIGHT,0)
    Dexter.set_motor_dps(Dexter.MOTOR_LEFT,0)
    