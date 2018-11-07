from __future__ import division
import math, random

from skhep.math  import Kallen_function, Vector3D, LorentzVector
from skhep.units import MeV, GeV

from phenomena.particles.models.undercoverparticle import UndercoverParticle


class LAB2BodyDecay(object):

    def __init__(self,initialparticle,finalparticles):
        self._setInitialParticle(initialparticle)
        self._finalparticles = finalparticles
        self._setBoost()
        self._setCM()
        self._setLAB()

    def _setInitialParticle(self,initialparticle):
        if initialparticle.mass !=0:
            self._initialparticle = initialparticle
        else:
            fourmomentum = LorentzVector()
            px = initialparticle.fourMomentum.px
            py = initialparticle.fourMomentum.py
            pz = initialparticle.fourMomentum.pz
            fourmomentum.setpxpypze(px,py,py,initialparticle.E)
            self._initialparticle = UndercoverParticle('undercovergamma', mass = fourmomentum.mass)
            self._initialparticle.fourMomentum = fourmomentum

    def _setBoost(self):
        self._boostVector = self._initialparticle.fourMomentum.boostvector

    def _setLAB(self):
        for particle in self._finalparticles:
            newfourMomentum = particle.fourMomentum.boost(-1*self._boostVector)
            particle.fourMomentum = newfourMomentum

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
        theta = math.pi * random.random() # [0, math.pi]
        phi = 2*math.pi * random.random() #random.choice([-math.pi/2, math.pi/2])
        vector1 = Vector3D.fromsphericalcoords(p,theta,phi)
        vector2 = -1*vector1
        return [vector1, vector2]

    @property
    def values(self):
        return self._finalparticles
