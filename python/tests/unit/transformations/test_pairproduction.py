import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations.types import Transformation, PairProduction

from testparticles import PairProductionParticle


test_particles = [(PairProductionParticle("gamma", p=2.0))]


@pytest.mark.parametrize("particle",test_particles)
def test_pairproduction_basics(particle):
    assert particle.name == 'gamma'
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='PairProduction']
    #assert thisType[0]['target'] == 'p+'
    assert set(thisType[0]['list'][0][1]) == set(['e-', 'e+'])

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_pairproduction_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
