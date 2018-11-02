import pytest
from context import phenomena
import sys, os

import math

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, UndercoverParticle
#imports for test_fetchers
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, SciKitHEPFetcher, DecayLanguageFetcher, ExtraInfoFetcher

#Which Particle Model to Use
PARTICLE = BubbleChamberParticle

#precision
@pytest.fixture(scope='session',)
def resolution():
    '''Returns decimals for rounds'''
    return 4

#particle at rest
@pytest.fixture(scope='function')
def particle_rest(particle):
    '''Returns particle at rest'''
    return PARTICLE(particle)

#boosted particle
@pytest.fixture(scope='function')
def particle_boosted(particle,momentum):
    '''Returns boosted particle with given momentum'''
    return  PARTICLE(particle, p=momentum)

#decay values particle
@pytest.fixture(scope='function')
def particle_transformation_output(particle,momentum):
    '''Returns decay values of boosted particle with given momentum'''
    return  PARTICLE(particle, momentum).transformation.output

#conservations
@pytest.fixture(scope='function')
def particle_conservation_energy(particle,momentum):
    '''Returns energy in and energy out'''
    energy_dict ={}
    original_particle = PARTICLE(particle, momentum)
    energy_dict["energy_in"] = original_particle.E
    if original_particle.transformation.target:
        energy_dict["energy_in"] += UndercoverParticle(original_particle.transformation.target).fourMomentum.e
    energy_out = 0.
    for item in original_particle.transformation.output:
        print item
        energy_out += item.fourMomentum.e
    energy_dict["energy_out"] = energy_out
    return energy_dict

@pytest.fixture(scope='function')
def particle_conservation_transverse_momentum(particle,momentum):
    '''Returns pt in and momentum out'''
    momentum_dict ={}
    original_particle = PARTICLE(particle, momentum)
    momentum_dict["pt_in"] = original_particle.fourMomentum.pt
    pt_out = 0.
    for item in original_particle.transformation.output:
        print item
        pt_out += item.fourMomentum.pt
    momentum_dict["pt_out"]=pt_out
    return momentum_dict

@pytest.fixture(scope='function')
def particle_conservation_momentum_components(particle,momentum):
    '''Returns pt in and momentum out'''
    momentum_dict ={}
    original_particle = PARTICLE(particle,momentum)
    momentum_dict["p_in"] = [original_particle.fourMomentum.px, original_particle.fourMomentum.py, original_particle.fourMomentum.pz]
    px = py = pz= 0.
    for item in original_particle.transformation.output:
        print item
        px += item.fourMomentum.px
        py += item.fourMomentum.py
        pz += item.fourMomentum.pz
    momentum_dict["p_out"]=[px,py,pz]
    return momentum_dict

@pytest.fixture(scope='function')
def particle_conservation_charge(particle,momentum):
    '''Returns charge in and charge out'''
    charge_dict = {}
    original_particle = PARTICLE(particle, momentum)
    charge_dict['charge_in'] = original_particle.charge
    if original_particle.transformation.target:
        charge_dict['charge_in'] += PARTICLE.getcharge(original_particle.transformation.target)

    charge_out = 0.
    for item in original_particle.transformation.output:
        print item
        charge_out += item.charge
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
