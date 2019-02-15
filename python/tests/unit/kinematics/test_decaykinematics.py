import pytest
from phenomena.particles.models import QuantumUniverseVirtualParticle,QuantumUniverseParticle
from phenomena.particles.models.undercoverparticle import UndercoverParticle
from phenomena.particles.transformations.types.decays.decaykinematics import DecayKinematics, LAB2BodyDecay, LAB3BodyDecay

testparticle = [#(QuantumUniverseParticle("mu-", p= 1)),
                (QuantumUniverseParticle("mu-", p= 1)),
]

@pytest.mark.parametrize("particle",testparticle)
def test_decaykinematics(particle):
    initial = particle
    target = None
    final = map(UndercoverParticle, particle.transformation.selectedChannel)

    LAB3 = LAB3BodyDecay(particle,target,final)
    assert isinstance(LAB3,LAB3BodyDecay)

    print LAB3._initialparticleLAB.fourMomentum
    print LAB3._initialparticleCM.fourMomentum
    assert LAB3._finalparticlesCM !=  LAB3._finalparticlesLAB
    for index, itemCM in enumerate(LAB3._finalparticlesCM):
        itemLAB = LAB3._finalparticlesLAB[index]
        assert itemCM.fourMomentum.vector != itemLAB.fourMomentum.vector
        print itemCM.name, itemCM.fourMomentum.vector, itemLAB.fourMomentum.vector


    #DK = DecayKinematics(particle,target,final)

    #assert isinstance(DK,DecayKinematics)
