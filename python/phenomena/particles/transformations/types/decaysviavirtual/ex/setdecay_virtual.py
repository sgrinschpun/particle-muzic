from __future__ import division
import math, random
from scipy.stats import rv_continuous
import numpy as np

from phenomena.particles.decays.Breit_Wigner import lim_nonrel_breit_wigner_gen, lim_rel_breit_wigner_gen
from phenomena.particles.sources import ParticleDataSource
from phenomena.particles.decays.setdecay import Decay

class VirtualDecay(object):

    @staticmethod
    def set(decay,mass,masses,name):

        virtualp = {}
        limits = VirtualDecay.set_mass_limits(mass,masses)
        virtualp = VirtualDecay.set_channel_choice(name, decay, limits)
        if virtualp['name'] != []:
            mass = VirtualDecay.set_mass(masses,virtualp)
            return VirtualDecay.set_virtual_particle_decay(decay,virtualp)
        else:
            return decay

    @staticmethod
    def set_mass_limits(mass,masses):
        return {
                    '12' : [masses[0]+masses[1],mass-masses[2]],
                    '13' : [masses[0]+masses[2],mass-masses[1]],
                    '23' : [masses[1]+masses[2],mass-masses[0]],
                }

    @staticmethod
    def set_weights(fp): #Weights are set with the inverses of the masses

        invmasses = []
        weights = []
        for poss in fp:
            invmasses.append(1./float(poss[1]))

        for invmass in invmasses:
            weights.append(invmass/sum(invmasses))
        return weights

    @staticmethod
    def set_BW_mass(mass,width,limits):
        # Use self._virtualp._name
        # Mass
        #nonrel_breit_wigner = nonrel_breit_wigner_gen(a=limits[0], b=limits[1], shapes='mass, width, limit1, limit2')
        #virtual_mass = nonrel_breit_wigner(mass=float(mass), width=float(width), limit1=limits[0], limit1=limits[1]).rvs()

        lim_rel_breit_wigner = lim_rel_breit_wigner_gen(a=limits[0], b=limits[1], shapes='mass, width, limit1, limit2')
        virtual_mass = lim_rel_breit_wigner(mass=float(mass), width=float(width), limit1=limits[0], limit2=limits[1]).rvs()

        return virtual_mass

    @staticmethod
    def set_channel_choice(name,decay,limits):

        import xml.etree.ElementTree as ET
        import os

        base = 'C:\Users\Sergi\Anaconda2\Lib\site-packages\particletools'

        searchpaths = (base + '/ParticleData.xml', 'ParticleData.xml',
                       '../ParticleData.xml',
                       'ParticleDataTool/ParticleData.xml')
        xmlname = None
        for p in searchpaths:
            if os.path.isfile(p):
                xmlname = p
                break
        if xmlname is None:
            raise IOError('ParticleDataTool::_load_xml(): '
                          'XML file not found.')
        root = ET.parse(xmlname).getroot()


        k = ParticleDataSource.getPDGId(name)
        ids = [k]
        ids.append(ParticleDataSource.getPDGId(decay[0]))
        ids.append(ParticleDataSource.getPDGId(decay[1]))
        ids.append(ParticleDataSource.getPDGId(decay[2]))

        tags = [[str(ids[0]),str(-ids[1])],
            [str(ids[0]),str(-ids[2])],
            [str(ids[0]),str(-ids[3])],
            [str(ids[1]),str(ids[2])],
            [str(ids[1]),str(ids[3])],
            [str(ids[2]),str(ids[3])]]
        tagsR = [[str(-ids[1]),str(ids[0])],
            [str(-ids[2]),str(ids[0])],
            [str(-ids[3]),str(ids[0])],
            [str(ids[2]),str(ids[1])],
            [str(ids[3]),str(ids[1])],
            [str(ids[3]),str(ids[2])]]
        tagsbar = [[str(-ids[0]), str(ids[1])],
            [str(-ids[0]),str(ids[2])],
            [str(-ids[0]),str(ids[3])],
            [str(-ids[1]),str(-ids[2])],
            [str(-ids[1]),str(-ids[3])],
            [str(-ids[2]),str(-ids[3])]]
        tagsbarR = [[str(ids[1]), str(-ids[0])],
            [str(ids[2]),str(-ids[0])],
            [str(ids[3]),str(-ids[0])],
            [str(-ids[2]),str(-ids[1])],
            [str(-ids[3]),str(-ids[1])],
            [str(-ids[3]),str(-ids[2])]]
        combs = {'01':[], '02':[], '03':[], '12':[], '13':[], '23':[]}
        masses = {}
        mwidth = {}
        for parent in root:
            if parent.tag == 'particle':
                for channel in parent:
                    if channel.attrib['products'] == ' '.join(tags[0]) or channel.attrib['products'] == ' '.join(tagsR[0]):
                        combs['01'].append(parent.attrib['name'])
                        masses[parent.attrib['name']]=parent.attrib['m0']
                    if channel.attrib['products'] == ' '.join(tags[1]) or channel.attrib['products'] == ' '.join(tagsR[1]):
                        combs['02'].append(parent.attrib['name'])
                        masses[parent.attrib['name']]=parent.attrib['m0']
                    if channel.attrib['products'] == ' '.join(tags[2]) or channel.attrib['products'] == ' '.join(tagsR[2]):
                        combs['03'].append(parent.attrib['name'])
                        masses[parent.attrib['name']]=parent.attrib['m0']
                    if channel.attrib['products'] == ' '.join(tags[3]) or channel.attrib['products'] == ' '.join(tagsR[3]):
                        combs['12'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[4]) or channel.attrib['products'] == ' '.join(tagsR[4]):
                        combs['13'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[5]) or channel.attrib['products'] == ' '.join(tagsR[5]):
                        combs['23'].append(parent.attrib['name'])

                    if channel.attrib['products'] == ' '.join(tagsbar[0]) or channel.attrib['products'] == ' '.join(tagsbarR[0]):
                        combs['01'].append(parent.attrib['antiName'])
                        masses[parent.attrib['antiName']]=parent.attrib['m0']
                    if channel.attrib['products'] == ' '.join(tagsbar[1]) or channel.attrib['products'] == ' '.join(tagsbarR[1]):
                        combs['02'].append(parent.attrib['antiName'])
                        masses[parent.attrib['antiName']]=parent.attrib['m0']
                    if channel.attrib['products'] == ' '.join(tagsbar[2]) or channel.attrib['products'] == ' '.join(tagsbarR[2]):
                        combs['03'].append(parent.attrib['antiName'])
                        masses[parent.attrib['antiName']]=parent.attrib['m0']
                    if channel.attrib['products'] == ' '.join(tagsbar[3]) or channel.attrib['products'] == ' '.join(tagsbarR[3]):
                        combs['12'].append(parent.attrib['antiName'])
                    if channel.attrib['products'] == ' '.join(tagsbar[4]) or channel.attrib['products'] == ' '.join(tagsbarR[4]):
                        combs['13'].append(parent.attrib['antiName'])
                    if channel.attrib['products'] == ' '.join(tagsbar[5]) or channel.attrib['products'] == ' '.join(tagsbarR[5]):
                        combs['23'].append(parent.attrib['antiName'])

        poss1 = list(set(combs['01']).intersection(combs['23']))
        mposs1 = []
        for poss in poss1:
            mposs1.append(masses[poss])

        GeVfm = 0.19732696312541853
        fp = [] #final possibilities
        ew = []
        min1 = []
        for poss in poss1:
            if masses[poss] == min(mposs1):
                min1.append(poss)
            # We're giving total priority to these three particles and ignoring other options with this choice
            if poss in ['Z0','W+','W-']:
                min1 = [poss, masses[poss]]
                break
            if poss == poss1[-1]:
                min1.append(min(mposs1))

        # We filter out those options for which we won't be able to fetch the data
        for poss in min1[:-1]:
            try:
                ParticleDataSource.getCTau(poss)
            except:
                min1.remove(poss)
        # If we're left without options we need to remove the mass too to avoid passing unwanted checks
        if len(min1)==1:
            min1=[]

        if len(min1)>2:
            n = random.randint(0,len(min1)-2)
            a = min1[n]
            min1 = [a,min(mposs1)]

        if len(min1)>0:
            min1.append(GeVfm/ParticleDataSource.getCTau(min1[0])*1e-15*100.0)
            min1.append(1)
            fp.append(min1)
            if min1[0] in ['W-','W+','Z0']:
                ew.append(min1)

        poss2 = list(set(combs['02']).intersection(combs['13']))
        mposs2 = []
        for poss in poss2:
            mposs2.append(masses[poss])

        min2 = []
        for poss in poss2:
            if masses[poss] == min(mposs2):
                min2.append(poss)
            if poss in ['Z0','W+','W-']:
                min2 = [poss, masses[poss]]
                break
            if poss == poss1[-1]:
                min1.append(min(mposs1))

        # We filter out those options for which we won't be able to fetch the data
        for poss in min2[:-1]:
            try:
                ParticleDataSource.getCTau(poss)
            except:
                min2.remove(poss)
        # If we're left without options we need to remove the mass too to avoid passing unwanted checks
        if len(min2)==1:
            min2=[]

        if len(min2)>2:
            n = random.randint(0,len(min2)-2)
            a = min2[n]
            min2 = [a,min(mposs2)]

        if len(min2)>0:
            min2.append(GeVfm/ParticleDataSource.getCTau(min2[0])*1e-15*100.0)
            min2.append(2)
            fp.append(min2)
            if min2[0] in ['W-','W+','Z0']:
                ew.append(min2)

        poss3 = list(set(combs['03']).intersection(combs['12']))
        mposs3 = []
        for poss in poss3:
            mposs3.append(masses[poss])

        min3 = []
        for poss in poss3:
            if masses[poss] == min(mposs3):
                min3.append(poss)
            if poss in ['Z0','W+','W-']:
                min3 = [poss, masses[poss]]
                break
            if poss == poss1[-1]:
                min1.append(min(mposs1))

        # We filter out those options for which we won't be able to fetch the data
        for poss in min3[:-1]:
            try:
                ParticleDataSource.getCTau(poss)
            except:
                min3.remove(poss)
        # If we're left without options we need to remove the mass too to avoid passing unwanted checks
        if len(min3)==1:
            min3=[]

        if len(min3)>2:
            n = random.randint(0,len(min3)-2)
            a = min3[n]
            min3 = [a,min(mposs3)]

        if len(min3)>0:
            min3.append(GeVfm/ParticleDataSource.getCTau(min3[0])*1e-15*100.0)
            min3.append(3)
            fp.append(min3)
            if min3[0] in ['W-','W+','Z0']:
                ew.append(min3)

        # If we found a choice compatible with electroweak theory, that's our first option
        if len(ew)>0:
            n = random.randint(0,len(ew)-1)
            fd = ew[n]
        # Otherwise, we might have found another option that is well known (CTau defined, etc.)
        else:
            weights = VirtualDecay.set_weights(fp)
            fd = Decay.weightedChoice(fp, weights)
        # Lastly, we might not have found a viable virtual decay option so we return the original decay,
        # but this option is considered at the end to fit the format of the return

        # We put a way out of the function if nothing was found to avoid errors fetching the 'NoneType' fd
        if type(fd)!=list:
            virtualp = {'name': []}
            return virtualp

        chnum = []
        for ind in range(len(decay)):
            if ind != fd[3]-1:
                chnum.append(str(ind+1))
        channel = ''.join(chnum)
        # For this specific 3 particle case, it might be simpler to use:
        # if self._is_virtual[0] == 0:
        #     channel = '23'
        # elif self._is_virtual[1] == 0:
        #     channel = '13'
        # else:
        #     channel = '12'

        virtual_particle = fd[0]
        virtual_particle_mass = fd[1]
        virtual_particle_width = fd[2]
        virtual_channel_freepart = fd[3]

        # We must set the virtual particle name (could be empty) and then flag which masses will come from the virtual particle
        virtual_mass = VirtualDecay.set_BW_mass(virtual_particle_mass, virtual_particle_width, limits[channel])

        # We set the threshold for no virtual decay if the virtual mass is on the lower end of our distribution
        # This way, it's more probable to see a virtual particle when we're close
        virtualp = {}
        if (virtual_particle in ['W-','W+','Z0']) or virtual_mass >= (limits[channel][0]+limits[channel][1])/2.:
            virtualp['name'] = virtual_particle
            virtualp['mass'] = virtual_mass
            virtualp['realmass'] = virtual_particle_mass
            virtualp['channel'] = virtual_channel_freepart
        else:
            virtualp['name'] = []

        return virtualp

    @staticmethod
    def set_mass(masses,virtualp):

        # We don't need the masses of the daughter particles, because they are looked up in DecayCalc
        # vrt_masses = []
        new_masses = []
        new_masses.append(masses[virtualp['channel']-1])
        new_masses.append(virtualp['mass'])
        # self._virtualp._masses = vrt_masses
        return new_masses

    @staticmethod
    def set_virtual_particle_decay(decay,virtualp):
        vrt_decay = []
        new_decay = []
        for index in range(len(decay)):
            if index != virtualp['channel']-1:
                vrt_decay.append(decay[index])
            else:
                new_decay.append(decay[index])
        new_decay.append(virtualp['name'])

        # We set the particles to which the virtual particle must decay inside the dictionary virtualp with other data
        virtualp['decay'] = vrt_decay

        #In the place of the virtual particle we have a dictionary with all needed data
        decay = new_decay[:-1]+[virtualp]

        return decay
