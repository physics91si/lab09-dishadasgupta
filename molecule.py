# Physics 91SI
# Spring 2018
# Lab 9

import numpy as np

class Molecule:  
    """Stores information about a molecule with two particles' positions and masses, spring constant, and equilibrium length ."""
       
    def __init__(self, p1x, p1y, p2x, p2y, p1m, p2m, k, L0):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y
        self.m1 = p1m
        self.m2 = p2m
        self.spr = k
        self.eq = L0
    
    def get_disp(self):
        """Returns the vector distance between particle 1 and 2"""
        return (((self.p2x - self.p1x)**2) + ((self.p2y - self.p1y)**2))**(1/2)
    
    def get_force(self):
        """Returns the force due to the spring on particle 1"""
        stretch = self.get_disp()
        return self.spr*(stretch - self.eq)
    
