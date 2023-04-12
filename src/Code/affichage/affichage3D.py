from threading import Thread
import time
from math import *
import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt
import logging
from Code.simulation import constantes as cs

# Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
AUTRE = (235, 152, 135)

class Affichage3D(Thread):
    def __init__(self, simulation, fps):
        """
        Constructeur de la classe affichage en 3D
        :param simulation: simulation choisie
        :param fps: nombre d'images par seconde
        """
        super(Affichage3D, self).__init__()
        self.simulation = simulation
        pygame.init()
        self.disp = pygame.display.set_mode((cs.WIDTH, cs.HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (cs.WIDTH / cs.HEIGHT), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)  # Position de la caméra
        self.fps = fps
        self.old_pos = []
        logging.info("Affichage 3D créé")

    def run(self):
        """
        Cette boucle permet d'actualiser l'affichage en 3D à chaque pas de temps
        """
        self.encours = True
        while self.encours:
            self.update()
            self.clock.tick(self.fps)
        pygame.quit()
        self.simulation.stop()
        logging.info("Affichage 3D terminé")

    def events(self):
        """
        Sert à récupérer les événements
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.encours = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_q]:  # Quit
                    self.encours = False
                if event.key in [pygame.K_d]:
                    logging.debug(f"Robot :{self.simulation.robot.centre}")

    def update(self):
        """
        Met à jour la position des sprites en 3D
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        x, y, z = self.simulation.robot.centre.x, self.simulation.robot.centre.y, 0
        self.old_pos.append((x, y, z))
        for obs in self.simulation.terrain.liste_obstacle:
            obs.draw3D(RED)
        for pos in self.old_pos:
            pygame.draw.circle(self.disp, RED, (pos[0], pos[1]), 2)

        pygame.draw.circle(self.disp, BLUE, (x, y), cs.RAYON_ROBOT_CM)

        pygame.display.flip()
        self.events()