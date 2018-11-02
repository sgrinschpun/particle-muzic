from phenomena.particles.transformations.kinematics.decay import DecayKinematics
from phenomena.particles.transformations.kinematics.elastic import ElasticKinematics
from phenomena.particles.transformations.kinematics.inelastic import InelasticKinematics

buildType = {
'ComptonEffect': 'Elastic',
'ElasticCollisionWithProton': 'Elastic',
'ElasticCollisionWithElectron': 'Elastic',
'ElasticCollisionWithNeutron': 'Elastic',
'PairProduction': 'Inelastic',
'Annihilation': 'Inelastic',
'InelasticCollisionWithProton': 'Inelastic',
'InelasticCollisionWithNeutron': 'Inelastic',
'Decay':  'Decay'
}


class KinematicsController(object):

    def __init__(self, particle):
        self._set_initial(particle)
        self._set_target(particle)
        self._set_final(particle)
        self._set_kinematicstype(particle)

    def _set_initial(self,particle):
        self._initial = particle

    def _set_target(self,particle):
        if particle.transformation.target != None:
            self._target = UndercoverParticle(particle.transformation.target)

    def _set_final(self,particle):
        finallist = []
        for part in particle.transformation.selectedChannel:
            finallist.append(UndercoverParticle(part))
        self._final = finallist

    def _set_kinematicstype(self, particle):
        type = particle.transformation.selectedType
        if buildType[type] == 'Elastic':
            self._buildElasticValues()
        elif buildType[type] == 'Inelastic':
            self._buildInelasticValues()
        elif buildType[type] == 'Decay':
            self._buildDecayValues()

    def _buildElasticValues(self):
        self._finalState = ElasticKinematics(self._initial, self._target, self._final).getFinalState()

    def _buildInelasticValues(self):
        self._finalState = InelasticKinematics(self._initial, self._target, self._final).getFinalState()

    def _buildDecayValues(self):
        self._finalState = DecayKinematics(self._initial, self._final).getFinalState()

    def getFinalState(self):
        return self._finalState

from phenomena.particles.mixins import ParticleData, ParticleBoost

class UndercoverParticle(ParticleBoost, ParticleData):
    '''
    This particle class is only used when we need to consider interaction with particles that are not logged in the server. for example, interaction with protons in the bubble chamber.
    '''

    def __init__(self, name, **kwargs):
        #### ParticleData
        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition()

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters
