from __future__ import division
import math, random

from particle import Particle, ParticleDT, toDictionary

from phenomena.particles.kinematics.decay.calculations import DecayCalc
from phenomena.particles.kinematics.parameters import boostParams
from phenomena.particles.virtual_particle import VirtualChannel

#Santi was here

NO_PARENT = -1
class ParticleBoosted(ParticleDT):
    c= 299792458 #m/s

    # With virtual particles added, name is no longer always the name.
    # If it doesn't raise trouble anywhere else, it should be changed into something else (pdata, particle, etc)
    def __init__(self, *argv, **kwargs): #initialize either with momentum (p) or energy (E)

        try:
            self._parent = argv[1]
        except:
            self._parent = -1

        if isinstance(argv[0], collections.Mapping):
            self._virtual_init(*argv, **kwargs)
        elif isinstance(argv[0], six.string_types):
            self._real_init(*argv, **kwargs)
        else:
            return None

        def _virtual_init(self, argv, **kwargs):
            self._name = argv[0].get['name']

        if type(name) is str:
            # Scenario for handling regular particles
            super(ParticleBoosted, self).__init__(name,parent)#inherit properties from ParticleDT
            self._theta = kwargs.get('theta',0) #the angle of this instance

            masses = []  # array of masses 0: parent particle, 1: first decay particle, ...
            for particle in self.decay:
                masses.append(ParticleDT.getmass(particle))

            self._masses = masses

            #decide if we want the decay to happen through a virtual channel
            if len(self.decay) == 3:
                VirtualChannel(self.decay,self.mass, self._masses, self.name)
            #the decay particles and masses have been reset inside ParticleVirtual if necessary

            #calculate and assign boosted parameters
            self._setBoostedParameters(kwargs)

            # increase lifetime by gamma factor
            self._lifetime *= self._gamma
        else:
            # Scenario for handling virtual particles
            pname = name[0]
            mass = name[1]
            decay = [name[2],name[3]]
            self._set_name(pname)  # Name of the particle pypdt convention
            self._set_id() # Class Counter
            self._set_pdgid(pname) # Id from PDG, taken from pypdt
            self._mass = mass # Mass of the particle in GeV
            self._set_charge() # Charge of the particle taken from pypdt
            self._set_lifetime() # Lifetime of the particle, taken from pypdt
            # Virtual particles have lifetimes that are too short, so we make them large. This can be changed to a more realistic approach
            self._lifetime *= 1.e10 #!!CHECK!!#
            self._set_type() # Particle Type will always be virtual
            self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json.
            self._set_lifetime_ren() #Renormalization of the lifetime THIS SHOULD BE DONE AT THE NODES and brought back with callback
            self.decay = decay # Particle decay channel chosen
            self._set_time_to_decay()  # Particle time lived before decay, renormalized
            self._setParent(parent)

            self._p = kwargs.get('p',None)
            self._gamma = boostParams.gamma_from_p(self.mass,self._p)
            self._beta =  boostParams.beta_from_gamma(self._gamma)
            self._E = boostParams.E_from_p(self._beta,self._p)
            self._T = boostParams.T_from_gamma(self.mass,self._gamma)

            self._theta = kwargs.get('theta',0)
            self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self.decay).values # sets values for decay particles

            # increase lifetime by gamma factor
            self._lifetime *= self._gamma

    def _setBoostedParameters(self,kwargs):
        self._params = boostParams(self._name,p=kwargs.get('p',None),E=kwargs.get('E',None)) # sets boosted parameters for this instance
        self._p = self._params.p
        self._E = self._params.E
        self._gamma = self._params.gamma
        self._beta = self._params.beta
        self._T = self._params.T

        self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self.decay).values # sets values for decay particles


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

    def toDictionary(self):
        return toDictionary(self)
