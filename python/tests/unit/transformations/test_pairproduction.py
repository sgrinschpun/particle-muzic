import pytest
from phenomena.particles.models.bubblechamber import BubbleChamberParticle, NO_PARENT
from phenomena.particles.transformations.types import Transformation, PairProduction

class PairProductionParticle(BubbleChamberParticle):
    TRANSFORMATIONS = [PairProduction]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(PairProductionParticle, self).__init__(name, **kwargs)
        self._setTransformationManager(self, PairProductionParticle.TRANSFORMATIONS)

test_particles = [(PairProductionParticle("gamma", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
class TestPairProduction(object):

    def test_pairproduction_basics(particle):
        assert particle.name == 'gamma'
        alltypes = particle.transformation.allTypes
        thisType = [transf for transf in alltypes if transf['type']=='PairProduction']
        assert thisType[0]['target'] == 'p+'
        assert set(thisType[0]['list'][0][1]) == set(['e-', 'e+','p+'])

        output = particle.transformation.output
        assert len(output) == 3

        for outputpart in output:
            assert isinstance(outputpart,UndercoverParticle)
            assert outputpart.E < particle.E

    def test_pairproduction_conservation(particle, conservation, resolution, print_particle):
        print_particle

        for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
            assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
