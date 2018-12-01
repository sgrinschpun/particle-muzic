import pytest
from phenomena.particles.models import BubbleChamberParticle

test_particles = [
(BubbleChamberParticle("mu-", p=2.0)),
(BubbleChamberParticle("pi+",p=2.0)),
(BubbleChamberParticle("K-", p=2.0)),
(BubbleChamberParticle("K+",p=2.0)),
(BubbleChamberParticle("e-",p=2.0)),
(BubbleChamberParticle("e+",p=2.0)),
(BubbleChamberParticle("gamma",p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_bubblechamber_transformation(particle):
    alltypes = particle.transformation.allTypes
    thisType = particle.transformation.selectedType
    assert thisType in BubbleChamberParticle.TRANSFORMATIONS
