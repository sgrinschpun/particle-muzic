from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, NO_PARENT, ParticleData, ParticlePosition, ParticleBoost, ParticleTransformation
from phenomena.particles.transformations.types import ComptonEffect, PairProduction, Annihilation, InelasticCollisionWithProton,InelasticCollisionWithNeutron, Decay, ElasticCollisionWithProton, ElasticCollisionWithElectron, ElasticCollisionWithNeutron, NoTransformation

class TestParticle(ParticleTransformation, ParticleBoost, ParticleData):

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

class AnnihilationParticle(TestParticle):
    TRANSFORMATIONS = [Annihilation]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(AnnihilationParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, AnnihilationParticle.TRANSFORMATIONS)

class PairProductionParticle(TestParticle):
    TRANSFORMATIONS = [PairProduction]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(PairProductionParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, PairProductionParticle.TRANSFORMATIONS)

class ComptonParticle(TestParticle):
    TRANSFORMATIONS = [ComptonEffect]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(ComptonParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, ComptonParticle.TRANSFORMATIONS)

class DecayParticle(TestParticle):
    TRANSFORMATIONS = [Decay]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(DecayParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, DecayParticle.TRANSFORMATIONS)

class ElasticParticle(TestParticle):
    TRANSFORMATIONS = [ElasticCollisionWithProton, ElasticCollisionWithElectron, ElasticCollisionWithNeutron]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(ElasticParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, ElasticParticle.TRANSFORMATIONS)

class InelasticParticle(TestParticle):
    TRANSFORMATIONS = [InelasticCollisionWithProton,InelasticCollisionWithNeutron]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(InelasticParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, InelasticParticle.TRANSFORMATIONS)

class NoTransformationParticle(TestParticle):
    TRANSFORMATIONS = [NoTransformation]

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        super(NoTransformationParticle, self).__init__(name, parent = NO_PARENT, **kwargs)
        self._setTransformationManager(self, NoTransformationParticle.TRANSFORMATIONS)
