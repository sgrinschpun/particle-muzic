from __future__ import division
import math

from phenomena.particles.particle import Particle
from skhep.constants import c_light
from skhep import units as u
from skhep.math  import lifetime_to_width

#https://github.com/afedynitch/ParticleDataTool

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

class ParticleDataToolFetcher(object):

    @staticmethod
    def getName(pdgid):
        return pythia.name(pdgid)

    @staticmethod
    def getMass(pdgid):
        return pythia.mass(pdgid) * u.GeV

    @staticmethod
    def getCharge(pdgid):
        return pythia.charge(pdgid)

    @staticmethod
    def getPDGId(name):
        return pythia.pdg_id(name)

    @staticmethod
    def getTau(pdgid):
        c = c_light/(u.cm/u.s)
        tau = (ParticleDataToolFetcher.getCTau(pdgid)/u.cm)/c *u.s / u.picosecond
        if math.isnan(tau) or math.isinf(tau):
            tau = Particle.STABLE
        return tau

    @staticmethod
    def getDecayChannels(pdgid):
        try:
            decaychannels = pythia.decay_channels(pdgid)
        except:
            decaychannels =[]
        return decaychannels

    @staticmethod
    def getCTau(pdgid):
        return pythia.ctau(pdgid) * u.cm

    @staticmethod
    def getWidth(pdgid):
        tau = ParticleDataToolFetcher.getTau(pdgid) / u.picosecond
        width = lifetime_to_width(tau / u.picosecond)
        return width / u.GeV

    @staticmethod
    def getParticleList():
        return pythia.iteritems()
