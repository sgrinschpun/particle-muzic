from __future__ import division
import math, random


from skhep.math  import Kallen_function, Vector3D, LorentzVector
from skhep.units import MeV, GeV
from skhep.constants import half_pi, two_pi

class LAB4BodyCalc(object):

    def __init__(self,initialparticle,finalparticles):
        self._initialparticle = initialparticle
        self._finalparticles = finalparticles
        self._setCM()
        self._setLAB()

    def _setLAB(self):
        theboost = self._initialparticle.fourMomentum.boostvector
        for particle in self._finalparticles:
            #particle.fourMomentum.boost(theboost)
            particle.fourMomentum.setpxpypzm(1,1,1,particle.mass)

    def _setCM(self):
        pass

    @property
    def values(self):
        return self._finalparticles
