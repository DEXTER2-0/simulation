import unittest
from math import pi
from Code.simulation import Robot as r
from Code.simulation import Capteur_de_distance
#from Code.Capteur_de_distance import Capteur_de_distance as cap
from Code.simulation import Obstacle as ob
from Code.simulation import Vecteur as vec
from Code.simulation import constantes as cs


class TestCapteur(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Capteur_de_distance
        """
        self.capteur = Capteur_de_distance(cs.DISTANCE_CAPTABLE)
        self.robot = r.Robot(3,5,200,cs.DISTANCE_CAPTABLE,vec.Point(0,0),0)
        #self.ia = i.IA(self.robot)
        self.obs1 = ob.Obstacle(1,[0,7],1)
        self.obs2 = ob.Obstacle(1,[0,15],2) 
        self.obs3 = ob.Obstacle(1,[-50,0],45) 
        self.obs4 = ob.Obstacle(1,[13,13],7) 
        self.obs5 = ob.Obstacle(1,[-15,-15],1) 
        self.listObs = [self.obs1,self.obs2,self.obs3,self.obs4,self.obs5]
    #def test_init(self):
     #   print("test_INIT")
      #  self.assertEqual(self.capteur.distanceCaptable,10)

    #def test_distance(self):
     #   print("testDistance")
        #self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs1)
        #self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs2)
        #self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs3)

    def test_senseurDistance(self):
        self.assertEqual(self.capteur.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,0,0.01, self.listObs),cs.DISTANCE_CAPTABLE)
        self.assertLess(self.capteur.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,pi/2,0.01, self.listObs),cs.DISTANCE_CAPTABLE)
        self.assertLess(self.capteur.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,pi,0.01, self.listObs),cs.DISTANCE_CAPTABLE)
        self.assertLess(self.capteur.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,pi/4,0.01, self.listObs),cs.DISTANCE_CAPTABLE)
        self.assertEqual(self.capteur.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,(3*pi)/2,0.01, self.listObs),cs.DISTANCE_CAPTABLE)

    if __name__ == '__main__':
        print("MMAAINN")


        unittest.main()
#pour tester -> python3 .m unittest nom_de_Dexter .nomdefichier -v
