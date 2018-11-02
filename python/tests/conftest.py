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

@pytest.fixture(scope='function')
def conservation(part, momentum):
    return Conservation(part, momentum)
