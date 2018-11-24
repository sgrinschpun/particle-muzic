from __future__ import division
from phenomena.particles.transformations.types import Transformation

class DecayThroughVirtual(Transformation):

    TARGET = None

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        self._buildTransfValues()

    def _outputParticles(self):
        return Transformation.channelListToNames(VirtualDecay(self._particle)xxxxxx)

class VirtualDecay(object):

    def __init__(self, particle):
        self._particle = particle
        self._set_decay_masses()



    def _set_decay_masses(self):
        decay_masses = []
        for part in self._particle.decay_channels:
            decay_masses.append(ParticleDataSource.getMass(part))

        self._decay_masses = decay_masses
