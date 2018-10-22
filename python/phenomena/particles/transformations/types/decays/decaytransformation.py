from phenomena.particles.transformations.types import Transformation

class Decay2(Transformation):

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        self._buildTransfValues()

    def _outputParticles(self):
        return Transformation.channelListToNames(self._particle.decay_channels)

    def _transfTime(self):
        return 1
