import abc

class Particle(object):
    STABLE = -1
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
    # @abc.abstractproperty
    # def p(self):
    #     pass
    #
    # @abc.abstractproperty
    # def theta(self):
    #     pass
    #
    # @abc.abstractproperty
    # def beta(self):
    #     pass

    @abc.abstractmethod
    def toDictionary(self):
        pass

class ParticleId(object):
    '''
    This is a mixin class for the ParticleBoosted class
    It adds functionality ised by the particle server:
     - It adds the attributes and methods related to id & parent
     - It adds the CLASS_COUNTER class attribute
     - It adds the toDictionary method
    '''
    CLASS_COUNTER = 0

    @property
    def id(self):
        return self._id

    def _set_id(self):
        self._id = ParticleId.CLASS_COUNTER
        ParticleId.CLASS_COUNTER += 1

    @property
    def parent(self):
        return self._parent

    def _setParent(self, parent):
        self._parent = parent

    def toDictionary(self):
        return toDictionary(self)



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
            "theta": particle.phi,
            "beta": particle.beta}
