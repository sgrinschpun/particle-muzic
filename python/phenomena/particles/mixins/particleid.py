#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

NO_PARENT = -1

class ParticleId(object):
    '''
    This is a mixin class for the Particle class
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

    def _set_parent(self, argv):
        try:
            parent = argv[1]
        except:
            parent = NO_PARENT
        self._parent = parent

    def toDictionary(self):
        return toDictionary(self)
