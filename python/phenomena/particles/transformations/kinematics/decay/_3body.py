from __future__ import division
import math, random


from skhep.math  import Kallen_function, Vector3D, LorentzVector
from skhep.units import MeV, GeV
from skhep.constants import half_pi, two_pi
from _2body import LAB2BodyDecay
from phenomena.particles.transformations.kinematics.decay._2body import LAB2BodyDecay
from phenomena.particles.models.undercoverparticle import UndercoverParticle

class LAB3BodyDecay(object):

    def __init__(self,initialparticle,finalparticles):
        self._initialparticle = initialparticle
        self._finalparticles = finalparticles
        self._final1 = finalparticles[0]
        self._final2 = finalparticles[1]
        self._final3 = finalparticles[2]
        self._setBoost()
        self._setDalitz()
        self._setCM()
        self._setLAB()

    def _setBoost(self):
        self._boostVector = self._initialparticle.fourMomentum.boostvector

    def _setCM(self):
        # Step 1: solve the system M -> m12 + m3 in the M CM
        self._part12 = UndercoverParticle('part12', self._m12)
        self._initialparticleCM = UndercoverParticle(self._initialparticle.name, p=0)
        self._outputStep1= LAB2BodyDecay(self._initialparticleCM,[self._part12,self._final3]).values
        #Step 2: solve the system m12 -> m1+m2 in the M CM
        self._outputStep2 = LAB2BodyDecay(self._outputStep1[0],[self._final1,self._final2]).values
        # 1,2,3 in the M CM in finalparticles
        self._finalparticles = [self._outputStep2[0],self._outputStep2[1],self._outputStep1[1]]

    def _setLAB(self):
        for particle in self._finalparticles:
            newfourMomentum = particle.fourMomentum.boost(-1*self._boostVector)
            particle.fourMomentum = newfourMomentum

    def _setDalitz(self):
        M = self._initialparticle.mass
        m1 = self._final1.mass
        m2 = self._final2.mass
        m3 = self._final3.mass
        m12 = random.uniform(m1+m2,M-m3)
        self._m12 = m12

    @property
    def values(self):
        return self._finalparticles
