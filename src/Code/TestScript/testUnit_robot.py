import unittest
from Code.simulation import Robot as r
from Code.simulation.Vecteur import Point
from Code.simulation import Simulation as s
from Code.simulation import Terrain as t
from Code.simulation import constantes as c
class TestRobot(unittest.TestCase):
    
    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Robot 
        """

        self.r1 = r.Robot(c.RAYON_DES_ROUES_CM,c.RAYON_ROBOT_CM,c.VITESSE_MAX_DEG_PAR_SEC,c.DISTANCE_CAPTABLE)

    def test_init(self):
        self.assertEqual(self.r1.roue_gauche.taille_cm,3)
        self.assertEqual(self.r1.roue_droite.taille_cm,self.r1.roue_gauche.taille_cm)
        self.assertEqual(self.r1.rayonDuRobotCm,5)
        self.assertEqual(self.r1.roue_droite.vMaxDegParSec,self.r1.roue_gauche.vMaxDegParSec)
        self.assertEqual(self.r1.l,2*self.r1.rayonDuRobotCm)
        self.assertEqual(self.r1.capteurDistance.distanceCaptable,c.DISTANCE_CAPTABLE+c.RAYON_ROBOT_CM)
        
    def test_position_x_y(self):
        self.r1.setMotorDps(c.V_ANGULAIRE_G,c.V_ANGULAIRE_D)
        self.assertEqual(self.r1.roue_gauche.vDegParSec,c.V_ANGULAIRE_G)
        self.assertEqual(self.r1.roue_droite.vDegParSec,c.V_ANGULAIRE_D)

        self.r1.update()


    if __name__ == '__main__':
        unittest.main()

#pour tester -> python3 -m unittest nomdefichier -v
