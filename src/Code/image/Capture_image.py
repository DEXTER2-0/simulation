from PIL import Image
from ia import IA as ia 
import cv2

class Capture_image:
    def __init__(self,robot):
        self.robot=robot
        self.image=None
    
    def update(self):
        self.image=self.robot.get_image()

class Traitement_image: #traitement d'image afin de savoir si la balise entiere est dedans
    def __init__(self):
        self.image=None
        self.balise=None
    
    def couleurs_balise(): #description des couleurs de la balise
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)

class Decision:
    def __init__(self,robot,traducteur):
        self.robot=robot
        self.tourne=ia.IA_tourner(traducteur,10,1,100)
        self.cap=Capture_image(self.robot)
        self.trait=Traitement_image()
        self.encours=True
    
    def update(self):
        while self.encours:
            self.cap.update()
            #traitement de l'image
            if self.trait.balise:
                self.stop()
            elif not self.trait.balise and not self.tourne.encours:
                self.tourne.start()
            elif not self.trait.balise and self.tourne.encours:
                self.tourne.step()
    
    def stop(self):
        self.encours=False
        self.tourne.stop()
