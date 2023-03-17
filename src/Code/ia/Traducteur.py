class Traducteur :
    def __init__ (self,ia,robot_reel,robot_sim):
        self.ia = ia 
        self.robot_reel = robot_reel
        self.robot_sim = robot_sim

class Traducteur_Simulation:
    def __init__(self,robot):
        self.robot=robot
    
    def setMotorDps(self,v_gauche,v_droite):
        self.robot.setMotorDps(v_gauche,v_droite)

class Traducteur_Realite:
    def __init__(self,robot):
        self.robot=robot
    
    def setMotorDps(self,v_gauche,v_droit):
        self.robot.set_motor_dps(port,v_gauche)
