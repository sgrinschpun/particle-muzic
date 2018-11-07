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
        fourmomentum = LorentzVector()
        px = initialparticle.fourMomentum.px
        py = initialparticle.fourMomentum.py
        pz = initialparticle.fourMomentum.pz
        fourmomentum.setpxpypze(px,py,py,initialparticle.E)
        self._initialparticleLAB = UndercoverParticle('undercovergamma', mass = fourmomentum.mass)
        self._initialparticleLAB.fourMomentum = fourmomentum

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._initialparticleLAB.mass,self._targetLAB.mass)
        self._setFourMomenta()

    def _setS(self):
        self._s = (self._initialparticleCM.e + self._targetCM.e)**2

    def _setFourMomenta(self):
        vector3Dlist = self._setVector3D(self._p)
        for id, particle in enumerate(self._finalparticlesLAB):
            particle.fourMomentum.setpxpypzm(vector3Dlist[id].x,vector3Dlist[id].y,vector3Dlist[id].z,self._initialparticleLAB.mass)
