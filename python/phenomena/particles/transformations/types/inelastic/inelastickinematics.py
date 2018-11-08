from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody

class InelasticKinematics(KinematicsCalculations):
    '''
    We expect initialparticle and target to be a LorentzVector and outputparticles a list of LorentzVectors
    '''
    def __init__(self, initialparticle, target, finalparticles):
        super(InelasticKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        self._calculations = LAB2BodyInelastic(self._initial,self._target,self._final)

class LAB2BodyInelastic(LABNBody):
    def __init__(self, initialparticle, target, finalparticles):
        super(LAB2BodyInelastic, self).__init__(initialparticle, target, finalparticles)

    def _setInitialParticleLAB(self,initialparticle):
        self._initialparticleLAB = initialparticle

    def _setS(self):
        self._s = (self._initialparticleCM.e + self._targetCM.e)**2

    def _setCM(self):
        self._setS()
        self._setP(self._s,self._finalparticlesCM[0].mass,self._finalparticlesCM[1].mass)
        self._setFourMomenta()
