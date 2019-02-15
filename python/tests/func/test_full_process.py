import pytest
from phenomena.particles.models import UndercoverParticle, BubbleChamberParticle
from phenomena.particles.transformations import TransformController, KinematicsController

testparticles1 = [   (BubbleChamberParticle("pi-")),
                    (BubbleChamberParticle("mu-")),
                ]

testparticles2 = [ (BubbleChamberParticle("gamma")),
                ]

@pytest.mark.parametrize("particle",testparticles1)
def test_fullprocess_decay(particle):
    assert isinstance(particle, BubbleChamberParticle)
    assert isinstance(particle.transformation, TransformController)
    assert isinstance(particle.transformation.output, list)
    for item in particle.transformation.output:
        assert isinstance(item,UndercoverParticle)
    KC = KinematicsController(particle)
    for item in  KC.getFinalState():
        assert isinstance(item,UndercoverParticle)
    assert len(particle.transformation.output) == len(KC.getFinalState())

@pytest.mark.parametrize("particle",testparticles2)
def test_fullprocess_notransformation(particle):
    assert isinstance(particle, BubbleChamberParticle)
    assert isinstance(particle.transformation, TransformController)
    assert isinstance(particle.transformation.output, list)
    assert particle.transformation.output == []
