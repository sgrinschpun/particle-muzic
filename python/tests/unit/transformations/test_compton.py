import pytest
from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, NO_PARENT, ParticleData, ParticlePosition, ParticleBoost, ParticleTransformation
from phenomena.particles.transformations.types import Transformation, ComptonEffect

class ComptonParticle(ParticleTransformation, ParticleBoost, ParticleData):
    TRANSFORMATIONS = [ComptonEffect]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        #### ParticleData
        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters

        ### ParticleTransformation
        self._setTransformationManager(self, ComptonParticle.TRANSFORMATIONS)

test_particles = [(ComptonParticle("gamma", p=2.0))]


@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_basics(particle):
    assert particle.name == "gamma"
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='ComptonEffect']
    assert thisType[0]['target'] == 'e-'
    assert set(thisType[0]['list'][0][1]) == set(['gamma', 'e-'])

    output = particle.transformation.output
    assert len(output) == 2

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_comptoneffect_conservation(particle, conservation, resolution, print_particle):
    print_particle

    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
