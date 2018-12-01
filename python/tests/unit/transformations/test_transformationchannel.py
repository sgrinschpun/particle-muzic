import pytest
from phenomena.particles.models import BubbleChamberParticle
from phenomena.particles.transformations.transformationchannel import TransformationChannel, TransformationChannels, AllDecays

@pytest.mark.skip
def test_TransformationChannel():
    part = BubbleChamberParticle('mu+')
    BR = part.decay_channels[0][0]
    particles = part.decay_channels[0][1]
    TC = TransformationChannel(BR, particles)
    assert isinstance(TC,TransformationChannel)
    assert TC.BR == BR
    assert TC.ids == particles
    assert TC.names != particles
    assert TC.length == 3
    assert TC.nameSet == set(['nu_e', 'e+', 'nu_mubar'])
    assert TC.totalCharge == 1
    assert TC.leptonNumber.total == -1
    print TC.leptonNumber.list
    print TC.isLeptonNeutrino()

particles = [   (BubbleChamberParticle("mu+")),
                (BubbleChamberParticle("pi0")),
                (BubbleChamberParticle("Lambda0"))
]

@pytest.mark.skip
@pytest.mark.parametrize("particle",particles)
def test_TransformationChannels(particle):
    TCS = TransformationChannels.from_pdt(particle.decay_channels)
    assert isinstance(TCS.all, list)
    print TCS.all
    assert isinstance(TCS.getChannel(0),TransformationChannel)
    print TCS.getChannel(0)
    print TCS.length
    print TCS.mostProbable.names
    print TCS.getChannel(['gamma', 'gamma'])
    print TCS.getChannel(1)
    print TCS.lengthCut(2)
    print TCS.lengthSelection(3)

decays = [  (['gamma', 'gamma']),
            (['e-', 'nu_ebar'])]
@pytest.mark.parametrize("decay",decays)
def test_alldecays(decay):
    alldecays = AllDecays()
    assert isinstance(alldecays,AllDecays)
    assert isinstance(alldecays._allDecaysinDB, list)
    assert isinstance(alldecays._allDecaysinDB[0], AllDecays.ParticleDecayChannels)
    assert isinstance(alldecays._allDecaysinDB[0].decayChannels, TransformationChannels)
    assert isinstance(alldecays._allDecaysinDB[0].decayChannels.all, list)
    assert isinstance(alldecays._allDecaysinDB[10].decayChannels.all[1], TransformationChannel)

    print alldecays.getParticlesfromDecay(decay)
