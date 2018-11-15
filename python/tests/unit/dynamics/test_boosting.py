import pytest
from phenomena.particles.models import UndercoverParticle, BubbleChamberParticle
from skhep.math  import Vector3D, LorentzVector

undercover_particles = [(UndercoverParticle("pi-", p=0.01))]

@pytest.mark.parametrize("particle",undercover_particles)
def test_Boosting(particle):
    fourMomentum0 = particle.fourMomentum.copy()
    assert isinstance(fourMomentum0, LorentzVector)
    assert isinstance(fourMomentum0.boostvector, Vector3D)
    print fourMomentum0.vector
    print fourMomentum0.boostvector
    print fourMomentum0.vector/(particle.mass*fourMomentum0.gamma)
    fourMomentum1 = fourMomentum0.boost(-1*Vector3D(0.34,0,0))
    print "1", fourMomentum1.boostvector
    fourmomentum2= fourMomentum0.boost(fourMomentum0.boostvector)
    print "2,1", fourmomentum2.boostvector
    fourmomentum2= fourmomentum2.boost(-1*Vector3D(0.34,0,0))
    print "2,2", fourmomentum2.boostvector
