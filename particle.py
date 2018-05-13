# Physics 91SI
# Spring 2018
# Lab 9

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, XPosition, YPosition, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.xpos = XPosition   # Sets x position
        self.ypos = YPosition
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,1))
        self.acc = np.zeros((2,1))
