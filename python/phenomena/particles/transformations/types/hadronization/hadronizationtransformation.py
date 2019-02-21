import math
from .phenomena.particles.transformations.transformationchannel import TransformationChannels
from .phenomena.particles.transformations.types import Transformation
from .phenomena.particles.sources import ParticleDataSource
from .hadronizationdata import HadronizationData

class Hadronization(Transformation):

    TARGET = None
    INPUT = ['u', "ubar", "d", "dbar","c","cbar","s","sbar","b","bar"]

    def __init__(self, particle):
        self._particle = particle
        self._values = {}
        if  self._particle.name in Hadronization.INPUT:
        #if  self._particle.name in HadronizationData.listOriginParticles():
            self._buildTransfValues()

    def _transformationChannels(self):
        hadronizationlist = HadronizationData.allParticles(self._particle.name)
        return TransformationChannels.from_decaylistNames(hadronizationlist)


    def getProbability(self, dt=1./60.):
        return 1
