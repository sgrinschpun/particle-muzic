import pytest
from phenomena.particles.models import UndercoverParticle
from testparticles import ElasticParticle
from phenomena.particles.transformations import KinematicsController
from phenomena.particles.transformations.types import ElasticKinematics

test_particles = [(ElasticParticle("pi-", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_ElasticCollision_Calculations(particle):
    target = UndercoverParticle(particle.transformation.target)
    finallist = []
    for part in particle.transformation.selectedChannel:
        finallist.append(UndercoverParticle(part))
    calculations = ElasticKinematics(particle,target,finallist)._calculations

    assert calculations._targetLAB.p == 0
    assert calculations._initialparticleCM.vector == -1*calculations._targetCM.vector
    assert calculations._p < particle.p

@pytest.mark.parametrize("particle",test_particles)
def test_ElasticCollision_Basics(particle):
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']==particle.transformation.selectedType]
    assert thisType[0]['target'] in ['e-','n0','p+']
    assert set(thisType[0]['list'][0][1]) == set([particle.transformation.target, particle.name])

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E <= particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_elasticcollision_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
