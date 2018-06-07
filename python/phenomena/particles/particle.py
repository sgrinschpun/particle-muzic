from __future__ import division
import abc

import sys
import os

import random
import math
import json
import textwrap
from operator import itemgetter
import time, threading

import numpy as np

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
path = '/home/cristobal/Desenvolupament/OwnProjects/particle-muzik/particle_extra_info/part_extra_info.json'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, path)
particle_extra_info = json.load(open(filename))


class Particle(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def parent(self):
        pass

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def charge(self):
        pass

    @abc.abstractproperty
    def composition(self):
        pass

    @abc.abstractproperty
    def decay_time(self):
        pass

    @abc.abstractproperty
    def mass(self):
        pass

    @abc.abstractproperty
    def type(self):
        pass

    @abc.abstractmethod
    def toDictionary(self):
        pass

class BasicParticle(Particle):

    def __init__(self, parent, id, name, type, mass, charge, composition, decay_time):
        self._parent = parent
        self._id = id
        self._name = name
        self._type = type
        self._mass = mass
        self._composition = composition
        self._charge = charge
        self._decay_time = decay_time

    @property
    def name(self):
        return self._name

    @property
    def charge(self):
        return self._charge

    @property
    def composition(self):
        return self._composition

    @property
    def decay_time(self):
        return self._decay_time

    @property
    def mass(self):
        return self._mass

    @property
    def parent(self):
        return self._parent

    @property
    def type(self):
        return self._type

    def toDictionary(self):
        return {"name": self._name,
                "parent": self._parent,
                "id": self._id,
                "type": self._type,
                "mass": self._mass,
                "charge": self._charge,
                "decay_time": self._decay_time,
                "composition": self._composition}

NO_PARENT = -1
class ParticleDT(Particle):
    STABLE = -1

    def __new__(cls, *args, **kw):
        if args[0] in ['u','d','c','s','t','b']:
            return super(ParticleDT, cls).__new__(cls)
        else:
            try:
                part_dict[args[0]]
                return super(ParticleDT, cls).__new__(cls)
            except Exception, ex:
                raise Exception("Exception: {0}".format(ex.message))

    CLASS_COUNTER = 0

    def __init__(self, name, parent = NO_PARENT):
        self._set_name(name)  # Name of the particle pypdt convention
        self._set_id() # Class Counter
        self._set_pdgid(name) # Id from PDG, taken from pypdt
        self._set_mass() # Mass of the particle in GeV, taken from pypdt
        self._set_charge() # Charge of the particle, taken from pypdt
        self._set_lifetime() # Lifetime of the particle, taken from pypdt
        self._set_decay_channels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...] from ParticleDataTool
        self._set_type() # Particle Type (quark, lepton, bosoon, meson, baryon) taken from json
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json. Check unicode vs string
        self._set_lifetime_ren() #Renormalization of the lifetime
        self._set_decay() # Particle decay channel chosen
        self._set_time_to_decay()  # Particle time lived before decay, renormalized
        self._setParent(parent)

    @property
    def parent(self):
        return self._parent

    def _setParent(self, parent):
        self._parent = parent

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
        return int(math.log(x,10))


    @staticmethod
    def renormalize_time(n):
        # range 1 & 2 define the renormalization. Needs to be improved.
        range1 = [-13., 14.]
        range2 = [1.e-3, 5.]
        delta1 = range1[1] - range1[0]
        delta2 = range2[1] - range2[0]
        return np.around((delta2 * (n - range1[0]) / delta1) + range2[0], 2)

    @property
    def name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    def _set_id(self):
        self._id = ParticleDT.CLASS_COUNTER
        ParticleDT.CLASS_COUNTER += 1

    @property
    def pdgid(self):
        return self._pdgid

    def _set_pdgid(self, name):
        self._pdgid = part_dict[name]

    @property
    def mass(self):
        return self._mass

    def _set_mass(self):
        self._mass= tbl[self._pdgid].mass

    @property
    def charge(self):
        return self._charge

    def _set_charge(self):
        self._charge= tbl[self._pdgid].charge

    @property
    def lifetime(self):
        return self._lifetime

    def _set_lifetime(self):
        self._lifetime= tbl[self._pdgid].lifetime

    @property
    def lifetime_ren(self):
        return self._lifetime_ren

    def _set_lifetime_ren(self):
        if self._lifetime != None :
            self._lifetime_ren= ParticleDT.renormalize_time(ParticleDT.magnitude(self._lifetime))

    @property
    def decay_channels(self):
        return self._decay_channels

    def _set_decay_channels(self):
        try:
            self._decay_channels = pythia.decay_channels(self._pdgid)
        except:
            self._decay_channels = []

    @property
    def type(self):
        return self._type

    def _set_type(self):
        self._type= particle_extra_info[str(self._pdgid)]['type']

    @property
    def composition(self):
        return self._composition

    def _set_composition(self):
        #    for index, item in enumerate(particle_extra_info[str(self._pdgid)]['composition']):
        #        self._composition.append([])
        #        for quark in item:
        #            self._composition[index].append(quark.encode('utf-8'))
        self._composition =[]
        if particle_extra_info[str(self._pdgid)]['composition'] != []:
            for quark in particle_extra_info[str(self._pdgid)]['composition'][0]: #only consider first superposition of quarks
                self._composition.append(quark.encode('utf-8'))
        else:
            pass

    def _set_decay(self):
        list_decay = []
        if self._decay_channels != []:
            try:
                choice = self._weighted_choice(self._build_weights()[0],self._build_weights()[1])
                channels = self._decay_channels[choice][1]
                for part in channels:
                    #list_decay.append(ParticleDT(ParticleDT.apdgid(part).name))  this actually creates objects
                    list_decay.append(ParticleDT.apdgid(part).name)  # this just shows particles names
            finally:
                self.decay = list_decay
        else:
            self.decay = []

    @property
    def decay_time(self):
        return self._time_to_decay

    def _set_time_to_decay(self): #this is just a proof of concept. need to be improved
        if self._lifetime != None :
            self._time_to_decay = self._next_decay()
        else:
            #self._timetodecay = 'stable'  # mixing strings with floats ???
            self._time_to_decay = ParticleDT.STABLE

    def _build_weights(self):
        seq = []
        weights=[]
        for index, item in enumerate(self._decay_channels):
            if item[0] != 0.0:           # do not use channels with prob = 0.0
                seq.append(index)
                weights.append(item[0])
        return seq, weights

    def _weighted_choice(self, seq, weights):
        assert len(weights) == len(seq)
        #assert abs(1. - sum(weights)) < 1e-6
        x = random.random()
        for i, elmt in enumerate(seq):
            if x <= weights[i]:
                return elmt
            x -= weights[i]

    #Calculates next decay according to renormalized lifetime
    def _next_decay(self):
        #need to include a minimum of a milisecond
        if self._lifetime != None:
            return random.expovariate(1/self._lifetime_ren)

    #Callback  the timer trigger
    def decay_callback(self):
        print 'Decays to: %s in %s' % (self.decay, self._time_to_decay)

    #Timer trigger method
    def start(self, callback):
        if self._time_to_decay != ParticleDT.STABLE:
            wait_time = ParticleDT.renormalize_time(self._time_to_decay)
            print "Wait for: ", wait_time
            threading.Timer(wait_time, callback).start()
        else:
            print "Wait for: ", 10
            threading.Timer(10, callback).start()

    def get_channel_names(self):
        dc_names = []
        if self._decay_channels != []:
            for item in self._decay_channels:
                if item[0] != 0.0:            # do not use channels with prob = 0.0
                    part_names =[]
                    for part in item[1]:
                        part_names.append(ParticleDT.apdgid(part).name)     # use apdgid to process particles that are their own antiparticle
                    dc_names.append(tuple([item[0], part_names]))
            return sorted(dc_names,key=itemgetter(0), reverse=True)
        else:
            return dc_names

    def get_decay_tree_all(self, leaf = 1):
        wrapper1 = textwrap.TextWrapper(initial_indent='-'*leaf, width=70)
        wrapper2 = textwrap.TextWrapper(initial_indent='-'*(leaf+1), width=70)
        channel_names = self.get_channel_names()
        if self._decay_channels !=[]:
            for index, channel in enumerate(channel_names):
                print wrapper1.fill('Channel {} : {}'.format(index, channel[0]))
                for part in channel[1]:
                    print wrapper2.fill(part)
                    ParticleDT(part).get_decay_tree_all(leaf+1)
        else:
            print wrapper2.fill(ParticleDT.STABLE)

    def get_decay_tree_random(self, leaf=1):
        wrapper = textwrap.TextWrapper(initial_indent='-'*leaf, width=70)
        channel_names = self.get_channel_names()
        if self._decay_channels !=[]:
            choice = self._weighted_choice(self._build_weights()[0],self._build_weights()[1])
            channel = channel_names[choice][1]
            for part in channel:
                print wrapper.fill(part)
                ParticleDT(part).get_decay_tree_random(leaf+1)
        else:
            print wrapper.fill(ParticleDT.STABLE)

    def toDictionary(self):
        return {"name": self._name,
                "id": self._id,
                "type": self._type,
                "mass": self._mass,
                "charge": self._charge,
                "decay_time": self._time_to_decay,
                "composition": self._composition}

