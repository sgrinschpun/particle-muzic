#!/usr/bin/env python

__author__ = "Sergi Masot"
__license__ = "--"
__version__ = "0.1"
__email__ = "sergimasot13@gmail.com"
__status__ = "Development"

import collections
import six
from phenomena.particles.particle import Particle
from phenomena.particles.mixins import ParticleId, ParticleVirtual, ParticleData, ParticleDecay, ParticleBoost, ParticleChannel

NO_PARENT = -1

class QuantumUniverseVirtualParticle(ParticleChannel, ParticleDecay, ParticleBoost, ParticleVirtual, ParticleData, ParticleId, Particle):
    '''
    This class is intended for the QuantumUniverse simulation allowing virtual particles.
    '''

    # To preserve the structure in the server, we incorporate every additional argument that a virtual particle needs in
    # *argv instead of it's name and parent
    def __init__(self, *argv, **kwargs):

        ### Check for the kind of particle that is being created. If it's virtual, his mass (and possibly his decay) is already assigned
        try:
            parent = argv[1]
        except:
            parent = NO_PARENT

        ### Run all methods from mixins that depend on virtuality
        if isinstance(argv[0], collections.Mapping):

            # Reformat arguments in argv
            name = argv[0].get('name')
            mass = argv[0].get('mass')
            self._set_name(name)  # Name of the particle

            #### ParticleVirtual
            self._set_virtual_mass(name,mass) # Mass of the particle in GeV
            self._set_virtual_lifetime() # Lifetime of the particle in ****units****
            self._set_virtuality()

        elif isinstance(argv[0], six.string_types):

            name = argv[0]
            self._set_name(name)  # Name of the particle

            #### ParticleData
            self._set_mass() # Mass of the particle in GeV
            self._set_lifetime() # Lifetime of the particle in ****units****

        else:
            return None

        #### ParticleId
        self._set_id() # Class Counter
        self._set_parent(parent) # The parent id of particle

        #### ParticleData
        # We set the name at the beginning as it is needed for some particlaData methods
        self._set_pdgid(name) # Id from PDG
        # We don't set the mass with _set_mass method as it's not the amount in PDG
        self._set_charge() # Charge of the particle
        # We don't set the lifetime with _set_lifetime method in particle data as it is too short for virtual particles
        # We don't set the type using particledata method
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...]
        self._set_decayChannels() #All the decay channels and BRs of the particle in format [(BR,[part1,..,partn]),...]
        self._set_type() # Particle Type (quark, lepton, boson, meson, baryon) #

        #### ParticleBoost
        self._set_fourMomentum(kwargs)#assign 4momentum vector and  boosted parameters
        self._set_boostedLifetime()# lifetime is recalculated

        if argv[0].get('decay') is None: # If particle decay channel is not already chosen

            #### ParticleVirtual
            self._deactivate_decay_channels() # for virtual particles, not all channels are allowed
            self._renorm_decay_channels() # remaining channels must have the probability renormalized
            ### ParticleDecay
            self._set_decay()

            # decide if we want the decay to happen through a virtual channel
            # this choice is independent of the fact that this model can calculate the decay of a given virtual particle
            if len(self._decay) == 3:
                ### ParticleChannel
                self._set_virtual_decay()
            # in decays of 2 particles there is no point in considering the possibility
            # in decays of 4 and more particles we first need to generalize the combination searching algorithm
        else :  # Otherwise, we decide on a decay
            self._decay = argv[0].get('decay')

        ### ParticleDecay
        self._set_decayTime() #Time until decay in ****units****
        self._set_decayBoostedParameters() #Calculates the boosted parameters of the decayed particles
