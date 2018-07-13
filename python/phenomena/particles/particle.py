from __future__ import division
import abc

from os.path import expanduser, join
HOME = expanduser("~")
import random
import math
import json
import collections
from operator import itemgetter
import time, threading

#ParticleDataTool gives us the parameters and decay channels
from particletools.tables import PYTHIAParticleData, SibyllParticleTable, print_decay_channels, print_stable
pythia = PYTHIAParticleData()
Sibyll = SibyllParticleTable()

class Particle(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def parent(self):
        pass

    #pdg attributes
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

    #boost attributes (minimum, i.e, interesting for visualization)
    @abc.abstractproperty
    def p(self):
        pass

    @abc.abstractproperty
    def theta(self):
        pass

    @abc.abstractproperty
    def beta(self):
        pass

    @abc.abstractmethod
    def toDictionary(self):
        pass

class BasicParticle(Particle):

    def __init__(self, parent, id, name, type, mass, charge, composition, decay_time, p, theta, beta):
        self._parent = parent
        self._id = id
        self._name = name
        self._type = type
        self._mass = mass
        self._composition = composition
        self._charge = charge
        self._decay_time = decay_time
        self._p = p
        self._theta = theta
        self._beta = beta

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

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

    @property
    def p(self):
        return self._p

    @property
    def theta(self):
        return self._theta

    @property
    def beta(self):
        return self._beta

    def toDictionary(self):
        return toDictionary(self)

NO_PARENT = -1

class ParticleDT(Particle):
    STABLE = -1
    JSON_PATH = join(HOME, '.phenomena/conf/part_extra_info.json')
    XTRA_INFO = json.load(open(JSON_PATH))
    CLASS_COUNTER = 0
    C = 29979245800 #cm/(s) 2.99792458e10

    def __new__(cls, *args, **kw):
        try:
#        pythia.pdg_id(args[0])
            return super(ParticleDT, cls).__new__(cls)
        except Exception, ex:
            raise Exception("Exception: {0}".format(ex.message))

    def __init__(self, name, parent = NO_PARENT):
        self._set_name(name)  # Name of the particle pypdt convention
        self._set_id() # Class Counter
        self._set_pdgid(name) # Id from PDG, taken from pypdt
        self._set_mass() # Mass of the particle in GeV, taken from pypdt
        self._set_charge() # Charge of the particle, taken from pypdt
        self._set_lifetime() # Lifetime of the particle, taken from pypdt
        self._set_decay_channels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...] from ParticleDataTool
        self._set_type() # Particle Type (quark, lepton, bosoon, meson, baryon) taken from json
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json.
        self._set_lifetime_ren() #Renormalization of the lifetime THIS SHOULD BE DONE AT THE NODES and brought back with callback
        self._set_decay() # Particle decay channel chosen
        self._set_time_to_decay()  # Particle time lived before decay, renormalized
        self._setParent(parent)

    @property
    def parent(self):
        return self._parent

    def _setParent(self, parent):
        self._parent = parent

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
        return (delta2 * (n - range1[0]) / delta1) + range2[0]

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
        self._pdgid = pythia.pdg_id(name)
        #if name in list(aquarks.keys()):
        #    self._pdgid = aquarks[name]
        #else:
        #    self._pdgid = part_dict[name]

    @property
    def mass(self):
        return self._mass

    def _set_mass(self):
        self._mass = pythia.mass(self._name)
        #self._mass= tbl[self._pdgid].mass

    @property
    def charge(self):
        return self._charge

    def _set_charge(self):
        self._charge = pythia.charge(self._name)
        #self._charge= tbl[self._pdgid].charge

    @property
    def lifetime(self):
        return self._lifetime

    def _set_lifetime(self):
        if math.isnan(pythia.ctau(self._name)) or math.isinf(pythia.ctau(self._name)):
            self._lifetime = ParticleDT.STABLE
        else:
            self._lifetime = pythia.ctau(self._name)/ParticleDT.C
        #self._lifetime= tbl[self._pdgid].lifetime

    @property
    def lifetime_ren(self):
        return self._lifetime_ren

    def _set_lifetime_ren(self):
        if self._lifetime != ParticleDT.STABLE :
            self._lifetime_ren= ParticleDT.renormalize_time(ParticleDT.magnitude(self._lifetime))

    @property
    def decay_channels(self):
        return self._decay_channels

    def _set_decay_channels(self):
        try:
            self._decay_channels = pythia.decay_channels(self._name)
        except:
            self._decay_channels = []

    @property
    def type(self):
        return self._type

    def _set_type(self):
        self._type= ParticleDT.XTRA_INFO[str(self._pdgid)]['type'].encode('utf-8')

    @property
    def composition(self):
        return self._composition

    def _set_composition(self):
        self._composition =[]
        if ParticleDT.XTRA_INFO[str(self._pdgid)]['composition'] != []:
            for quark in ParticleDT.XTRA_INFO[str(self._pdgid)]['composition'][0]: #only consider first superposition of quarks
                self._composition.append(quark.encode('utf-8'))
        else:
            pass

    def _set_decay(self):
        list_decay = []
        if self._decay_channels != []:
            try:
                choice = self._weighted_choice(self._build_weights()[0],self._build_weights()[1])
                channel = self._decay_channels[choice][1]
                for part in channel:
                    list_decay.append(pythia.name(part))  # this just shows parti
            finally:
                self.decay = list_decay
        else:
            self.decay = []

    @property
    def decay_time(self):
        return self._time_to_decay

    def _set_time_to_decay(self): #this is just a proof of concept. need to be improved
        if self._lifetime != ParticleDT.STABLE :
            self._time_to_decay = self._next_decay()
        else:
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
                        part_names.append(pythia.name(part))
                    dc_names.append(tuple([item[0], part_names]))
            return sorted(dc_names,key=itemgetter(0), reverse=True)
        else:
            return dc_names

    def toDictionary(self):
        return toDictionary(self)

    @property
    def p(self):
        return 0

    @property
    def theta(self):
        return 0

    @property
    def beta(self):
        return 0

    def printDecayChannels(self):
        print_decay_channels(pythia.pdg_id(self._name))

    @staticmethod
    def getmass(name):
        #return tbl[part_dict[name]].mass
        return pythia.mass(name)

    @staticmethod
    def get_list_all_particles():
        particles = []
        part_dict = {}
        for pid, pd in pythia.iteritems():
            if '~' not in pd.name: #except intermediate species
                particles.append((pid, pd))
                part_dict[pd.name] = {
                    'pdg_id':pid,
                    'mass':pd.mass,
                    'ctau':pd.ctau,
                    'charge':pd.charge
                }
        part_dict_ord = collections.OrderedDict(sorted(part_dict.items()))
        #print sorted(part_dict)
        print json.dumps(part_dict_ord, indent=1)
        #print len(particles)
        #print('{:18s} {:>10} {:>10} {:>10} {:>6}'.format("name", "PDG ID", "mass[GeV]",
        #                                     "ctau[cm]", "charge"))

        #for pid, pd in particles:
        #    print('{name:18} {pid:10} {mass:10.3g} {ctau:10.3e} {charge:6.2g}'
        #           .format(name=pd.name, pid=pid, mass=pd.mass,
        #                  ctau=pd.ctau, charge=pd.charge))



    @staticmethod
    def get_list_stable_particles(tau=1e-8):
        print_stable(tau, title=('Particles with known finite lifetimes longer than ({0})').format(tau))

    @staticmethod
    def get_list_baryons():
        return Sibyll.list_baryons()

    @staticmethod
    def get_list_mesons():
        return Sibyll.list_mesons()


def toDictionary(particle):
    return {"name": particle.name,
            "parent": particle.parent,
            "id": particle.id,
            "type": particle.type,
            "mass": particle.mass,
            "charge": particle.charge,
            "decay_time": particle.decay_time,
            "composition": particle.composition,
            "p": particle.p,
            "theta": particle.theta,
            "beta": particle.beta}


if __name__ == '__main__':
    a = ParticleDT("pi-")
    a.start()
    import time
    time.sleep(10)
