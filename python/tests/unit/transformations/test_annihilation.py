import pytest
from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, NO_PARENT, ParticleData, ParticlePosition, ParticleBoost, ParticleTransformation
from phenomena.particles.transformations.types import Transformation, Annihilation

class AnnihilationParticle(ParticleTransformation, ParticleBoost, ParticleData):
    TRANSFORMATIONS = [Annihilation]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        #### ParticleData
        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters

        ### ParticleTransformation
        self._setTransformationManager(self, AnnihilationParticle.TRANSFORMATIONS)

test_particles = [(AnnihilationParticle("e+", p=2.0))]



@pytest.mark.parametrize("particle",test_particles)
def test_annihilation_basics(particle):
    assert particle.name == "e+"
    alltypes = particle.transformation.allTypes
    thisType = [transf for transf in alltypes if transf['type']=='Annihilation']
    assert thisType[0]['target'] == 'e-'
    assert set(thisType[0]['list'][0][1]) == set(['gamma'])

    output = particle.transformation.output
    assert len(output) == 1

    for outputpart in output:
        assert isinstance(outputpart,UndercoverParticle)
        assert outputpart.E < particle.E

@pytest.mark.parametrize("particle",test_particles)
def test_annihilation_conservation(particle, conservation, resolution, print_particle):
    print_particle
    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
