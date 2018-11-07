from __future__ import division
import math, random
from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody
from phenomena.particles.models.undercoverparticle import UndercoverParticle

class DecayKinematics(KinematicsCalculations):
    '''
    We expect initialparticle to be a LorentzVector and outputparticles a list of LorentzVectors
    '''

    def __init__(self, initialparticle, target, finalparticles):
        super(DecayKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        if len(self._final) == 2:
            calculations = LAB2BodyDecay(self._initial,self._target,self._final)
        elif len(self._final) == 3:
            calculations = LAB3BodyDecay(self._initial,self._target,self._final)
        else:
            calculations = LAB4BodyCalc(self._initial,self._target,self._final)
        self._calculations = calculations

class LAB2BodyDecay(LABNBody):

    def __init__(self, initialparticle, target, finalparticles):
        super(LAB2BodyDecay, self).__init__(initialparticle, target, finalparticles)

    def _setInitialParticle(self,initialparticle):
        self._initialparticle = initialparticle

    def _setBoost(self):
        self._setBoostVector()
        self._initialparticleCM  = self._initialparticleLAB.fourMomentum.boost(self._boostVector)

    def _setBoostVector(self):
        self._boostVector = self._initialparticle.fourMomentum.boostvector

    def _setS(self):
        self._s = self._initialparticleCM.e**2


class LAB3BodyDecay(object):

    def __init__(self,initialparticle,finalparticles):
        self._initialparticleLAB = initialparticle
        self.self._finalparticlesLAB= finalparticles
        self._final1 = finalparticles[0]
        self._final2 = finalparticles[1]
        self._final3 = finalparticles[2]
        self._setBoost()
        self._setDalitz()
        self._setCM()
        self._setLAB()

    def _setBoost(self):
        self._boostVector = self._initialparticleLAB.fourMomentum.boostvector

    def _setCM(self):
        # Step 1: solve the system M -> m12 + m3 in the M CM
        self._part12 = UndercoverParticle('part12', self._m12)
        self._initialparticleCM = UndercoverParticle(self._initialparticleLAB.name, p=0)
        self._outputStep1= LAB2BodyDecay(self._initialparticleCM,[self._part12,self._final3]).values
        #Step 2: solve the system m12 -> m1+m2 in the M CM
        self._outputStep2 = LAB2BodyDecay(self._outputStep1[0],[self._final1,self._final2]).values
        # 1,2,3 in the M CM in finalparticles
        self.self._finalparticlesLAB = [self._outputStep2[0],self._outputStep2[1],self._outputStep1[1]]

    def _setLAB(self):
        for particle in self._finalparticles:
            newfourMomentum = particle.fourMomentum.boost(-1*self._boostVector)
            particle.fourMomentum = newfourMomentum

    def _setDalitz(self):
        M = self._initialparticleLAB.mass
        m1 = self._final1.mass
        m2 = self._final2.mass
        m3 = self._final3.mass
        m12 = random.uniform(m1+m2,M-m3)
        self._m12 = m12

    @property
    def finalState(self):
        return self._finalparticlesLAB
