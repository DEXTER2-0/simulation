from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True
from math import *







while True :
	robot.tourner2(3.14,0)
	robot.nouvelle_position2(1)
	time.sleep(5)
	print(robot)