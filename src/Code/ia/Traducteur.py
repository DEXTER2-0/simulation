from Code.simulation.Robot import Robot
from Code.simulation.Robot import Capteur_de_distance 
from math import pi
import time as time

class Traducteur_Simulation:
    def __init__(self,robot,simulation):
        """
        :param simualtion : simulation utilisee
        :param robot : robot utilise
        """
        self.robot=robot
        self.liste={}
        self.t0 = 0
        self.cap = Capteur_de_distance(self.robot.d_captable,self.robot.rayonDuRobotCm)
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
        return k * self.robot.rayonRouesCm + (r * self.robot.rayonRouesCm) / 360

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
    