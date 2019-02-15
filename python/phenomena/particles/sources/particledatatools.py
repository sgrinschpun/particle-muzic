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
        try:
            width = lifetime_to_width(tau / u.picosecond)
        except:
            width = 0
        return width / u.GeV

    @staticmethod
    def getParticleList():
        '''Get the list of al particles in the DB'''
        return pythia.iteritems()

    @staticmethod
    def decayListToNames(decaylist):
        '''Change ids for names in decay lists'''
        allchannels_list = []
        for channel in decaylist:
            thischannels_list = []
            for particle in channel[1]:
                thischannels_list.append(ParticleDataToolFetcher.getName(particle))
            allchannels_list.append((channel[0],thischannels_list))
        return allchannels_list

    @staticmethod
    def getDecayChannelsWithNames(name):
        '''Substitute the ids of the particles for their names in the decay_channel'''
        pdgid = ParticleDataToolFetcher.getPDGId(name)
        pdgid_list = ParticleDataToolFetcher.getDecayChannels(pdgid)
        return ParticleDataToolFetcher.decayListToNames(pdgid_list)

    @staticmethod
    def getDecayParticles(name):
        '''Given a particle name, return all the particles it decay to'''
        pdgid = ParticleDataToolFetcher.getPDGId(name)
        decaylist = ParticleDataToolFetcher.getDecayChannels(pdgid)
        particle_list = []
        for channel in ParticleDataToolFetcher.decayListToNames(decaylist):
            particle_list.append(channel[1])
        return particle_list


    @staticmethod
    def getOriginParticles(listofdecayedparticles):
        '''Given a list of particle names, search for particles that decay into these'''
        pdgid_list = map(ParticleDataToolFetcher.getPDGId, listofdecayedparticles)
        part_list = []
        for item in ParticleDataToolFetcher.getParticleList():
         channels = ParticleDataToolFetcher.getDecayChannels(item[0])
         for channel in channels:
             if set(pdgid_list) == set(channel[1]):
                 part_list.append((channel[0],[item[1].name]))
        return part_list

    @staticmethod
    def getBR(originparticle, listofdecayedparticles):
        '''Given a particle and the particles it decays to, return the BR of that channel'''
        pdgid_origin = ParticleDataToolFetcher.getPDGId(originparticle)
        pdgid_list = map(ParticleDataToolFetcher.getPDGId, listofdecayedparticles)
        channels = ParticleDataToolFetcher.getDecayChannels(pdgid_origin)
        for channel in channels:
            if set(pdgid_list) == set(channel[1]):
                BR = channel[0]
                return BR

    @staticmethod
    def getChannel(particle, id):
        'get a specific channel from decay values'
        return ParticleDataToolFetcher.getDecayParticles(particle)[id]


    @staticmethod
    def getNdecays(integer):
        '''Get all the particles that decay to integer = 2 or 3 or .. particles'''
        part_list = []
        for item in ParticleDataToolFetcher.getParticleList():
         channels = ParticleDataToolFetcher.getDecayChannels(item[0])
         for channel in channels:
             if len(channel[1]) == integer and channel[0] != 0.0:
                 part_list.append(item[1].name)
        return part_list
