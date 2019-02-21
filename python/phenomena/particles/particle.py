import abc

class Particle(object):
    '''
    Abstract Particle class
    Always changing
    '''

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

    # @abc.abstractproperty
    # def decay_time(self):
    #     pass

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

    # @abc.abstractproperty
    # def theta(self):
    #     pass

    @abc.abstractproperty
    def beta(self):
        pass

    @abc.abstractmethod
    def toDictionary(self):
        pass

class BasicParticle(Particle):
    '''
    This class is used by the server to transmit the messages through the socket. It is just a container of information.
    '''

    def __init__(self, parent, id, name, type, mass, charge, composition, transformtime, p, E, vx, vy, vz, beta):
        self._parent = parent
        self._id = id
        self._name = name
        self._type = type
        self._mass = mass
        self._composition = composition
        self._charge = charge
        self._transformtime = transformtime
        self._p = p
        self._E = E
        self._vx = vx
        self._vy = vy
        self._vz = vz
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
    def transformtime(self):
        return self._transformtime

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
    def E(self):
        return self._E

    @property
    def vx(self):
        return self._vx

    @property
    def vy(self):
        return self._vy
    @property
    def vz(self):
        return self._vz
    @property
    def beta(self):
        return self._beta

    def toDictionary(self):
        return toDictionary(self)

def toDictionary(particle):
    '''
    This method is used to extract the infromation required by the visualization and sonification nodes and send it through the socket
    '''
    return {"name": particle.name,
            "parent": particle.parent,
            "id": particle.id,
            "type": particle.type,
            "mass": particle.mass,
            "charge": particle.charge,
            "transformtime": particle.transformtime,
            "composition": particle.composition,
            "p": particle.p,
            "E": particle.E,
            "vx": particle.vx,
            "vy": particle.vy,
            "vz": particle.vz,
            "beta": particle.beta
            }
