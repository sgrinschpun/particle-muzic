import abc

class C12MCalc(object):
# For 3body decay this RF for the CM of particles 1 and 2 is useful
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def dalitz(masses):
        """Returns the randomized dalitz plot variable m12"""

    @abc.abstractmethod
    def E(masses,dalitz):
        """Returns list of child particles energies"""

    @abc.abstractmethod
    def P(masses,dalitz):
        """Returns list of child particles momentum"""

    @abc.abstractmethod
    def pxy(masses,dalitz,angles):
        """Returns list of dictonaries of child particles momentum components"""
        pass


class CMCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def p3(masses):
        """Returns one particle's momemntum for 3body decay"""

    @abc.abstractmethod
    def E(masses):
        """Returns list of child particles energies"""

    @abc.abstractmethod
    def P(masses):
        """Returns list of child particles momentum"""

    @abc.abstractmethod
    def pxy(masses,angles):
        """Returns list of dictonaries of child particles momentum components"""
        pass


class LabCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def values(self):
        """Returns list of dictonaries of child particles momentum, angle and energy"""
        pass
