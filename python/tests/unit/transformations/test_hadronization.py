import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations import TransformController
from phenomena.particles.transformations import TransformationChannels, TransformationChannel
from phenomena.particles.transformations.types import Transformation, TransformationValues
from phenomena.particles.transformations.types import Hadronization, HadronizationKinematics
from phenomena.particles.transformations.types.hadronization import LAB2BodyDecay
from testparticles import HadronizationParticle

test_hadronization = [
                (HadronizationParticle("u", p=0.1)),
                (HadronizationParticle("ubar", p=0.1)),
                (HadronizationParticle("d", p=0.1)),
                (HadronizationParticle("dbar", p=0.1)),
                (HadronizationParticle("c", p=0.1)),
                (HadronizationParticle("cbar", p=0.1)),
                (HadronizationParticle("s", p=0.1)),
                (HadronizationParticle("sbar", p=0.1)),
                (HadronizationParticle("b", p=0.1)),
                (HadronizationParticle("bbar", p=0.1)),
            ]

@pytest.mark.parametrize("particle",test_hadronization )
def test_hadronization_basics(particle):
    assert isinstance(particle.transformation,TransformController)
    assert isinstance(particle.transformation.allTypes,list)
    assert isinstance(particle.transformation.selectedType,TransformationValues)
    assert isinstance(particle.transformation.selectedType.channels,TransformationChannels)
    assert isinstance(particle.transformation._selectedChannel,TransformationChannel)
    assert isinstance(particle.transformation.selectedChannel,list)
    assert isinstance(particle.transformation.output,list)

    assert particle.transformation.selectedType.type == 'Hadronization'
    assert particle.transformation.selectedType.target == None
    #assert particle.transformation._selectedChannel.nameSet == set(['gamma', 'e-'])
    assert len(particle.transformation.output) == 2

@pytest.mark.skip
@pytest.mark.parametrize("particle",test_hadronization)
def test_hadronization_calculations(particle):
    target = None
    finallist = []
    for part in particle.transformation.selectedChannel:
        finallist.append(UndercoverParticle(part))
    calculations = HadronizationKinematics(particle,target,finallist)._calculations

    assert calculations._initialparticleCM.p == 0 # Initial at rest in CM
    vector0 = calculations._finalparticlesCM[0].fourMomentum.vector
    vector1 = calculations._finalparticlesCM[1].fourMomentum.vector
    assert vector0.isantiparallel(vector1) # final particles in CM are antiparallel
    eLAB_init = particle.E
    eCM_init = calculations._initialparticleCM.e
    eCM_final = calculations._finalparticlesCM[0].fourMomentum.e + calculations._finalparticlesCM[1].fourMomentum.e
    eLAB_final = calculations._finalparticlesLAB[0].fourMomentum.e + calculations._finalparticlesLAB[1].fourMomentum.e
    assert round(eCM_init,4) == round(eCM_final,4) #energy is conserved in the CM
    assert round(eLAB_init,4) == round(eLAB_final,4) #energy is conserved in the LAB


@pytest.mark.skip
@pytest.mark.parametrize("particle",test_hadronization )
def test_hadronization_conservation(particle, conservation, resolution):
    for attr in ['E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
    for attr in ['P']:
        assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)
