import unittest

from Code.simulation import constantes as cs
from Code.simulation import Robot as rb
from Code.simulation import Terrain as ter
from Code.simulation import Simulation as simu
from Code.ia import Traducteur as tr
from Code.ia import IA as ia

import time as time

class test_IA_avancer(unittest.TestCase):
    
    def setUp(self):
        self.robot = rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC,cs.DISTANCE_CAPTABLE,0,0)
        self.terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, [])
        self.simulation = simu.Simulation(self.robot,self.terrain,120)
        self.trad = tr.Traducteur_Simulation(self.simulation,self.robot)
        self.ia_avance = ia.IA_avancer(self.trad,10,100)


    def test_postion_robot_apres_avancement(self):
        self.ia_avance.start()
        if self.ia_avance.encours == False:
            assert

