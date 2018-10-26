from __future__ import division
import math, random

from skhep.math  import Kallen_function, Vector3D, LorentzVector
from skhep.units import MeV, GeV

class LAB2BodyDecay(object):

    def __init__(self,initialparticle,finalparticles):
        self._initialparticle = initialparticle
        self._finalparticles = finalparticles
        self._setCM()
        self._setLAB()

    def _setLAB(self):
        theboost = self._initialparticle.fourMomentum.boostvector
        for particle in self._finalparticles:
            particle.fourMomentum.boost(theboost)

    def _setCM(self):
        p = self._setP()
        vector3Dlist = self._setVector3D(p)
        for id, particle in enumerate(self._finalparticles):
            particle.fourMomentum.setpxpypzm(vector3Dlist[id].x,vector3Dlist[id].y,vector3Dlist[id].z,particle.mass)

    def _setP(self):
        m0 = self._initialparticle.mass * GeV
        m1 = self._finalparticles[0].mass * GeV
        m2 = self._finalparticles[1].mass * GeV
        p = math.sqrt( Kallen_function( m0**2, m1**2, m2**2 ) ) / (2*m0)
        return p / GeV

    def _setVector3D(self,p):
        theta = 0. #if 3D -> theta0 = math.pi * random.random()
        phi = 2*math.pi * random.random()
        vector1 = Vector3D.fromsphericalcoords(p,phi,theta)
        vector2 = -1*vector1
        return [vector1, vector2]

    @property
    def values(self):
        return self._finalparticles
