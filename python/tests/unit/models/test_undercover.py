import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.sources import ParticleDataSource

def test_undercover_from_mass():
    particle = UndercoverParticle('12',2.3, p=1)
    assert particle.name == '12'
    assert particle.mass == 2.3
    assert particle.p == 1

def test_undercover_from_name():
    particle = UndercoverParticle('pi+', p=1)
    assert particle.name == 'pi+'
    assert particle.mass == ParticleDataSource.getMass(particle.name)
    assert particle.p == 1
