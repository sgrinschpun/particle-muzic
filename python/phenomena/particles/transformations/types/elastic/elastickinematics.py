from phenomena.particles.transformations.types import KinematicsCalculations, LABNBody

class ElasticKinematics(KinematicsCalculations):
    '''
    We expect initialparticle and target to be oc class Particle and outputparticles a list of Particle
    '''
    def __init__(self, initialparticle, target, finalparticles):
        super(ElasticKinematics, self).__init__(initialparticle, target, finalparticles)

    def _set_calculations(self):
        self._calculations = LAB2BodyElastic(self._initial,self._target,self._final)

class LAB2BodyElastic(LABNBody):
    def __init__(self, initialparticle, target, finalparticles):
        super(LAB2BodyElastic, self).__init__(initialparticle, target, finalparticles)

    def _setInitialParticleLAB(self,initialparticle):
        self._initialparticleLAB = initialparticle

    def _setS(self):
        self._s = (self._initialparticleCM.e + self._targetCM.e)**2
