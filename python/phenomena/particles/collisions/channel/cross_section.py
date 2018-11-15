from __future__ import division
import math

class CrossSection(object): # This warrants a class since the calculations will get more complicated when more cases are added

    def __init__(self,mass,twidth,b_rat,energy):

        if mass != 0:
            coeff = 12 * math.pi * b_rat * twidth**2 * energy**2 / mass**2
            denom = ((energy**2 - mass**2)**2 + energy**2 * twidth**2)

            self._cross_section = coeff / denom
        else:
            self._cross_section = 0 # This is because a massless channel is sometimes allowed (such as a photon) before it's removed
