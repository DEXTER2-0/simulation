from Code.simulation.Robot import Robot
from Code.simulation.Robot import Capteur_de_distance 
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
    def __init__(self,robot,simulation):
        """
        :param simualtion : simulation utilisee
        :param robot : robot utilise
        """
        self.robot=robot
        self.liste={}
        self.t0 = 0
        self.cap = Capteur_de_distance(self.robot.d_captable)
        self.sim = simulation

    def debut(self,ref,port):
        """
        :param ref : start
        :param port : port utilise
        """
        self.liste[ref]=self.robot.get_pos_roues()[port]

    def stopSim(self):
        self.simulation.stop()

    def getdistance(self,ref,port): #INITIALISATION DE T0 methode reset et get?
        diff = self.robot.get_pos_roues()[port] - self.liste[ref]
        self.liste[ref] = self.robot.get_pos_roues()[port]
        # Distance parcourue
        k, r = divmod(diff, 360)
        return k * self.rayonRouesCm + (r * self.rayonRouesCm) / 360

    def resetdistance(self):
        self.distance=0

    def getangle(self):
        t=time.time()
        dt=t-self.t0
        self.t0=t
        self.angle+=dt*self.robot.gspeed
        print("angle =",self.angle)
    
    def resetangle(self):
        self.angle=0

    def capteur(self):
        t=time.time()
        dt=t-self.t0
        self.t0=t
        return self.cap.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,self.robot.angle_fait,0.01,self.sim.terrain.liste_obstacle)

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
    
    def evaluer_condition(self,condition):
        """
        :condition: condition(chaine caractere) a evaluer 
        verifier la condition, return True si c'est verifie, Flase sinon. 
        """
        return (eval(condition))

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
    
    #def capteur(dt):
    #    """
    #    :param dt : temps ecoule depuis le dernier calcul
    #    """
