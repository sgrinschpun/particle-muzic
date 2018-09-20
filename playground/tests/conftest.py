import pytest
import path
import math

from phenomena.particles.particletest import ParticleTest
#imports for test_fetchers
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher, DecayLanguageFetcher, ExtraInfoFetcher

#precision
@pytest.fixture(scope='session',)
def resolution():
    '''Returns decimals for rounds'''
    return 6

#particle at rest
@pytest.fixture(scope='function')
def particle_rest(particle):
    '''Returns particle at rest'''
    return ParticleTest(particle)

#boosted particle
@pytest.fixture(scope='function')
def particle_boosted(particle,momentum):
    '''Returns boosted particle with given momentum'''
    return  ParticleTest(particle, p=momentum)

#decay values particle
@pytest.fixture(scope='function')
def particle_decay_values(particle,momentum):
    '''Returns decay values of boosted particle with given momentum'''
    return  ParticleTest(particle, p=momentum).decayvalues

#conservations
@pytest.fixture(scope='function')
def particle_conservation_energy(particle,momentum):
    '''Returns energy in and energy out'''
    energy_dict ={}
    original_particle = ParticleTest(particle, p=momentum)
    energy_dict["energy_in"] = original_particle.E
    energy_out = 0.
    for part in original_particle.decayvalues:
        energy_out += part["E"]
    energy_dict["energy_out"] = energy_out
    return energy_dict

@pytest.fixture(scope='function')
def particle_conservation_momentum(particle,momentum):
    '''Returns momentum in and momentum out, both t and l'''
    momentum_dict ={}
    original_particle = ParticleTest(particle, p=momentum)
    momentum_dict["pt_in"] = original_particle.p*math.sin(original_particle.theta)
    momentum_dict["pl_in"] = original_particle.p*math.cos(original_particle.theta)
    pt_out = 0.
    for part in original_particle.decayvalues:
        pt_out += part["p"]*math.sin(part['theta'])
    momentum_dict["pt_out"]=pt_out
    pl_out = 0.
    for part in original_particle.decayvalues:
        pl_out += part["p"]*math.cos(part['theta'])
    momentum_dict["pl_out"]=pl_out
    return momentum_dict

@pytest.fixture(scope='function')
def particle_conservation_charge(particle,momentum):
    '''Returns charge in and charge out'''
    charge_dict = {}
    original_particle = ParticleTest(particle, p=momentum)
    charge_dict['charge_in'] = original_particle.charge
    charge_out = 0.
    for part in original_particle.decayvalues:
        charge_out += ParticleTest(part['name']).charge
    charge_dict['charge_out'] = charge_out
    return charge_dict

#fixtures for test_sources:
@pytest.fixture(scope='session')
def particledatasource():
    return ParticleDataSource

@pytest.fixture(scope='session')
def particledatatools():
    return ParticleDataToolFetcher

@pytest.fixture(scope='session')
def scikithep():
    return SciKitHEPFetcher

@pytest.fixture(scope='session')
def decaylanguage():
    return DecayLanguageFetcher

@pytest.fixture(scope='session')
def extrainfo():
    return ExtraInfoFetcher
