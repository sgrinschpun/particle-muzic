import pytest
from phenomena.particles.models.bubblechamber import BubbleChamberParticle, NO_PARENT
from phenomena.particles.transformations.types import Transformation, ElasticCollisionWithProton, ElasticCollisionWithElectron, ElasticCollisionWithNeutron

class ElasticParticle(BubbleChamberParticle):
    TRANSFORMATIONS = [ElasticCollisionWithProton, ElasticCollisionWithElectron, ElasticCollisionWithNeutron]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(ElasticParticle, self).__init__(name, **kwargs)
        self._setTransformationManager(self, ElasticParticle.TRANSFORMATIONS)

test_particles = [(ElasticParticle("e+", p=2.0))]

@pytest.mark.parametrize("particle",test_particles)
class TestElasticCollision(object):

    def test_ElasticCollision_Basics(particle):
        alltypes = particle.transformation.allTypes
        ElasticType = [transf for transf in alltypes if transf['type']==particle.transformation.selectedType]
        assert ElasticType[0]['target'] in ['e-','n0','p+']
        assert set(ElasticType[0]['list'][0][1]) == set([particle.transformation.target, particle.name])

        assert len(particle.transformation.output) == 2

    def test_ElasticCollision_Conservation(particle, conservation, resolution, print_particle):
        print_particle

        for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
            assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
