import abc

class CMCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def values(self):
        """Returns list of dictonaries of parent particles' momentum, angle and energy"""
        pass


class LabCalc(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def values(self):
        """Returns list of dictonaries of child particle's momentum, angle and energy"""
        pass
