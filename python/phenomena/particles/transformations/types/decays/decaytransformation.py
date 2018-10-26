from phenomena.particles.transformations.types import Transformation

class Decay(Transformation):

    TARGET = None

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        self._buildTransfValues()

    def _outputParticles(self):
        return Transformation.channelListToNames(self._particle.decay_channels)
