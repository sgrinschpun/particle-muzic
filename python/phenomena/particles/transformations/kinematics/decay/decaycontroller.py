from _2body import LAB2BodyDecay
from _3body import LAB3BodyDecay
from phenomena.particles.transformations.kinematics import KinematicsCalculations

class DecayKinematics(KinematicsCalculations):
    '''
    We expect initialparticle to be a LorentzVector and outputparticles a list of LorentzVectors
    '''

    def __init__(self, initialparticle, finalparticles):
        super(DecayKinematics, self).__init__(initialparticle, finalparticles)

    def _set_finalState(self):
        if len(self._final) == 2:
            finalState = LAB2BodyDecay(self._initial,self._final).values
        elif len(self._final) == 3:
            finalState = LAB3BodyDecay(self._initial,self._final).values
        else:
            finalState = LAB4BodyCalc(self._initial,self._final).values
        self._finalState = finalState
