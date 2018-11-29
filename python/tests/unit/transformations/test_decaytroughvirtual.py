import pytest
from phenomena.particles import Particle
from phenomena.particles.models import BubbleChamberParticle, UndercoverParticle
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualParticleChannel

from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher

test_particle= [  (BubbleChamberParticle("mu-"))]

@pytest.mark.skip
def test_anti():
    list = ['nu_e','nu_mu','nu_tau','nu_ebar','nu_mubar','nu_taubar']
    for item in list:
        print ParticleDataSource.getPDGId(item)


@pytest.mark.parametrize("particle",test_particle)
def test_virtual(particle):
    assert isinstance(particle, Particle)
    VPC = VirtualParticleChannel(particle)
    assert isinstance(VPC, object)
    print VPC._decayParticles
    for item in VPC._virtualchannels:
        print item
