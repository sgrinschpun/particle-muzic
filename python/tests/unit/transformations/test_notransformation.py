import pytest
from phenomena.particles.transformations.types import Transformation, NoTransformation
from testparticles import NoTransformationParticle

test_particles = [(NoTransformationParticle("gamma", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_notransformation_basics(particle):
    alltypes = particle.transformation.allTypes
    print alltypes
    thisType = [transf for transf in alltypes if transf['type']=='NoTransformation']
    assert thisType[0]['target'] == None
    assert set(thisType[0]['list']) == set([])

    output = particle.transformation.output
    assert len(output) == 0
