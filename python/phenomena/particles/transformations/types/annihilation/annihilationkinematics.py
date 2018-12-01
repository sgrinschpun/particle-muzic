import math, copy
from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody
from phenomena.particles.models.undercoverparticle import UndercoverParticle

class AnnihilationKinematics(KinematicsCalculations):
    '''
    We expect initialparticle and target to be a LorentzVector and outputparticles a list of LorentzVectors
    '''
    def __init__(self, initialparticle, target, finalparticles):
        super(AnnihilationKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        self._calculations = LAB1BodyAnnihilation(self._initial,self._target,self._final)


class LAB1BodyAnnihilation(LABNBody):
    def __init__(self, initialparticle, target, finalparticles):
        super(LAB1BodyAnnihilation, self).__init__(initialparticle, target, finalparticles)

    @property
    def finalState(self):
        return self._finalparticlesLAB

    def _setInitialParticleLAB(self, initialparticle):
        self._initialparticleLAB = initialparticle

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._initialparticleLAB.mass,self._targetLAB.mass)

    def _setS(self):
        self._s = (self._initialparticleCM.e + self._targetCM.e)**2

    def _setLAB(self):
        vectorp = self._initialparticleLAB.fourMomentum.vector*self._p
        px = vectorp.x
        py = vectorp.y
        pz = vectorp.z
        self._finalparticlesLAB = self._finalparticlesCM
        self._finalparticlesLAB[0].fourMomentum.setpxpypze(px,py,pz,self._initialparticleLAB.E+self._targetLAB.mass)
