import pytest
import path

from phenomena.particles.particle_boosted import ParticleBoosted

@pytest.fixture
def pi_rest():
    '''Returns pion at rest'''
    return ParticleBoosted('pi+')

@pytest.fixture
def pi_boosted():
    '''Returns pion with p = 1 GeV'''
    return  ParticleBoosted('pi+', p=1)


def test_particle_name(pi_rest):
    assert pi_rest.name == 'pi+'

def test_particle_rest(pi_rest):
    pi = ParticleBoosted('pi+')
    assert pi_rest.p == 0
    assert pi_rest.E == pi_rest.mass
