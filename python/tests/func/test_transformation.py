import pytest
from phenomena.particles.models import UndercoverParticle, BubbleChamberParticle

from phenomena.particles.transformations import TransformController

testparticles = [ (BubbleChamberParticle("e-")) ]

@pytest.mark.parametrize("particle",testparticles)
def test_transformations(particle):
    transformationlist = [transf.__name__ for transf in BubbleChamberParticle.TRANSFORMATIONS]
    assert isinstance(particle.transformation, TransformController)
    assert isinstance(particle.transformation.output, list)
    for item in particle.transformation.output:
        assert isinstance(item, UndercoverParticle)
        print item.name
    assert particle.transformation.selectedType in transformationlist
