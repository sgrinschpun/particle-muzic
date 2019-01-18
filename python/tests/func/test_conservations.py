import pytest
from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseVirtualParticle, QuantumUniverseParticle


test_particles = [  #(BubbleChamberParticle("phi")),
                    #(QuantumUniverseParticle("phi")),
                    (QuantumUniverseVirtualParticle("mu-", p=1.0)),
                    # (BubbleChamberParticle("mu-")),
                    # (QuantumUniverseParticle("mu-")),
                    # (QuantumUniverseVirtualParticle("mu-")),
                    # (BubbleChamberParticle("pi-", p=2.0)),
                    # (QuantumUniverseParticle("pi-", p=2.0)),
                    # (QuantumUniverseVirtualParticle("pi-", p=2.0)),
                    # (BubbleChamberParticle("pi-")),
                    # (QuantumUniverseParticle("pi-")),
                    # (QuantumUniverseVirtualParticle("pi-")),
]

@pytest.mark.parametrize("particle",test_particles)
def test_elasticcollision_conservation(particle, conservation, resolution):
    print particle.name, particle.transformation.selectedChannel
    for attr in ['E', 'charge', 'baryonnumber', 'leptonnumber']:
        #print attr
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
    for attr in ['P']:
        print attr, getattr(conservation.In,attr), getattr(conservation.Out,attr)
        assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)
