import pytest
from phenomena.particles import Particle
from phenomena.particles.models import UndercoverParticle, BubbleChamberParticle, QuantumUniverseParticle

particle_noparent = [   (QuantumUniverseParticle("e+")),
                        (QuantumUniverseParticle("e+", p = 3.0)),
                        (BubbleChamberParticle("e+")),
                        (BubbleChamberParticle("e+", p = 3.0))
                ]

particle_parent = [ (QuantumUniverseParticle("e+",2)),
                    (QuantumUniverseParticle("e+", 2, p=2.0)),
                    (BubbleChamberParticle("e+",2)),
                    (BubbleChamberParticle("e+", 2, p=2.0))
                ]

@pytest.mark.parametrize("particle",particle_noparent)
def test_no_parent(particle):
    assert isinstance(particle, Particle)
    assert particle.parent == -1
    assert isinstance(particle.id, int)

@pytest.mark.parametrize("particle",particle_parent)
def test_parent(particle):
    assert isinstance(particle, Particle)
    assert particle.parent == 2
    assert isinstance(particle.id, int)
