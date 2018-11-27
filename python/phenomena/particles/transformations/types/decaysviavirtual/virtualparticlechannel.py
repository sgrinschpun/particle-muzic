from collections import namedtuple
from phenomena.particles.sources import ParticleDataToolFetcher, ParticleDataSource

VirtualChannel = namedtuple('VirtualChannel', 'output1 virtual output23 BR1,BR2')

class VirtualParticleChannel(object):

    def __init__(self, particle):
        self._particle = particle
        self._decayParticles= ParticleDataToolFetcher.getDecayParticles(self._particle.name)
        self._buildVirtualChannels(self._decayParticles[0])

    def _buildVirtualChannels(self,decayparticles):
        assert len(decayparticles) == 3
        VirtualChannels = []
        for index, item in enumerate(decayparticles):
            output1 = item
            output23 = decayparticles[:index]+decayparticles[index+1:]
            virtuallist = ParticleDataToolFetcher.getOriginParticles(output23)
            for item in virtuallist:
                if item[0] != 0.0:
                    BR1 = item[0]
                    virtual = item[1][0]
                    BR2 = ParticleDataToolFetcher.getBR(virtual,[self._particle.name,ParticleDataSource.getAnti(output1)])
                    vc = VirtualChannel(output1, virtual, output23, BR1, BR2)
                    VirtualChannels.append(vc)
        self._virtualchannels = VirtualChannels
