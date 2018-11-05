import pytest
from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, NO_PARENT, ParticleData, ParticlePosition, ParticleBoost, ParticleTransformation
from phenomena.particles.transformations.types import Transformation, NoTransformation

class NoTransformationParticle(ParticleTransformation,ParticleData):
    TRANSFORMATIONS = [NoTransformation]
    def __init__(self, name, parent = NO_PARENT, **kwargs):
        #### ParticleData
        self._set_name(name)  # Name of the particle
        #### ParticleTransformation
        self._setTransformationManager(self, NoTransformationParticle.TRANSFORMATIONS)



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
