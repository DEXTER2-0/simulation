from math import pi

###--------------- PROPRIETE ROBOT -------------------------###
RAYON_ROBOT_CM=100 #en cm

###--------------- PROPRIETE ROUE ---------------------------###
RAYON_DES_ROUES_CM=30 #en cm
DIAMETRE_ROUES=RAYON_DES_ROUES_CM*2
CIRCONFERENCE_ROUES=DIAMETRE_ROUES*pi

VITESSE_MAX_DEG_PAR_SEC= 200
V_ANGULAIRE_G = 120#deg/s
V_ANGULAIRE_D = 120 #deg/s

###--------------- PROPRIETE CAPTEUR_DISTANCE ----------------###
DISTANCE_MIN_ARRET = 5 #en metre (mais faudra mettre en en cm)
DISTANCE_CAPTABLE = 10

###--------------- PROPRIETE TERRAIN -------------------------###
WIDTH = 600 # axe des x
HEIGHT = 600 # axe des y
