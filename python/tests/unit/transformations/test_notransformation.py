import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations import TransformController
from phenomena.particles.transformations import TransformationChannels, TransformationChannel
from phenomena.particles.transformations.types import Transformation, TransformationValues

from phenomena.particles.transformations.types import NoTransformation
from testparticles import NoTransformationParticle

test_particles = [(NoTransformationParticle("gamma", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_notransformation_basics(particle):
    assert isinstance(particle.transformation,TransformController)
    assert isinstance(particle.transformation.allTypes,list)
    assert isinstance(particle.transformation.selectedType,TransformationValues)
    assert isinstance(particle.transformation.selectedType.channels,TransformationChannels)
    assert isinstance(particle.transformation._selectedChannel,TransformationChannel)
    assert isinstance(particle.transformation.selectedChannel,list)
    assert isinstance(particle.transformation.output,list)

    assert particle.transformation.selectedType.type == 'NoTransformation'
    assert particle.transformation.selectedType.target == None
    assert particle.transformation._selectedChannel.nameSet == set([])
    assert len(particle.transformation.output) == 0
