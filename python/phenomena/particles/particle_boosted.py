import time, threading

from phenomena.particles.particle import Particle, toDictionary
from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.channels import Decay, TimeRemap
from phenomena.particles.kinematics.decay.calculations import DecayCalc
from phenomena.particles.kinematics.parameters import BoostParams

NO_PARENT = -1

class ParticleBoosted(Particle):
    CLASS_COUNTER = 0

    #checker for wrong particle names
    #possibility for instance from pdgid?

    def __init__(self, name, parent = NO_PARENT, **kwargs):
        self._set_id() # Class Counter
        self._setParent(parent) # The parent id of particle

        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        self._set_lifetime() # Lifetime of the particle in ****units****
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]

        self._theta = kwargs.get('theta',0)#the angle of this instance
        self._setThisBoostedParameters(kwargs)#calculate and assign boosted parameters
        self._setBoostedLifetime()# lifetime is recalculated

        self._set_decay_channels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...]
        self._set_decay() # Particle decay channel chosen
        self._set_decay_time() #Time until decay in ****units****
        self._setDecaysBoostedParameters() #Calculates the boosted parameters of the decayed particles


    @property
    def id(self):
        return self._id

    def _set_id(self):
        self._id = ParticleBoosted.CLASS_COUNTER
        ParticleBoosted.CLASS_COUNTER += 1

    @property
    def parent(self):
        return self._parent

    def _setParent(self, parent):
        self._parent = parent

    def toDictionary(self):
        return toDictionary(self)

    @property
    def name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    @property
    def pdgid(self):
        return self._pdgid

    def _set_pdgid(self, name):
        self._pdgid = ParticleDataSource.getPDGId(name)

    @property
    def mass(self):
        return self._mass

    def _set_mass(self):
        self._mass = ParticleDataSource.getMass(self._name)

    @staticmethod
    def getmass(name):
        return ParticleDataSource.getMass(name)

    @property
    def charge(self):
        return self._charge

    def _set_charge(self):
        self._charge = ParticleDataSource.getCharge(self._name)

    @property
    def lifetime(self):
        return self._lifetime

    def _set_lifetime(self):
        self._lifetime = ParticleDataSource.getTau(self._name)

    @property
    def type(self):
        return self._type

    def _set_type(self):
        self._type= ParticleDataSource.getType(self._name)

    @property
    def composition(self):
        return self._composition

    def _set_composition(self):
        self._composition = ParticleDataSource.getComposition(self._name)

    @property
    def decay_channels(self):
        return self._decay_channels

    def _set_decay_channels(self):
        self._decay_channels = ParticleDataSource.getDecayChannels(self._name)

    @property
    def decay(self):
        return self._decay

    def _set_decay(self):
        self._decay = Decay.set(self._decay_channels)

    @property
    def decay_time(self):
        return self._decay_time

    def _set_decay_time(self):
        if self._lifetime != Particle.STABLE :
            print "********", self._lifetime
            self._decay_time = TimeRemap.getNextDecayTime(self._lifetime)
        else:
            self._decay_time = Particle.STABLE

    def start(self, callback):
        if self._decay_time != Particle.STABLE:
            wait_time = TimeRemap.renormalize(self._decay_time)
            print "Wait for: ", wait_time
            threading.Timer(wait_time, callback).start()
        else:
            print "Wait for: ", 10
            threading.Timer(10, callback).start()

    @property
    def p(self):
        return self._p

    @property
    def E(self):
        return self._E

    @property
    def gamma(self):
        return self._gamma

    @property
    def beta(self):
        return self._beta

    @property
    def theta(self):
        return self._theta

    @property
    def T(self):
        return self._T

    def _setThisBoostedParameters(self,kwargs):
        self._params = BoostParams(self._mass,p=kwargs.get('p',None),E=kwargs.get('E',None)) # sets boosted parameters for this instance
        self._p = self._params.p
        self._E = self._params.E
        self._gamma = self._params.gamma
        self._beta = self._params.beta
        self._T = self._params.T

    def _setBoostedLifetime(self):# lifetime is recalculated if not stable
        if self._lifetime != Particle.STABLE :
            self._lifetime *= self._gamma

    @property
    def decayvalues(self):
        return self._decayvalues

    def _setDecaysBoostedParameters(self):
        self._decayvalues = DecayCalc.getValues(self._mass,self._gamma,self._theta,self._decay) # sets values for decay particles
