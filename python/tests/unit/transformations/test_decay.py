import pytest
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, UndercoverParticle
from phenomena.particles.transformations.types import Transformation
from phenomena.particles.transformations.kinematics.decay._3body import LAB3BodyDecay


class DecayParticle(BubbleChamberParticle):
    TRANSFORMATIONS = [Decay]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(DecayParticle, self).__init__(name, **kwargs)
        self._setTransformationManager(self, DecayParticle.TRANSFORMATIONS)

test_3body = [  (DecayParticle("mu-", p=2.0),0),
                (DecayParticle("eta", p=1.0),1),
                (DecayParticle("K+", p=1.0),3)]

test_2body = [  (DecayParticle("pi-", p=2.0),0),
                (DecayParticle("pi+", p=2.0),0),
                (DecayParticle("K-", p=2.0),0),
                (DecayParticle("K+", p=2.0),0)]

@pytest.mark.parametrize("particle, id",test_2body )
class Test2Bodydecay(object):

    def test_2body_decay_basics(particle, id):
        finalparticlesNames = Transformation.channelListToNames(particle.decay_channels)[id][1]
        assert len(finalparticlesNames) == 2
        finalparticles = []
        for part in finalparticlesNames:
            finalparticles.append(UndercoverParticle(part))
        output = LAB3BodyDecay(particle, finalparticles).values

        assert isinstance(output,list)
        assert len(output) == 2
        for outputpart in output:
            assert outputpart.name in finalparticlesNames
            assert isinstance(outputpart,UndercoverParticle)
            assert outputpart.E < particle.E
        #we need a test for ouput particles in the same plane

    def test_2body_decay_conservation(particle, conservation, resolution, print_particle):
        print_particle

        for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
            assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)


@pytest.mark.parametrize("particle, id",test_3body )
class Test3Bodydecay(object):

    def test_3body_decay_basics(particle, id):
        finalparticlesNames = Transformation.channelListToNames(particle.decay_channels)[id][1]
        assert len(finalparticlesNames) == 3
        finalparticles = []
        for part in finalparticlesNames:
            finalparticles.append(UndercoverParticle(part))
        output = LAB3BodyDecay(particle, finalparticles).values

        assert isinstance(output,list)
        assert len(output) == 3
        for outputpart in output:
            assert outputpart.name in finalparticlesNames
            assert isinstance(outputpart,UndercoverParticle)
            assert outputpart.E < particle.E
        #we need a test for ouput particles in the same plane

    def test_3body_decay_conservation(particle, conservation, resolution, print_particle):
        print_particle

        for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
            assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
