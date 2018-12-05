import pytest
from phenomena.particles.models import BubbleChamberParticle


test_particles = [  (BubbleChamberParticle("mu-", p=2.0)),
#                     (BubbleChamberParticle("pi+", p=2.0)),
#                     (BubbleChamberParticle("K-", p=2.0)),
#                     (BubbleChamberParticle("K+", p=2.0)),
#                     (BubbleChamberParticle("e-", p=2.0)),
#                     (BubbleChamberParticle("e+", p=2.0)),
#                     (BubbleChamberParticle("gamma", p=2.0)),
]

@pytest.mark.parametrize("particle",test_particles)
def test_elasticcollision_conservation(particle, conservation, resolution):
    #print_particle
    for attr in ['charge', 'baryonnumber', 'leptonnumber']:
        print attr
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
    # for attr in ['P']:
    #     assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)
