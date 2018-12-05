import pytest
from phenomena.particles import Particle
from phenomena.particles.models import BubbleChamberParticle, UndercoverParticle
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualParticleChannel
from phenomena.particles.transformations.transformationchannel import TransformationChannel, TransformationChannels, AllDecays

from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher

test_particle= [    (BubbleChamberParticle("mu-"),['nu_ebar', 'e-', 'nu_mu']),
                    (BubbleChamberParticle("eta"),['gamma', 'e-', 'e+']),  #['gamma', 'e-', 'e+']
                    (BubbleChamberParticle('pi0'),['gamma', 'e-', 'e+']),
                    (BubbleChamberParticle("K+"), ['pi+', 'pi+', 'pi-']),
                    (BubbleChamberParticle('Lambda0'),['nu_ebar', 'e-', 'p+']),
]

@pytest.mark.parametrize("particle, decaylist",test_particle)
def test_virtual(particle, decaylist):
    assert isinstance(particle, Particle)
    VPC = VirtualParticleChannel(particle, decaylist)
    assert isinstance(VPC, object)
    for index, item in enumerate(VPC._virtualchannels):
        print index, item

@pytest.mark.skip
def test_choose_chanel():
    part = BubbleChamberParticle('Lambda0')
    decayparticles = ParticleDataToolFetcher.getDecayParticles(part.name)
    for index, channel in enumerate(decayparticles):
        print index,channel
    #print decayparticles[3]
