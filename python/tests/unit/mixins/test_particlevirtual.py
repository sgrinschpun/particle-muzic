import pytest
from phenomena.particles import Particle
from phenomena.particles.models import UndercoverParticle, BubbleChamberParticle, QuantumUniverseParticle, QuantumUniverseVirtualParticle


virtualparticles = [(QuantumUniverseVirtualParticle({'name':"W+",'mass':3.0})),
                    (QuantumUniverseVirtualParticle({'name':"W+",'mass':3.0, 'decay':[(0.321369, [-1, 2])]})),
                    (QuantumUniverseVirtualParticle({'name':"W+",'mass':3.0, 'decay':[-1, 2]}))
                ]
nonvirtualparticles = [(QuantumUniverseVirtualParticle("W+"))
                ]
@pytest.mark.parametrize("particle", virtualparticles)
def test_virtual(particle):
    nonvirtualversion = QuantumUniverseParticle(particle.name)
    assert isinstance(particle, Particle)
    assert isinstance(particle.name, str)
    assert isinstance(particle.mass, float)
    assert particle.virtuality == 1
    assert isinstance(particle.decay_channels, list)
    assert particle.decay_channels != []
    assert particle.mass != nonvirtualversion.mass
    assert particle.decay_channels !=nonvirtualversion.decay_channels

    print particle.decay_channels
    print nonvirtualversion.decay_channels

@pytest.mark.parametrize("particle", nonvirtualparticles)
def test_nonvirtual(particle):
    assert isinstance(particle, Particle)
    assert isinstance(particle.name, str)
    assert isinstance(particle.mass, float)
    assert particle.virtuality == 0
    assert isinstance(particle.decay_channels, list)
    assert particle.decay_channels != []
