import pytest
from phenomena.particles.models import UndercoverParticle
from testparticles import ElasticParticle

test_particles = [(ElasticParticle("e+", p=2.0))]

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


@pytest.mark.parametrize("particle",test_particles)
def test_elasticcollision_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
