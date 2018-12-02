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
    assert TC.isLeptonNeutrino() == False

    # part2 = BubbleChamberParticle('W+')
    # for channel in part2.decay_channels:
    #     a = TransformationChannel(channel[0], channel[1])
    #     print a.names, a.isLeptonNeutrino()



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
            (['e-', 'nu_ebar']),
            (['e+', 'nu_e']),
            (['e-', 'e+']),
            (['pi+', 'pi-']),
            ]

@pytest.mark.parametrize("decay",decays)
def test_alldecays(decay):
    alldecays = AllDecays()
    assert isinstance(alldecays,AllDecays)
    assert isinstance(alldecays._allDecaysinDB, list)
    assert isinstance(alldecays._allDecaysinDB[0], AllDecays.ParticleDecayChannels)
    assert isinstance(alldecays._allDecaysinDB[0].decayChannels, TransformationChannels)
    assert isinstance(alldecays._allDecaysinDB[0].decayChannels.all, list)
    assert isinstance(alldecays._allDecaysinDB[10].decayChannels.all[1], TransformationChannel)

    #a = TransformationChannel(1,[11,22])
    #print a.isLeptonNeutrino()
    for item in alldecays.getParticlesfromDecay(decay):
        print item.name
