import pytest
from phenomena.particles.models import UndercoverParticle
from testparticles import ElasticParticle
from phenomena.particles.transformations.kinematics import KinematicsController, ElasticKinematics, LAB2BodyElastic

test_particles = [(ElasticParticle("pi-", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_ElasticCollision_Calculations(particle):
    controller = KinematicsController(particle)
    calculations = LAB2BodyElastic(particle, controller._target, controller._final)
    print controller._target.name
    print 'LAB', calculations._initialparticleLAB.fourMomentum
    print calculations._initialparticleLAB.mass
    print 'CM', calculations._initialparticleCM
    print calculations._initialparticleCM.mass
    print 'LAB', calculations._targetLAB.fourMomentum
    print 'CM', calculations._targetCM
    print calculations._initialparticleCM.e, calculations._targetCM.e
    print (calculations._initialparticleCM.e + calculations._targetCM.e)**2
    print calculations._p

    # print 'pinit', particle.fourMomentum.p
    # print 's', calculations._s
    # print 'p', calculations._p
    # for particle in calculations._finalparticlesLAB:
    #     print particle.fourMomentum
    # assert 1 == 1


@pytest.mark.skip
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
        assert outputpart.E < particle.E

@pytest.mark.skip
@pytest.mark.parametrize("particle",test_particles)
def test_elasticcollision_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
