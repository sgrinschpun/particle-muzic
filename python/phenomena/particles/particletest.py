from phenomena.particles.particle import Particle
from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.channels import Decay

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

NO_PARENT = -1

class ParticleTest(Particle):
    STABLE = -1
    CLASS_COUNTER = 0

    #checker for wrong particle names
    #ossibility for instance from pdgid?

    def __init__(self, name, parent = NO_PARENT):
        self._set_id() # Class Counter
        self._setParent(parent) # The parent id of particle

        self._set_name(name)  # Name of the particle
        self._set_pdgid(name) # Id from PDG
        self._set_mass() # Mass of the particle in GeV
        self._set_charge() # Charge of the particle
        self._set_lifetime() # Lifetime of the particle in ****units****
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon)
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]

        self._set_decay_channels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...]
        self._set_decay() # Particle decay channel chosen
        self._set_time_to_decay() #Time until decay in ****units****

    @property
    def id(self):
        return self._id

    def _set_id(self):
        self._id = ParticleTest.CLASS_COUNTER
        ParticleTest.CLASS_COUNTER += 1

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
        return self._time_to_decay

    def _set_time_to_decay(self):
        self._time_to_decay = 1

    @property
    def p(self):
        return 0

    @property
    def theta(self):
        return 0

    @property
    def beta(self):
        return 0
