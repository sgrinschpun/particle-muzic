from __future__ import division
import math
from collections import namedtuple
from phenomena.particles.sources import ParticleDataToolFetcher, ParticleDataSource

VirtualChannel = namedtuple('VirtualChannel', 'output1 virtual output23 BR1,BR2, BRW, Prob')

class VirtualParticleChannel(object):

    def __init__(self, particle,id):
        self._particle = particle
        self._decayParticles= ParticleDataToolFetcher.getDecayParticles(self._particle.name)
        self._buildVirtualChannels(self._decayParticles[id])

    def _buildVirtualChannels(self,decayparticles):
        '''
        0 -> o1+o2+o3; VP, virtual particles
        Create all combinations of o1 & o23
        Look for all VP -> o23
        Set de probability of the process through
         - BR1: the prob of the VP -> o23
         - Look for the BR2 of the process VP -> anti(o1) + 0
         - Set the Breit Wigner mass of the particle

        Set an array of VirtualChannels (namedtuples)
        '''
        assert len(decayparticles) == 3
        VirtualChannels = []
        for index, item in enumerate(decayparticles):
            output1 = item
            output23 = decayparticles[:index]+decayparticles[index+1:]
            virtuallist = ParticleDataToolFetcher.getOriginParticles(output23)
            #if lepton neutrino only accept W+-
            if VirtualParticleChannel.leptonnumber(output23)==0:
                for index, item in enumerate(virtuallist):
                    if item[1][0] in ['W+','W-']:
                        virtuallist = [virtuallist[index]]
                        break

            for item in virtuallist:
                BR1 = item[0]
                virtual = item[1][0]
                if BR1 != 0.0:
                    BRW = VirtualParticleChannel.breit_wigner(self._particle.name, virtual)
                    try:
                        BR2 = ParticleDataToolFetcher.getBR(virtual,[self._particle.name,ParticleDataSource.getAnti(output1)])
                        prob = BR1*BR2*BRW
                        vc = VirtualChannel(output1, virtual, output23, BR1, BR2, BRW, prob)
                        VirtualChannels.append(vc)
                    except:
                        pass
        self._virtualchannels = VirtualChannels

    @staticmethod
    def breit_wigner(part0,virtpart):
        E = ParticleDataSource.getMass(part0)**2
        M = ParticleDataSource.getMass(virtpart)**2
        T = ParticleDataSource.getWidth(virtpart)**2
        gamma = math.sqrt((M+T)*M)
        k = 2*math.sqrt(2*M*T)*gamma/(math.pi*math.sqrt(M+gamma))
        result = k/((E-M)**2 + M*T)
        return result

    @staticmethod
    def leptonnumber(pair):
        dict = {
        'e-':1,'nu_e':1,
        'e+':-1,'nu_ebar':-1,
        'mu-':1,'nu_mu':1,
        'mu+':-1,'nu_mubar':-1,
        'tau-': 1,'nu_tau':1,
        'tau+':-1,'nu_taubar':-1
        }
        value = 0
        for item in pair:
            try:
                leptonnumber = dict[item]
            except:
                leptonnumber = 0
            value += leptonnumber
        return value
