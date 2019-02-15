import pytest
from phenomena.particles import Particle
from phenomena.particles.models import BubbleChamberParticle, UndercoverParticle
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualParticleChannel

from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher

test_particle= [    (BubbleChamberParticle("mu-"),0),
                    (BubbleChamberParticle("eta"),5),  #['gamma', 'e-', 'e+']
                    (BubbleChamberParticle("K+"),3),
                    (BubbleChamberParticle('pi0'),1),
                    (BubbleChamberParticle('Lambda0'),3),
]


@pytest.mark.parametrize("particle, id",test_particle)
def test_virtual(particle, id):
    assert isinstance(particle, Particle)
    VPC = VirtualParticleChannel(particle, id)
    assert isinstance(VPC, object)
    #print VPC._decayParticles
    for item in VPC._virtualchannels:
        print item

@pytest.mark.skip
def test_choose_chanel():
    part = BubbleChamberParticle('Lambda0')
    decayparticles = ParticleDataToolFetcher.getDecayParticles(part.name)
    for channel in decayparticles:
        print channel
    print decayparticles[3]
