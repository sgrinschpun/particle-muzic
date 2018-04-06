from __future__ import division
import abc

import sys
import os

import random
import math
import json
import textwrap
from operator import itemgetter

import numpy as np

sys.path.insert(0, '../')

#ParticleDataTool gives us the decay channels
from ParticleDataTool import ParticleDataTool as pdt
pythia = pdt.PYTHIAParticleData(file_path='ParticleData.ppl', use_cache=True)

#PYPDT gives us info about mass, charge, lifetime
import pypdt
tbl = pypdt.ParticleDataTable()
part_dict = {}
for p in tbl:
    part_dict[p.name]= p.id

#particle_extra_info gives us information about composition, interactions, type,...
def str_hook(obj):    # this is to convert unicodes to strings in json load. copied from somewhere. doe snot work very well
    return {k.encode('utf-8') if isinstance(k,unicode) else k :
            v.encode('utf-8') if isinstance(v, unicode) else v
            for k,v in obj}
path = 'particle_extra_info/part_extra_info.json'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, path)
particle_extra_info = json.load(open(filename), object_pairs_hook=str_hook)

class Particle(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def mass(self):
        pass

    @abc.abstractmethod
    def charge(self):
        pass

class ParticleDT(Particle):

    def __new__(cls, *args, **kw):
        if args[0] in ['u','d','c','s','t','b']:
            return super(ParticleDT, cls).__new__(cls)
        else:
            try:
                part_dict[args[0]]
                return super(ParticleDT, cls).__new__(cls)
            except Exception, ex:
                raise Exception("Exception: {0}".format(ex.message))

    class_counter= 0

    def __init__(self, name):
        self.__set_name(name)  # Name of the particle pypdt convention
        self.__set_id() # Class Counter
        self.__set_pdgid(name) # Id from PDG, taken from pypdt
        self.__set_mass() # Mass of the particle in GeV, taken from pypdt
        self.__set_charge() # Charge of the particle, taken from pypdt
        self.__set_lifetime() # Lifetime of the particle, taken from pypdt
        self.__set_decay_channels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...] from ParticleDataTool
        self.__set_type() # Particle Type (quark, lepton, bosoon, meson, baryon) taken from json
        self.__set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json. Check unicode vs string

        self.__set_decay() # Particle decay channel chosen
        self.__set_timetodecay() # Particle time lived before decay, renormalized


    @property
    def name(self):
        return self.__name
    def __set_name(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id
    def __set_id(self):
        self.__id = ParticleDT.class_counter
        ParticleDT.class_counter += 1

    @property
    def pdgid(self):
        return self.__pdgid
    def __set_pdgid(self, name):
        self.__pdgid = part_dict[name]

    @property
    def mass(self):
        return self.__mass
    def __set_mass(self):
        self.__mass= tbl[self.__pdgid].mass

    @property
    def charge(self):
        return self.__charge
    def __set_charge(self):
        self.__charge= tbl[self.__pdgid].charge

    @property
    def lifetime(self):
        return self.__lifetime
    def __set_lifetime(self):
        self.__lifetime= tbl[self.__pdgid].lifetime

    @property
    def decay_channels(self):
        return self.__decay_channels
    def __set_decay_channels(self):
        try:
            self.__decay_channels = pythia.decay_channels(self.__pdgid)
        except:
            self.__decay_channels = []

    @property
    def type(self):
        return self.__type
    def __set_type(self):
        self.__type= particle_extra_info[str(self.__pdgid)]['type']

    @property
    def composition(self):
        return self.__composition
    def __set_composition(self):
        self.__composition= particle_extra_info[str(self.__pdgid)]['composition']

    @property
    def decay(self):
        return self.__decay
    def __set_decay(self):
        list_decay = []
        if self.__decay_channels != []:
            try:
                choice = self._weightedChoice(self._buildWeights()[0],self._buildWeights()[1])
                channels = self.__decay_channels[choice][1]
                for part in channels:
                    list_decay.append(ParticleDT.apdgid(part).name)
            finally:
                self.__decay = list_decay
        else:
            self.__decay = []

    @property
    def timetodecay(self):
        return self.__timetodecay
    def __set_timetodecay(self): #this is just a proof of concept. need to be improved
        if self.__lifetime != None :
            self.__timetodecay = ParticleDT.renormalizeTime(ParticleDT.magnitude(self._nextDecay()))
        else:
            self.__timetodecay = 'stable'  # mixing strings with floats ???

    @staticmethod
    def apdgid(partid):
        partid = str(partid)
        if pypdt.get(partid) != None:
            return pypdt.get(partid)
        else:
            if partid[0] == '-':
                return pypdt.get(partid[1:])
            else:
                return ValueError("Id not found")

    @staticmethod
    def magnitude(x):
        return int(math.log10(x))

    @staticmethod
    def renormalizeTime(n):
        # range 1 & 2 define the renormalization. Needs to be improved.
        range1=[-13,14]
        range2=[1e-3,5]
        delta1 = range1[1] - range1[0]
        delta2 = range2[1] - range2[0]
        return np.around((delta2 * (n - range1[0]) / delta1) + range2[0],2)

    def _buildWeights(self):
        seq = []
        weights=[]
        for index, item in enumerate(self.__decay_channels):
            if item[0] != 0.0:           # do not use channels with prob = 0.0
                seq.append(index)
                weights.append(item[0])
        return seq, weights

    def _weightedChoice(self, seq, weights):
        assert len(weights) == len(seq)
        #assert abs(1. - sum(weights)) < 1e-6
        x = random.random()
        for i, elmt in enumerate(seq):
            if x <= weights[i]:
                return elmt
            x -= weights[i]

    def _nextDecay(self):   #this is picosecons, needs to be normalized
        if self.__lifetime != None:
            return random.expovariate(1/self.__lifetime)


    def getChannelNames(self):
        dc_names = []
        if self.__decay_channels != []:
            for item in self.__decay_channels:
                if item[0] != 0.0:            # do not use channels with prob = 0.0
                    part_names =[]
                    for part in item[1]:
                        part_names.append(ParticleDT.apdgid(part).name)     # use apdgid to process particles that are their own antiparticle
                    dc_names.append(tuple([item[0], part_names]))
            return sorted(dc_names,key=itemgetter(0), reverse=True)
        else:
            return dc_names

    def getDecayTreeAll(self, leaf = 1):
        wrapper1 = textwrap.TextWrapper(initial_indent='-'*leaf, width=70)
        wrapper2 = textwrap.TextWrapper(initial_indent='-'*(leaf+1), width=70)
        channel_names = self.getChannelNames()
        if self.__decay_channels !=[]:
            for index, channel in enumerate(channel_names):
                print wrapper1.fill('Channel {} : {}'.format(index, channel[0]))
                for part in channel[1]:
                    print wrapper2.fill(part)
                    ParticleDT(part).getDecayTreeAll(leaf+1)
        else:
            print wrapper2.fill('Stable')

    def getDecayTreeRandom(self, leaf=1):
        wrapper = textwrap.TextWrapper(initial_indent='-'*leaf, width=70)
        channel_names = self.getChannelNames()
        if self.__decay_channels !=[]:
            choice = self._weightedChoice(self._buildWeights()[0],self._buildWeights()[1])
            channel = channel_names[choice][1]
            for part in channel:
                print wrapper.fill(part)
                ParticleDT(part).getDecayTreeRandom(leaf+1)
        else:
            print wrapper.fill('Stable')



if __name__ == '__main__':
    particle = ParticleDT("pi-")
    print particle.name
    print particle.charge
    new_particles = particle.decay
    for particle in new_particles:
        print particle.name
