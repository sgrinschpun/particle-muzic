from __future__ import division
import math

from phenomena.particles.particle import ParticleDT
from skhep.constants import c_light

#https://github.com/afedynitch/ParticleDataTool

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

class ParticleDataToolFetcher(object):

    @staticmethod
    def getName(pdgid):
        return pythia.name(pdgid)

    @staticmethod
    def getMass(pdgid):
        return pythia.mass(pdgid)

    @staticmethod
    def getCharge(pdgid):
        return pythia.charge(pdgid)

    @staticmethod
    def getPDGId(name):
        return pythia.pdg_id(name)

    @staticmethod
    def getTau(pdgid):
        tau = pythia.ctau(pdgid)/c_light
        if math.isnan(tau) or math.isinf(tau):
            tau = ParticleDT.STABLE
        return tau

    @staticmethod
    def getDecayChannels(name):
        try:
            decaychannels = pythia.decay_channels(name)
        except:
            decaychannels =[]
        return decaychannels

    @staticmethod
    def getCTau(pdgid):
        return pythia.ctau(pdgid)
