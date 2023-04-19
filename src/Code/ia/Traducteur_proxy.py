from math import pi
import time as time

class Traducteur(object):
    """
    """

    def __init__(self, robot,simulation,est_simulation):
        self.robot = robot
        self.ref_list = {}
        self.sim=simulation
        self.is_simu=est_simulation
        self.t0 = 0

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

    def capteur(self):
        if self.is_simu:
            t=time.time()
            dt=t-self.t0
            self.t0=t
            return self.robot.capteurDistance.senseur_de_distance(self.robot.centre.x,self.robot.centre.y,self.robot.angle_fait,0.01,self.sim.terrain.liste_obstacle)
        else:
            if self.robot.getdistance()==8190:
                return 800
            else:
                return self.robot.getdistance()/10

    def avance(self, speed):
        """
        :param float speed: Vitesse
        """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, speed)

    def stop(self):
        """
        Arrête le robot
        """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

    def tourne(self,orientation,speed):
        if orientation == 0:#gauche
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,speed)
        elif orientation==1 : #droite
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, speed)
