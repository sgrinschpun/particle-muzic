#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, QuantumUniverseVirtualParticle
from phenomena.particles.models.undercoverparticle import UndercoverParticle, VirtualUndercoverParticle

NO_PARENT = -1

class ServerParticle(object):
    '''
    Class used in the server to create particle instances. This class helps changing which class to useself.
    Class attribute PARTICLE determines the model to use.
    Staticmethod "init" allows instantiation from particle name(string) and p, theta, phi (in kwargs)
    Classmethod "fromparticle" helps with the instantiation from UndercoverParticle or VirtualUndercoverParticle
    particle can either be an UndercoverParticle or a VirtualUndercoverParticle"
    VirtualUndercoverParticle should only appear when PARTCILE points to QuantumUniverseVirtualParticle (or any model with the DECAYTHROUGHVIRTUAL set to true)
    '''

    #PARTICLE =  QuantumUniverseVirtualParticle
    PARTICLE =  QuantumUniverseParticle

    @staticmethod
    def init (name, parent = NO_PARENT, **kwargs):
        return ServerParticle.PARTICLE(name, parent, **kwargs)

    @classmethod
    def fromparticle(cls, particle, parent = NO_PARENT):
        if isinstance(particle,UndercoverParticle):
            """From undercover particle"""
            return cls.init(particle.name, parent, p=particle.p, theta=particle.theta, phi=particle.phi)
        elif isinstance(particle,VirtualUndercoverParticle):
            """From virtualundercover particle. We unpack values from the virtualundercover into a dict"""
            dict = {'name':particle.name, 'mass':particle.mass, 'decay':particle._decay_channels}
            return cls.init(dict, parent, p=particle.p, theta=particle.theta, phi=particle.phi)
