from phenomena.particles.transformations.types import ComptonKinematics, DecayKinematics, ElasticKinematics, InelasticKinematics, PairProductionKinematics, AnnihilationKinematics, HadronizationKinematics

from phenomena.particles.models.undercoverparticle import UndercoverParticle, VirtualUndercoverParticle

from phenomena.particles.transformations.types.decaysviavirtual.virtualparticlechannel import VirtualParticleChannel, RealInfo, VirtualInfo

KinematicsType = {
'ComptonEffect': ComptonKinematics,
'ElasticCollisionWithProton': ElasticKinematics,
'ElasticCollisionWithElectron': ElasticKinematics,
'ElasticCollisionWithNeutron': ElasticKinematics,
'PairProduction': PairProductionKinematics,
'Annihilation': AnnihilationKinematics,
'InelasticCollisionWithProton': InelasticKinematics,
'InelasticCollisionWithNeutron': InelasticKinematics,
'Decay': DecayKinematics,
'Hadronization': HadronizationKinematics
}

class KinematicsController(object):

    def __init__(self, particle):
        self._set_initial(particle)
        self._set_target(particle)
        self._set_final(particle)
        self._set_finalstate(particle)

    def _set_initial(self,particle):
        self._initial = particle

    def _set_target(self,particle):
        if particle.transformation.target != None:
            self._target = UndercoverParticle(particle.transformation.target)
        else:
            self._target = None

    def _set_final(self,particle):
        finallist = []
        for part in particle.transformation.selectedChannel:
            finallist.append(UndercoverParticle(part))
        self._final = finallist

    def _set_finalstate(self, particle):
        type = particle.transformation.selectedType.type
        self._finalState = KinematicsType[type](self._initial, self._target, self._final).getFinalState()

    def getFinalState(self):
        return self._finalState


class VirtualKinematicsController(KinematicsController):
    def __init__(self, particle):
        super(VirtualKinematicsController, self).__init__(particle)

    def _set_final(self,particle):
        finallist = []
        for part in particle.transformation._selectedChannel.particles:
            if isinstance(part, RealInfo):
                finallist.append(UndercoverParticle(part.name))
            elif isinstance(part, VirtualInfo):
                finallist.append(VirtualUndercoverParticle(part))
        self._final = finallist
