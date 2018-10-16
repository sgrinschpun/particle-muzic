#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle

NO_PARENT = -1

class ServerParticle(object):
    '''
    Class used in the server to create particle instances
    This class helps changing which class to use
    '''
    PARTICLE = BubbleChamberParticle

    @staticmethod
    def init (name, parent = NO_PARENT, **kwargs):
        return ServerParticle.PARTICLE(name, parent, **kwargs)
