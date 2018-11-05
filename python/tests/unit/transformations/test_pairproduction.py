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
def test_pairproduction(particle):
    assert particle.name == 'gamma'
    alltypes = particle.transformation.allTypes
    pairProductionType = [transf for transf in alltypes if transf['type']=='PairProduction']
    assert pairProductionType[0]['target'] == 'p+'
    assert set(pairProductionType[0]['list'][0][1]) == set(['e-', 'e+','p+'])
    print particle.transformation.selectedType
    if particle.transformation.selectedType == "PairProduction":
        print "PairProduction!"
        for part in particle.transformation.output:
            print part.name
            print part.fourMomentum
