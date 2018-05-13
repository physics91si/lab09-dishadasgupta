# Physics 91SI
# Spring 2018
# Lab 9

import numpy as np

class Molecule:  
   
    
    def __init__(self, Position1_X, Position1_Y, Position2_X, Position2_Y, M1, M2, k, L0):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.posX1 = Position1_X
        self.posY1 = Position1_Y
        self.posX2 = Position2_X
        self.posY2 = Position2_Y
        self.m1 = M1
        self.m2 = M2
        self.spr = k
        self.eq = L0
    
    def get_disp(self):
        return (((self.posX2 - self.posX1)**2) + ((self.posY2 - self.posY1)**2))**(1/2)
    
    def get_force(self):
        stretch = self.get_disp()
        return self.spr*(stretch - self.eq)
    
