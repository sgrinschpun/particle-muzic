import copy
from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody
from phenomena.particles.models.undercoverparticle import UndercoverParticle
from skhep.math  import LorentzVector

class ComptonKinematics(KinematicsCalculations):
    def __init__(self, initialparticle, target, finalparticles):
        super(ComptonKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        self._calculations = LAB2BodyCompton(self._initial,self._target,self._final)


class LAB2BodyCompton(LABNBody):
    def __init__(self, initialparticle, target, finalparticles):
        super(LAB2BodyCompton, self).__init__(initialparticle, target, finalparticles)

    def _setInitialParticleLAB(self, initialparticle):
        fourmomentum = copy.deepcopy(initialparticle.fourMomentum)
        self._initialparticleLAB = UndercoverParticle('undercovergamma', mass =initialparticle.E, p= initialparticle.p, theta = initialparticle.fourMomentum.theta(), phi =  initialparticle.fourMomentum.phi())

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._initialparticleLAB.mass,self._targetLAB.mass)
        self._setFourMomenta()

    def _setS(self):
        self._s = (self._initialparticleCM.e + self._targetCM.e)**2

    def _setFourMomenta(self):
        vector3Dlist = self._setVector3D(self._p)
        self._finalparticlesCM[0].fourMomentum.setpxpypzm(vector3Dlist[0].x,vector3Dlist[0].y,vector3Dlist[0].z,self._initialparticleLAB.mass)
        self._finalparticlesCM[1].fourMomentum.setpxpypzm(vector3Dlist[1].x,vector3Dlist[1].y,vector3Dlist[1].z,self._targetCM.mass)
