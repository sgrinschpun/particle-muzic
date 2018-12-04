import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations import TransformController
from phenomena.particles.transformations import TransformationChannels, TransformationChannel
from phenomena.particles.transformations.types import Transformation, TransformationValues
from phenomena.particles.transformations.types import Transformation, Decay, DecayKinematics
from phenomena.particles.transformations.types.decays import LAB2BodyDecay, LAB3BodyDecay
from testparticles import DecayParticle

test_3body = [  (DecayParticle("mu-", p=2.0),0),

                ]

test_2body = [  (DecayParticle("pi-", p=2.0)),
                (DecayParticle("pi+", p=2.0)),
                (DecayParticle("pi0", p=2.0)),
            ]

@pytest.mark.parametrize("particle",test_2body )
def test_2body_decay_basics(particle):
    assert isinstance(particle.transformation,TransformController)
    assert isinstance(particle.transformation.allTypes,list)
    assert isinstance(particle.transformation.selectedType,TransformationValues)
    assert isinstance(particle.transformation.selectedType.channels,TransformationChannels)
    assert isinstance(particle.transformation._selectedChannel,TransformationChannel)
    assert isinstance(particle.transformation.selectedChannel,list)
    assert isinstance(particle.transformation.output,list)

    assert particle.transformation.selectedType.type == 'Decay'
    assert particle.transformation.selectedType.target == None
    #assert particle.transformation._selectedChannel.nameSet == set(['gamma', 'e-'])
    assert len(particle.transformation.output) == 2

@pytest.mark.parametrize("particle",test_2body)
def test_decay_calculations(particle):
    target = None
    finallist = []
    for part in particle.transformation.selectedChannel:
        finallist.append(UndercoverParticle(part))
    calculations = DecayKinematics(particle,target,finallist)._calculations

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


@pytest.mark.parametrize("particle",test_2body )
def test_2body_decay_conservation(particle, conservation, resolution):
    for attr in ['E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
    for attr in ['P']:
        assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)

@pytest.mark.parametrize("particle, id",test_3body )
def test_3body_decay_basics(particle, id):
    assert isinstance(particle.transformation,TransformController)
    assert isinstance(particle.transformation.allTypes,list)
    assert isinstance(particle.transformation.selectedType,TransformationValues)
    assert isinstance(particle.transformation.selectedType.channels,TransformationChannels)
    assert isinstance(particle.transformation._selectedChannel,TransformationChannel)
    assert isinstance(particle.transformation.selectedChannel,list)
    assert isinstance(particle.transformation.output,list)

    assert particle.transformation.selectedType.type == 'Decay'
    assert particle.transformation.selectedType.target == None
    assert len(particle.transformation.output) == 3

@pytest.mark.parametrize("particle, id",test_3body )
def test_3body_decay_conservation(particle, id, conservation, resolution):
    for attr in ['E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
    for attr in ['P']:
        assert getattr(conservation.In,attr) == getattr(conservation.Out,attr)
