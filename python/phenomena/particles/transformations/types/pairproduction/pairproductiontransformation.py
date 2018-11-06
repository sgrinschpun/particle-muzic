from phenomena.particles.transformations.types import Transformation
from phenomena.particles.sources import ParticleDataSource

class PairProduction(Transformation):
    '''
    Pair production should involve a target = p+ and an inelastic 3-body collision kinematics
    For simplicity, we treat it as a decay with no target involved.
    LAB2BodyDecay is modified to consider massless initial particles.

    Pair production should include the possibility of muons and taus as output particles.
    '''

    TARGET = None

    INPUT = ['gamma']
    OUTPUT = ['e-', 'e+']

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in PairProduction.INPUT:
            self._buildTransfValues()

    def _outputParticles(self):
        return [(1.0, PairProduction.OUTPUT) ]

    def getProbability(self, dt=1./60.):
        gamma = self._particle.fourMomentum.gamma
        FACTOR = 0.1
        probability = 1- math.exp(-0.3*dt*gamma)
        return FACTOR*probability
