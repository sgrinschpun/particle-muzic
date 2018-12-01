from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody
from phenomena.particles.models.undercoverparticle import UndercoverParticle
from skhep.math  import LorentzVector

class PairProductionKinematics(KinematicsCalculations):
    def __init__(self, initialparticle, target, finalparticles):
        super(PairProductionKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        self._calculations = LAB2BodyPairProduction(self._initial,self._target,self._final)

class LAB2BodyPairProduction(LABNBody):
    def __init__(self, initialparticle, target, finalparticles):
        super(LAB2BodyPairProduction, self).__init__(initialparticle, target, finalparticles)

    def _setInitialParticleLAB(self,initialparticle):
        fourmomentum = LorentzVector()
        px = initialparticle.fourMomentum.px
        py = initialparticle.fourMomentum.py
        pz = initialparticle.fourMomentum.pz
        fourmomentum.setpxpypze(px,py,py,initialparticle.E)
        self._initialparticleLAB = UndercoverParticle('undercovergamma', mass = fourmomentum.mass)
        self._initialparticleLAB.fourMomentum = fourmomentum

    def _setBoost(self):
        self._setBoostVector()
        self._initialparticleCM  = self._initialparticleLAB.fourMomentum.boost(self._boostVector)

    def _setBoostVector(self):
        self._boostVector = self._initialparticleLAB.fourMomentum.boostvector

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._finalparticlesCM[0].mass,self._finalparticlesCM[1].mass)
        self._setFourMomenta()

    def _setS(self):
        self._s = self._initialparticleCM.e**2
