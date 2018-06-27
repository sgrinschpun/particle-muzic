from __future__ import division
import abc

from os.path import expanduser, join
HOME = expanduser("~")
import random
import math
import json
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
    JSON_PATH = join(HOME, '.phenomena/conf/part_extra_info.json')
    XTRA_INFO = json.load(open(JSON_PATH))
    CLASS_COUNTER = 0
    C = 29979245800 #cm/(s) 2.99792458e10

    def __new__(cls, *args, **kw):
        try:
            pythia.pdg_id(args[0])
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

    @staticmethod
    def getmass(name):
        #return tbl[part_dict[name]].mass
        return pythia.mass(name)

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
        return self._type.encode('utf-8')

    def _set_type(self):
        self._type= ParticleDT.XTRA_INFO[str(self._pdgid)]['type']

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
        return {"name": self._name,
                "id": self._id,
                "type": self._type,
                "mass": self._mass,
                "charge": self._charge,
                "decay_time": self._time_to_decay,
                "composition": self._composition}

    def printDecayChannels(self):
        print_decay_channels(pythia.pdg_id(self._name))


    @staticmethod
    def get_list_all_particles():
        particles = []
        for pid, pd in pythia.iteritems():
            if '~' not in pd.name: #except intermediate species
                particles.append((pid, pd))
        def cmp(a, b):
            ctau = lambda x: 0 if math.isnan(x[1].ctau) else x[1].ctau
            cta = ctau(a)
            ctb = ctau(b)
            if cta == ctb:
                return 0
            if cta < ctb:
                return -1
            return 1
        #particles.sort(cmp)

        print len(particles)
        print('{:18s} {:>10} {:>10} {:>10} {:>6}'.format("name", "PDG ID", "mass[GeV]",
                                             "ctau[cm]", "charge"))

        for pid, pd in particles:
            print('{name:18} {pid:10} {mass:10.3g} {ctau:10.3e} {charge:6.2g}'
                  .format(name=pd.name, pid=pid, mass=pd.mass,
                          ctau=pd.ctau, charge=pd.charge))

    @staticmethod
    def get_list_stable_particles(tau=1e-8):
        print_stable(tau, title=('Particles with known finite lifetimes longer than ({0})').format(tau))

    @staticmethod
    def get_list_baryons():
        return Sibyll.list_baryons()

    @staticmethod
    def get_list_mesons():
        return Sibyll.list_mesons()


if __name__ == '__main__':
    a = ParticleDT("pi-")
    a.start()
    import time
    time.sleep(10)
