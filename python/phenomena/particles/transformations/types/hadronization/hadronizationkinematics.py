from __future__ import division
import math, random
from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody
from phenomena.particles.models.undercoverparticle import UndercoverParticle

class HadronizationKinematics(KinematicsCalculations):
    '''
    We expect initialparticle to be a LorentzVector and outputparticles a list of LorentzVectors
    '''

    def __init__(self, initialparticle, target, finalparticles):
        super(HadronizationKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        '''
        We exepct hadronization only to 2body as per hadronization_data.json
        '''
        calculations = LAB2BodyDecay(self._initial,self._target,self._final)
        self._calculations = calculations

class LAB2BodyDecay(LABNBody):

    def __init__(self, initialparticle, target, finalparticles):
        super(LAB2BodyDecay, self).__init__(initialparticle, target, finalparticles)

    def _setInitialParticleLAB(self,initialparticle):
        self._initialparticleLAB = initialparticle

    def _setBoost(self):
        self._setBoostVector()
        self._initialparticleCM  = self._initialparticleLAB.fourMomentum.boost(self._boostVector)

    def _setBoostVector(self):
        self._boostVector = self._initialparticleLAB.fourMomentum.boostvector

    def _setS(self):
        self._s = self._initialparticleLAB.E**2 #self._initialparticleCM.e**2

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._finalparticlesCM[0].mass,self._finalparticlesCM[1].mass)
