from phenomena.particles.transformations.kinematics import KinematicsCalculations


class InelasticKinematics(KinematicsCalculations):
    '''
    We expect initialparticle and target to be a LorentzVector and outputparticles a list of LorentzVectors
    '''
    def __init__(self, initialparticle, target, finalparticles):
        self._target = target
        super(InelasticKinematics, self).__init__(initialparticle, finalparticles)

    def _set_finalState(self):
        self._finalState = 'finalstate'
