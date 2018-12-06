from __future__ import division
import math
import random
from collections import namedtuple
from phenomena.particles.transformations.transformationchannel import TransformationChannel, TransformationChannels, AllDecays
from phenomena.particles.sources import ParticleDataToolFetcher, ParticleDataSource

#VirtualChannel = namedtuple('VirtualChannel', 'output1 virtual output23 BR1,BR2, BRW, Prob')
VirtualChannel = namedtuple('VirtualChannel', 'output1 virtual output23 Prob')

class VirtualParticleChannel(object):
    def __init__(self,particle,decaylist):
        self._particle = particle
        self._channels = TransformationChannels.from_decaylist(self._particle.decay_channels)
        self._channel = self._channels.getChannel(decaylist)[0]
        self._alldecays = AllDecays()
        self._virtualchannels = self._buildVirtualChannels()
        self._virtualchannel = random.choice(self._virtualchannels)

    def _buildVirtualChannels(self):
        assert self._channel.length == 3
        virtualchannels = []
        for index, item in enumerate(self._channel.names):
            output1 = item
            output23 = self._channel.names[:index]+self._channel.names[index+1:]
            virtuallist = self._alldecays.getParticlesfromDecay(output23)
            for item in virtuallist:
                BR1 = item.BR
                virtual = item.name
                if item.BR != 0.0 and not any(obj.virtual == virtual for obj in virtualchannels):
                    BRW = VirtualParticleChannel.breit_wigner(self._particle.name, virtual)
                    try:
                        BR2 = ParticleDataToolFetcher.getBR(virtual,[self._particle.name,ParticleDataSource.getAnti(output1)])
                        prob = BR1*BR2*BRW
                        vc = VirtualChannel(output1, virtual, output23, prob)
                        virtualchannels.append(vc)
                    except:
                        pass
        return virtualchannels

    def getValues(self):
        return self._virtualchannel


    @staticmethod
    def breit_wigner(part0,virtpart):
        E = ParticleDataSource.getMass(part0)**2
        M = ParticleDataSource.getMass(virtpart)**2
        T = ParticleDataSource.getWidth(virtpart)**2
        gamma = math.sqrt((M+T)*M)
        k = 2*math.sqrt(2*M*T)*gamma/(math.pi*math.sqrt(M+gamma))
        result = k/((E-M)**2 + M*T)
        return result
