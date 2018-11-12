from __future__ import division, print_function
import math, random

from phenomena.particles.collision.kinematics.channel.inverse_decay_list import InverseDecayList
from phenomena.particles.collision.kinematics.channel.cross_section import CrossSection
from phenomena.particles.sources import ParticleDataSource

# Chooses the channel of "decay" after a two particle collision. If no impact parameter is given, sets the possible decays but doesn't choose
# We can set a biased probability of decay if we want to observe rare decays more often in line 29-30
class CollisionChannel(object):

    def __init__(self,p1,p2,energy,*argv):

        self._choose_virtual(p1,p2)
        self._set_virtual_data(self._virtual_list,p1,p2)

        self._set_cross_sections(self._virtual_masses,self._virtual_width,self._virtual_b_rat,energy)

        for particle in range(len(self._cross_section)):
            print(self._virtual_list[particle],'\t',self._cross_section[particle])

        # to use _set_decays method we must use decay tags even though we're not dealing with decays:
        try: # If an impact is given we choose an option for the collision
            impact = argv[0]
            self._set_available_channels(self._virtual_list,self._cross_section,impact)
            self._set_probabilities(self._cross_section) # For unbiased probabilities
            # self._set_biased_probabilities(self._cross_section)  #For biased probabilities (we will see unlikely decays more often)
            self._set_channel(self._virtual_list,self._probabilities)
            print('\nChosen channel is:\t',self._channel)
        except: # Otherwise Channel is empty and we will decide the channel later on
            self._set_channel([],1)


    def _choose_virtual(self,p1,p2): # Fetches possible virtual particles
        self._virtual_list = InverseDecayList(p1,p2)._virtual_list

    def _set_virtual_data(self,virtual_list,p1,p2):
        GeVfm = 0.19732696312541853

        self._virtual_masses = []
        self._virtual_width = []
        self._virtual_b_rat = []
        for particle in virtual_list:
            self._virtual_masses.append(ParticleDataSource.getMass(particle))
            self._virtual_width.append(GeVfm/ParticleDataSource.getCTau(particle)*1e-15*100.0)
            decay = ParticleDataSource.getDecayChannels(particle)
            if decay == []:
                self._virtual_b_rat.append(0)
            for option in decay:
                if ParticleDataSource.getPDGId(p1) in option[1] and ParticleDataSource.getPDGId(p2) in option[1] and len(option[1])==2 :
                    self._virtual_b_rat.append(option[0])

    def _set_cross_sections(self,mass,twidth,b_rat,energy):

        self._cross_section = []
        for index in range(len(mass)):
            cross_section = CrossSection(mass[index],twidth[index],b_rat[index],energy)._cross_section
            self._cross_section.append(cross_section)

    def _set_available_channels(self,virtual_list,cross_section,impact):

        available_cross = []
        available_list = []
        for index, area in enumerate(cross_section):
            if area >= impact and area!= 0:
                available_cross.append(area)
                available_list.append(virtual_list[index])

        self._virtual_list = available_list
        self._cross_section = available_cross

    def _set_probabilities(self,cross_sections): # We will balance the probabilities equally in this version

        total = sum(cross_sections)
        self._probabilities = [x/total for x in cross_sections]

    def _set_biased_probabilities(self,cross_sections): # We make the lesser probabilties comparable to the higher ones in this version

        mag = [math.log(x,10) for x in cross_sections]
        limits = [min(mag),max(mag)]
        new_mag = [(limits[1]-1)+(x-limits[0])/(limits[1]-limits[0]) for x in mag] # Redistribution in 1 order of magnitude
        # new_mag = [(limits[1]-2)+2*(x-limits[0])/(limits[1]-limits[0]) for x in mag] # Redistribution in 2 order of magnitude
        new_cross_sections = [10**x for x in new_mag]
        total = sum(new_cross_sections)
        self._probabilities = [x/total for x in new_cross_sections]

    def _set_channel(self,channel_list,probabilities):
        list_decay = []
        if channel_list != []:
            choice_param = self._build_weights(probabilities)
            choice = self._weighted_choice(choice_param[0],choice_param[1])
            channel = channel_list[choice]
            self._channel = channel
        else:
            self._channel = []

    def _build_weights(self,probabilities):
        seq = []
        weights=[]
        for index, item in enumerate(probabilities):
            if item != 0.0:      # do not use channels with prob = 0.0
                seq.append(index)
                weights.append(item)
        return seq, weights

    def _weighted_choice(self, seq, weights):
        assert len(weights) == len(seq)
        #assert abs(1. - sum(weights)) < 1e-6
        x = random.random()
        for i, elmt in enumerate(seq):
            if x <= weights[i]:
                return elmt
            x -= weights[i]

    @property
    def channel(self):
        return self._channel
