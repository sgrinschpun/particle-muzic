import pytest
from phenomena.particles.models.bubblechamber import BubbleChamberParticle, NO_PARENT
from phenomena.particles.transformations.types import Transformation, Annihilation

class AnnihilationParticle(BubbleChamberParticle):
    TRANSFORMATIONS = [Annihilation]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(AnnihilationParticle, self).__init__(name, **kwargs)
        self._setTransformationManager(self, AnnihilationParticle.TRANSFORMATIONS)

test_particles = [(AnnihilationParticle("e+", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_pairproduction(particle):
    assert particle.name == "e+"
    alltypes = particle.transformation.allTypes
    AnnihilationType = [transf for transf in alltypes if transf['type']=='Annihilation']
    assert AnnihilationType[0]['target'] == 'e-'
    assert set(AnnihilationType[0]['list'][0][1]) == set(['gamma'])
