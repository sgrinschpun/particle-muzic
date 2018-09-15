from __future__ import division
import math

from datasources import DataSourceFetcher
from phenomena.particles.particle import ParticleDT
from skhep.constants import c_light

#https://github.com/afedynitch/ParticleDataTool

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

class ParticleDataToolFetcher(DataSourceFetcher):

    def getMass(self, name):
        return pythia.mass(name)

    def getCharge(self, name):
        return pythia.charge(name)

    def getPDGId(self, name):
        return pythia.pdg_id(name)

    def getTau(self, name):
        tau = pythia.ctau(name)/c_light
        if math.isnan(tau) or math.isinf(tau):
            tau = ParticleDT.STABLE
        return tau
