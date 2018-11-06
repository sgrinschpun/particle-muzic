import pytest
from phenomena.particles.models import UndercoverParticle
from testparticles import InelasticParticle

test_particles = [(InelasticParticle("pi-", p=4.0)) ]

@pytest.mark.parametrize("particle",test_particles)
def test_InelasticCollision_Basics(particle):
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']==particle.transformation.selectedType]
    assert thisType[0]['target'] in ['n0','p+']

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_inelasticcollision_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
