import pytest
from context import phenomena
import sys, os

import math

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, UndercoverParticle
#imports for test_fetchers
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher, DecayLanguageFetcher, ExtraInfoFetcher

from testutils import Conservation

#Which Particle Model to Use
PARTICLE = BubbleChamberParticle

#precision
@pytest.fixture(scope='session')
def resolution():
    '''Returns decimals for rounds'''
    return 4

# @pytest.fixture(scope='function')
# def particle(part,momentum):
#     '''Returns boosted particle with given momentum'''
#     return  PARTICLE(part, p=momentum)

@pytest.fixture(scope='function')
def conservation(particle):
    return Conservation(particle)

@pytest.fixture(scope='function')
def print_particle(particle):
    print particle.name
    print particle.fourMomentum
    print particle.transformation.selectedType
    output = particle.transformation.output
    if output !=[]:
        for part in output:
            print part.name
            print part.fourMomentum
    else:
        print output
