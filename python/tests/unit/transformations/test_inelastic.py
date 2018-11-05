import pytest
from phenomena.particles.models.bubblechamber import BubbleChamberParticle, NO_PARENT
from phenomena.particles.transformations.types import Transformation, InelasticCollisionWithProton,InelasticCollisionWithNeutron

class InelasticParticle(BubbleChamberParticle):
    TRANSFORMATIONS = [InelasticCollisionWithProton,InelasticCollisionWithNeutron]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(ElasticParticle, self).__init__(name, **kwargs)
        self._setTransformationManager(self, ElasticParticle.TRANSFORMATIONS)

test_particles = [(InelasticParticle("pi+", p=2.0)),(InelasticParticle("pi-", p=2.0)) ]

@pytest.mark.parametrize("particle",test_particles)
class TestInelasticCollision(object):

    def test_InelasticCollision_Basics(particle):
        alltypes = particle.transformation.allTypes
        thisType = [transf for transf in alltypes if transf['type']==particle.transformation.selectedType]
        assert thisType[0]['target'] in ['n0','p+']
        #assert set(thisType[0]['list'][0][1]) != set([particle.transformation.target, particle.name])

        output = particle.transformation.output
        assert len(output) == 2

        for outputpart in output:
            assert isinstance(outputpart,UndercoverParticle)
            assert outputpart.E < particle.E


    def test_inelasticcollision_conservation(particle, conservation, resolution, print_particle):
        print_particle

        for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
            assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
