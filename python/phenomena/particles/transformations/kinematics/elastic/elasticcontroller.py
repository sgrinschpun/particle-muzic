from phenomena.particles.transformations.kinematics import KinematicsCalculations


class ElasticKinematics(KinematicsCalculations):
    '''
    We expect initialparticle and target to be a LorentzVector and outputparticles a list of LorentzVectors
    '''
    def __init__(self, initialparticle, target, finalparticles):
        self._target = target
        super(ElasticKinematics, self).__init__(initialparticle, finalparticles)


    def _set_finalState(self):
        self._finalState = 'finalstate'


class LAB2BodyElastic(object):
    def __init__(initialparticle, target, finalparticles):
        self._initialparticle = initialparticle
        self._target = target
        self._finalparticles = finalparticles
        self._setMandelstam()

    def _setMandelstam(self):
        s = (self._initialparticle.fourMomentum.p + self._target.fourMomentum.p)**2
