import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations import TransformController
from phenomena.particles.transformations import TransformationChannels, TransformationChannel
from phenomena.particles.transformations.types import Transformation, TransformationValues

from phenomena.particles.transformations import KinematicsController
from phenomena.particles.transformations.types import AnnihilationKinematics

from testparticles import AnnihilationParticle

test_particles = [(AnnihilationParticle("e+", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
def test_annihilation_basics(particle):
    assert isinstance(particle.transformation,TransformController)
    assert isinstance(particle.transformation.allTypes,list)
    assert isinstance(particle.transformation.selectedType,TransformationValues)
    assert isinstance(particle.transformation.selectedType.channels,TransformationChannels)
    assert isinstance(particle.transformation._selectedChannel,TransformationChannel)
    assert isinstance(particle.transformation.selectedChannel,list)
    assert isinstance(particle.transformation.output,list)

    assert particle.transformation.selectedType.type == 'Annihilation'
    assert particle.transformation.selectedType.target == 'e-'
    assert particle.transformation._selectedChannel.nameSet == set(['gamma'])
    assert len(particle.transformation.output) == 1

@pytest.mark.skip
@pytest.mark.parametrize("particle",test_particles)
def test_annihilation_conservation(particle, conservation, resolution, print_particle):
    print_particle
    for attr in ['E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
    #for attr in ['P']:
    #    assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)
