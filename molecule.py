# Physics 91SI
# Spring 2018
# Lab 9

import numpy as np

class Molecule:  
   
    
    def __init__(self, Position1, Position2, M1, M2, k, L0):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos1 = Position1
        self.pos2 = Position2
        self.m1 = M1
        self.m2 = M2
        self.spr = k
        self.eq = L0
    
    def get_disp(self):
        return self.pos2 - self.pos1
    
    def get_force(self):
        stretch = self.get_disp()
        return self.spr*(stretch - self.eq)
    
