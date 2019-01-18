import pytest
from phenomena.particles.models import QuantumUniverseVirtualParticle
from phenomena.particles.models.undercoverparticle import UndercoverParticle, VirtualUndercoverParticle
from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualInfo, VirtualParticleChannel
from phenomena.particles.server_particle import ServerParticle
from phenomena.particles.transformations.kinematicscontroller import KinematicsController, VirtualKinematicsController
from phenomena.particles.transformations.types.decays import DecayKinematics, LAB2BodyDecay

def test_virtualundercover():
    name = 'W+'
    decay = ['e-','nu_ebar']
    mass= VirtualParticleChannel.totalMass(decay)

    VI = VirtualInfo('W+',mass, decay)
    assert isinstance(VI, VirtualInfo)
    VP = VirtualUndercoverParticle(VI, p= 0.5, theta = 1, phi = 1)
    assert isinstance(VP, VirtualUndercoverParticle)
    assert VP.name == name
    assert VP.mass == mass

    VPS = ServerParticle.fromparticle(VP)
    assert isinstance(VPS, QuantumUniverseVirtualParticle)
    assert round(VPS.p,3) == round(VP.p,3)
    assert round(VPS.theta,3) == round(VP.theta,3)
    assert round(VPS.phi,3) == round(VP.phi,3)
    assert VPS._decay_channels == VP._decay_channels

    KC = KinematicsController(VPS)
    assert isinstance(KC,KinematicsController)
    assert KC._initial == VPS
    assert KC._target == None
    assert isinstance (KC._final, list)

    DK = DecayKinematics( KC._initial, KC._target, KC._final)
    assert isinstance(DK,DecayKinematics)

    DK2B = LAB2BodyDecay(KC._initial,KC._target,KC._final)
    assert isinstance(DK2B,LAB2BodyDecay)
    print DK2B._initialparticleLAB.p
    print DK2B._initialparticleLAB.mass
    print DK2B._initialparticleCM.p
    print DK2B._initialparticleCM.mass
    for item in DK2B._finalparticlesCM:
        print item.p, item.theta, item.phi
    for item in DK2B._finalparticlesLAB:
        print item.p, item.theta, item.phi
