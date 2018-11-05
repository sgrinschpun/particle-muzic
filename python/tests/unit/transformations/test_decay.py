import pytest
from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, NO_PARENT, ParticleData, ParticlePosition, ParticleBoost, ParticleTransformation
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.transformations.types import Transformation, Decay
from phenomena.particles.transformations.kinematics.decay._3body import LAB3BodyDecay
from phenomena.particles.transformations.kinematics.decay._2body import LAB2BodyDecay



class DecayParticle(ParticleTransformation, ParticleBoost, ParticleData):
    TRANSFORMATIONS = [Decay]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        #### ParticleData
        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]
        self._set_decayChannels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...]

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters

        ### ParticleTransformation
        self._setTransformationManager(self, DecayParticle.TRANSFORMATIONS)

test_3body = [  (DecayParticle("mu-", p=2.0),0),
                (DecayParticle("eta", p=1.0),1),
                (DecayParticle("K+", p=1.0),3)]

test_2body = [  (DecayParticle("pi-", p=2.0)),
                (DecayParticle("pi+", p=2.0)),
                (DecayParticle("K-", p=2.0)),
                (DecayParticle("K+", p=2.0))]


@pytest.mark.parametrize("particle",test_2body )
def test_2body_decay_basics(particle):
    finalparticlesNames = Transformation.channelListToNames(particle.decay_channels)[0][1]
    assert len(finalparticlesNames) == 2
    finalparticles = []
    for part in finalparticlesNames:
        finalparticles.append(UndercoverParticle(part))

    output = LAB2BodyDecay(particle, finalparticles).values
    assert isinstance(output,list)
    assert len(output) == 2
    for outputpart in output:
        assert outputpart.name in finalparticlesNames
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E
    #we need a test for ouput particles in the same plane

@pytest.mark.parametrize("particle",test_2body )
def test_2body_decay_conservation(particle, conservation, resolution):
    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)

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


@pytest.mark.parametrize("particle, id",test_3body )
def test_3body_decay_conservation(particle, id, conservation, resolution):
    for attr in ['Pt','E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
