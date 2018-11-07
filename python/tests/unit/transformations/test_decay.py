import pytest
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations.types import Transformation, Decay, DecayKinematics
from testparticles import DecayParticle

test_3body = [  (DecayParticle("mu-", p=2.0),0),
                (DecayParticle("eta", p=1.0),1),
                (DecayParticle("K+", p=1.0),3)]

test_2body = [  (DecayParticle("pi-", p=2.0)),
                (DecayParticle("pi+", p=2.0)),
                (DecayParticle("K-", p=2.0)),
                (DecayParticle("K+", p=2.0))]

@pytest.mark.parametrize("particle",test_2body)
def test_decay_calculations(particle):
    target = None
    finallist = []
    for part in particle.transformation.selectedChannel:
        finallist.append(UndercoverParticle(part))
    calculations = DecayKinematics(particle,target,finallist)._calculations

    assert calculations._initialparticleCM.p == 0
    assert calculations._p < particle.p


@pytest.mark.skip
@pytest.mark.parametrize("particle",test_2body )
def test_2body_decay_basics(particle):
    finalparticlesNames = Transformation.channelListToNames(particle.decay_channels)[0][1]
    assert len(finalparticlesNames) == 2
    finalparticles = []
    for part in finalparticlesNames:
        finalparticles.append(UndercoverParticle(part))

    output = LAB2BodyDecay(particle, None, finalparticles).values
    assert isinstance(output,list)
    assert len(output) == 2
    for outputpart in output:
        assert outputpart.name in finalparticlesNames
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E
    #we need a test for ouput particles in the same plane

@pytest.mark.skip
@pytest.mark.parametrize("particle",test_2body )
def test_2body_decay_conservation(particle, conservation, resolution):
    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)

@pytest.mark.skip
@pytest.mark.parametrize("particle, id",test_3body )
def test_3body_decay_basics(particle, id):
    finalparticlesNames = Transformation.channelListToNames(particle.decay_channels)[id][1]
    assert len(finalparticlesNames) == 3
    finalparticles = []
    for part in finalparticlesNames:
        finalparticles.append(UndercoverParticle(part))
    output = LAB3BodyDecay(particle, finalparticles).values

    assert isinstance(output,list)
    assert len(output) == 3
    for outputpart in output:
        assert outputpart.name in finalparticlesNames
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E
    #we need a test for ouput particles in the same plane

@pytest.mark.skip
@pytest.mark.parametrize("particle, id",test_3body )
def test_3body_decay_conservation(particle, id, conservation, resolution):
    for attr in ['Pt','E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
