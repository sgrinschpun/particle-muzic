import abc

class CMCalc(object):
    __metaclass__ = abc.ABCMeta

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
