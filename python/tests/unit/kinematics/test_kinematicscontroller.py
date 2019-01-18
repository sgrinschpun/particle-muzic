import pytest
from phenomena.particles.models import QuantumUniverseVirtualParticle,QuantumUniverseParticle
from phenomena.particles.models.undercoverparticle import UndercoverParticle, VirtualUndercoverParticle
from phenomena.particles.transformations import KinematicsController, VirtualKinematicsController
from phenomena.particles import ServerParticle

testparticle = [(QuantumUniverseVirtualParticle("mu-", p= 1)),
                (QuantumUniverseVirtualParticle("mu-", p= 0.0001, theta=1, phi = 0.7)),
]

@pytest.mark.parametrize("particle",testparticle)
def test_virtualkinematicscontroller(particle):
    VKC = VirtualKinematicsController(particle)
    assert isinstance(VKC, VirtualKinematicsController)
    assert isinstance(VKC._initial, QuantumUniverseVirtualParticle)
    assert VKC._initial == particle
    assert VKC._target == None
    for item in VKC._final:
        assert item.__class__ in [UndercoverParticle,VirtualUndercoverParticle]
    for item in VKC._finalState:
        assert item.__class__ in [UndercoverParticle,VirtualUndercoverParticle]
    finalp = VKC._finalState[0].fourMomentum + VKC._finalState[1].fourMomentum
    assert round(finalp[0],4) == round(particle.fourMomentum.px,4)
    assert round(finalp[1],4) == round(particle.fourMomentum.py,4)
    assert round(finalp[2],4) == round(particle.fourMomentum.pz,4)

    SPlist = map(ServerParticle.fromparticle, VKC._finalState)
    finalp = SPlist[0].fourMomentum + SPlist[1].fourMomentum
    assert round(finalp[0],4) == round(particle.fourMomentum.px,4)
    assert round(finalp[1],4) == round(particle.fourMomentum.py,4)
    assert round(finalp[2],4) == round(particle.fourMomentum.pz,4)
    for item in SPlist:
        print item.name, item.p, item.theta, item.phi
