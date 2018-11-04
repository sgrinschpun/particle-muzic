import pytest
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, UndercoverParticle
from phenomena.particles.transformations.types import Transformation
from phenomena.particles.transformations.kinematics.decay._3body import LAB3BodyDecay

test_3body = [  (BubbleChamberParticle("mu-", p=2.0),0),
                (BubbleChamberParticle("eta", p=1.0),1),
                (BubbleChamberParticle("K+", p=1.0),3)]

@pytest.mark.parametrize("particle, id",test_3body )
def test_3body_decay(particle, id):
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