class ParticleBoosted(ParticleDT):
    c= 299792458 #m/s

    def __init__(self, name, p=0, E=0, theta=0): #initialize either with momentum (p) or energy (e)
        super(ParticleBoosted, self).__init__(name) #inherit properties from ParticleDT

        self._set_boostvalues(p,E)

        #check E can't be less than rest mass

    @staticmethod
    def beta_from_gamma(gamma):
        return np.sqrt(1-np.divide(1,np.square(gamma)))

    def _set_gamma_from_E(self):
        return np.divide(self._E,self.mass)

    def _set_gamma_from_p(self):
        return np.sqrt(1+np.square(np.divide(self._p,self.mass)))

    def _set_p_from_E(self):
        return np.multiply(self._beta,self._E)

    def _set_E_from_p(self):
        return np.divide(self._p,self._beta)

    def _set_T(self):
        return np.multiply(self._gamma-1,self.mass)

    def _set_boostvalues(self,p,E):
        if p and E:
            print ("You can't define both E & p")
        elif p and not E:
            self._p = p   # Momentum of the particle, GeV/c, because mass comes in GeV/c^2
            self._gamma= self._set_gamma_from_p()
            self._beta = ParticleBoosted.beta_from_gamma(self._gamma)
            self._E = self._set_E_from_p()
            self._T = self._set_T()
        elif E and not p:
            self._E = E   # Energy of the particle, GeV, because mass comes in GeV/c^2
            self._gamma= self._set_gamma_from_E()
            self._beta = ParticleBoosted.beta_from_gamma(self._gamma)
            self._p = self._set_p_from_E()
            self._T = self._set_T()
        elif E==0 and p==0:
            self._E = 0
            self._p = 0
            self._gamma=1
            self._beta=0
            self._T = self._set_T()


    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._set_boostvalues(p=value, E=0)

    @property
    def E(self):
        return self._E

    @E.setter
    def E(self, value):
        self._set_boostvalues(P=0,E=value)

    @property
    def gamma(self):
        return self._gamma

    @property
    def beta(self):
        return self._beta

    @property
    def T(self):
        return self._T

    @ParticleDT.lifetime.getter
    def lifetime(self):
        return np.multiply(self._gamma,self._lifetime)



if __name__ == '__main__':
    #particle = ParticleDT("pi-")
    #print particle.name
    #print particle.charge
    #new_particles = particle.decay
    #for particle in new_particles:
    #    print particle.name
    a = ParticleDT("pi-")
    a.start()
    import time
    time.sleep(10)
