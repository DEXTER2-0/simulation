from Code.simulation.Robot import Robot
from Code.simulation.Robot import Capteur_de_distance 
from math import pi
import time as time

class Traducteur(object):
    """
    """

    def __init__(self, robot):
        self.robot = robot
        self.ref_list = {}

    def debut(self, ref, port):
        """
        :param ref : start
        :param port : port utilise
        """
        self.ref_list[ref] = self.robot.get_motor_position()[port]

    def getdistance(self, ref, port):
        """
        :param int port:
        Distance parcourue pour la strat
        """
        diff = self.robot.get_motor_position()[port] - self.ref_list[ref]
        self.ref_list[ref] = self.robot.get_motor_position()[port]
        # Distance parcourue
        k, r = divmod(diff, 360)
        return k * self.robot.rayonRouesCm + (r * self.robot.rayonRouesCm) / 360

    #gestion capteur

    def avance(self, speed):
        """
        :param float speed: Vitesse
        """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, speed)

    def stop(self):
        """
        Arrête le robot
        """
        self.robot.set_motor_dps(self.robot.MOTOR_GAUCHE+self.robot.MOTOR_DROIT,0)

    def tourne(self, side, speed):
        """
        :param int side: Côté
        :param float speed: Vitesse
        """
        if side == 0:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, 0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, speed)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, speed)
