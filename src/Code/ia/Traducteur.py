from Code.simulation import constantes as cs
from Code.simulation.Robot import Robot
from math import pi

class Traducteur :
    def __init__ (self,simulation,robot_reel,robot_sim):
        """
        :param simulation : simulation utilisee
        :param robot_reel : robot reel utilise
        :param robot_sim : robot simule utilise
        """
        self.simulation=simulation
        self.robot_reel = robot_reel
        self.robot_sim = robot_sim

class Traducteur_Simulation:
    def __init__(self,simulation,robot):
        """
        :param simualtion : simulation utilisee
        :param robot : robot utilise
        """
        self.simulation=simulation
        self.robot=robot
        self.distance=0
        self.angle=0
    
    def stopSim(self):
        self.simulation.stop()
    
    def setMotorDps(self,v_gauche,v_droite):
        """
        :param v_gauche : vitesse de la roue gauche en deg/s
        :param v_droite : vitesse de la roue droite en deg/s
        """
        self.robot.setMotorDps(v_gauche,v_droite)
    
    def getdistance(self,dt):
        """
        :param dt : temps ecoule depuis le dernier calcul
        """
        self.distance+=dt*cs.V_ANGULAIRE_G*cs.RAYON_ROBOT_CM*0.01*360

    def resetdistance(self):
        self.distance=0

    def getangle(self,dt):
        """
        :param dt : temps ecoule depuis le dernier calcul
        """
        self.angle+=dt*cs.V_ANGULAIRE_G
    
    def resetangle(self):
        self.angle=0

    def calcul_v(self,v_g,v_d):
        """
        :param v_g : vitesse de la roue gauche en deg/s
        :param v_d : vitesse de la roue droite en deg/s
        """
        self.robot.v=((cs.RAYON_DES_ROUES_CM*0.01)/2)*(v_g*(360/(2*pi))+v_d*(360/(2*pi)))
    
    def calcul_new_orientation(self,v_g,v_d):
        """
        :param v_g : vitesse de la roue gauche en deg/s
        :param v_d : vitesse de la roue droite en deg/s
        """
        self.robot.new_orientation=(cs.RAYON_DES_ROUES_CM/cs.RAYON_ROBOT_CM)*(v_g*(360/(2*pi))-v_d*(360/(2*pi)))

    def capteur(dt):
        """
        :param dt : temps ecoule depuis le dernier calcul
        """
        self.robot.senseur_de_distance(self.simulation.pos_x,self.simulation.pos_y,self.simulation.angle_robot,dt,self.simulation.terrain.liste_obstacle)

class Traducteur_Realite:
    def __init__(self,robot):
        """
        :param robot : robot utilise
        """
        self.robot=robot
    
    def setMotorDps(self,v_gauche,v_droit):
        """
        :param v_gauche : vitesse de la roue gauche en deg/s
        :param v_droite : vitesse de la roue droite en deg/s
        """
        self.robot.set_motor_dps(port,v_gauche)
    
    def getdistance(self,dt):
        """
        :param dt : temps ecoule depuis le dernier calcul
        """
        return dt*self.robot.get_motor_position()*360#*taille de la roue en m
    
    def resetdistance(self):
        self.robot.offset_motor_encoder(port, offset)

    def getangle(self,dt):
        """
        :param dt : temps ecoule depuis le dernier calcul
        """
        return dt*self.robot.get_motor_position()
    
    def resetangle(self):
        self.robot.offset_motor_encoder(port, offset)
    
    #def calcul_v(self,v_g,v_d):
    #    """
    #    :param v_g : vitesse de la roue gauche en deg/s
    #    :param v_d : vitesse de la roue droite en deg/s
    #    """

    #def calcul_new_orientation(self,v_g,v_d):
    #    """
    #    :param v_g : vitesse de la roue gauche en deg/s
    #    :param v_d : vitesse de la roue droite en deg/s
    #    """

    #def capteur(dt):
    #    """
    #    :param dt : temps ecoule depuis le dernier calcul
    #    """
