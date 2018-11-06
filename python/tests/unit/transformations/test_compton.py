import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations.types import Transformation, ComptonEffect
from testparticles import ComptonParticle

test_particles = [(ComptonParticle("gamma", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_basics(particle):
    assert particle.name == "gamma"
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='ComptonEffect']
    assert thisType[0]['target'] == 'e-'
    assert set(thisType[0]['list'][0][1]) == set(['gamma', 'e-'])

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E <= particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
