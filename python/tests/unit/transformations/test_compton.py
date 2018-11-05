import pytest
from phenomena.particles.models.bubblechamber import BubbleChamberParticle, NO_PARENT
from phenomena.particles.transformations.types import Transformation, ComptonEffect

class ComptonParticle(BubbleChamberParticle):
    TRANSFORMATIONS = [ComptonEffect]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(ComptonParticle, self).__init__(name, **kwargs)
        self._setTransformationManager(self, ComptonParticle.TRANSFORMATIONS)

test_particles = [(ComptonParticle("gamma", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_pairproduction(particle):
    assert particle.name == "gamma"
    alltypes = particle.transformation.allTypes
    ComptonType = [transf for transf in alltypes if transf['type']=='ComptonEffect']
    assert ComptonType[0]['target'] == 'e-'
    assert set(ComptonType[0]['list'][0][1]) == set(['gamma', 'e-'])
