from __future__ import division
import math

from phenomena.particles.particle import Particle
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
        print "wwwwwwww", tau
        if math.isnan(tau) or math.isinf(tau):
            tau = Particle.STABLE
        print "xxxxxx", tau
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
