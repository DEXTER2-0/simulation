from Code.simulation import constantes as cs
from Code.simulation.Robot import Robot
from math import pi
import time as time

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
    def __init__(self,robot):
        """
        :param simualtion : simulation utilisee
        :param robot : robot utilise
        """
        self.robot=robot
        self.liste={}

    def debut(self,ref,port):
        """
        :param ref : start
        :param port : port utilise
        """
        self.liste[ref]=self.robot.get_pos_roues()[port]

    
    def stopSim(self):
        self.simulation.stop()

    def getdistance(self,ref,port): #INITIALISATION DE T0 méthode reset et get?
        diff = self.robot.get_pos_roues()[port] - self.liste[ref]

        self.liste[ref] = self.robot.get_pos_roues()[port]

        # Distance parcourue
        k, r = divmod(diff, 360)

        return k * cs.RAYON_DES_ROUES_CM + (r * cs.RAYON_DES_ROUES_CM) / 360

    def resetdistance(self):
        self.distance=0

    def getangle(self):
        t=time.time()
        dt=t-self.t0
        self.t0=t
        self.angle+=dt*cs.V_ANGULAIRE_G
    
    def resetangle(self):
        self.angle=0

    
    def capteur(self):
        t=time.time()
        dt=t-self.t0
        self.t0=t
        return self.robot.capteurDistance.senseur_de_distance(self.simulation.pos_x,self.simulation.pos_y,self.simulation.angle,dt,self.simulation.terrain.liste_obstacle)

    def avance(self,speed):
        self.robot.setMotorDps(self.robot.MOTOR_GAUCHE+self.robot.MOTOR_DROIT,speed)

    def tourne(self,orientation,speed):
        if orientation == 0:#gauche
            self.robot.setMotorDps(self.robot.MOTOR_DROIT, 0)
            self.robot.setMotorDps(self.robot.MOTOR_GAUCHE,speed)
        elif orientation==1 : #droite
            self.robot.setMotorDps(self.robot.MOTOR_GAUCHE,0)
            self.robot.setMotorDps(self.robot.MOTOR_DROIT, speed)


    def stop(self):
       self.robot.setMotorDps(self.robot.MOTOR_GAUCHE+self.robot.MOTOR_DROIT,0)
    


    def reset(self,roue):
        self.distance=self.robot.get_pos_roues()[roue]
        self.angle=0
        self.robot.setMotorDps(0,0)
    


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
