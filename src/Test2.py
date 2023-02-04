from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True


# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 3
VITESSE_MAX_TOUR_PAR_SEC = 5
RAYON_ROBOT_CM = 8

# instanciation d'un robot, prenant en parametre les deux roue créer précédemment
robot = Robot(RAYON_DES_ROUES_CM, VITESSE_MAX_TOUR_PAR_SEC, RAYON_ROBOT_CM)

print(robot)

while True :
    robot.tourner2(2,2)
    robot.nouvelle_position2(1)
    time.sleep(1)
    print(robot)