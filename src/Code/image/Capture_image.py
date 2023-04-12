from PIL import Image
import cv2

class Capture_image:
    def __init__(self,robot):
        self.robot=robot
        self.encours=True
        self.image=None
    
    def update(self):
        self.image=self.robot.get_image()
    
    def stop(self):
        self.encours=False

class Traitement_image: #traitement d'image afin de savoir si la balise entiere est dedans
    def __init__(self):
        self.image=None
        self.balise=None
    
class Decision:
    def __init__(self,robot):
        self.robot=robot
        self.cap=Capture_image(self.robot)
        self.trait=Traitement_image()
