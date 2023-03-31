import unittest
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
        self.capteur = Capteur_de_distance(10)
        self.robot = r.Robot(3,5,200,10,vec.Point(0,0),0)
        #self.ia = i.IA(self.robot)
        self.obs1 = ob.Obstacle(1,[7,7],1)
        self.obs2 = ob.Obstacle(1,[0,15],2) 
        self.obs3 = ob.Obstacle(1,[0,250],1) 
        self.listObs = [self.obs1,self.obs2,self.obs3]
    #def test_init(self):
     #   print("test_INIT")
      #  self.assertEqual(self.capteur.distanceCaptable,10)

    #def test_distance(self):
     #   print("testDistance")
        #self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs1)
        #self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs2)
        #self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs3)

    def test_senseurDistance(self):
        self.assertGreaterEqual(self.capteur.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,3.14/2,0.01, self.listObs),0)
        
    if __name__ == '__main__':
        print("MMAAINN")


        unittest.main()
#pour tester -> python3 .m unittest nom_de_Dexter .nomdefichier -v
    