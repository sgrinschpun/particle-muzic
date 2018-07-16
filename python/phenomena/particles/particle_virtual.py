from __future__ import division, print_function
import math, random
from scipy.stats import rv_continuous
import numpy as np

from phenomena.particles.kinematics.decay.Breit_Wigner import lim_nonrel_breit_wigner_gen
from phenomena.particles.kinematics.decay.Breit_Wigner import lim_rel_breit_wigner_gen
from phenomena.particles.particle import ParticleDT

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

class VirtualChannel(object):

    def __init__(self,decay,mass,masses,name):
        self._name = name
        self._decay = decay
        self._virtualp = {}
        limits = self._set_mass_limits(mass,masses)
        self._set_channel_choice(decay, limits)
        if self._virtualp['name'] != []:
            self._set_mass(masses,self._virtualp['mass'])
            self._set_virtual_decay(decay)
            self._decay[-1] = self._virtualp
            #In the place of the virtual particle we have a tuple with name in [0], mass in [1] and decay in [2],[3]

    def _set_mass_limits(self,mass,masses):
        return {
                    '12' : [masses[0]+masses[1],mass-masses[2]],
                    '13' : [masses[0]+masses[2],mass-masses[1]],
                    '23' : [masses[1]+masses[2],mass-masses[0]],
                }

    def _set_weights(self,fp): #Weights are set with the inverses of the masses

        invmasses = []
        weights = []
        for poss in fp:
            invmasses.append(1./float(poss[1]))

        for invmass in invmasses:
            weights.append(invmass/sum(invmasses))
        return weights

    def _set_BW_mass(self,mass,width,limits):
        # Use self._virtualp._name
        # Mass
        #nonrel_breit_wigner = nonrel_breit_wigner_gen(a=limits[0], b=limits[1], shapes='mass, width, limit1, limit2')
        #virtual_mass = nonrel_breit_wigner(mass=float(mass), width=float(width), limit1=limits[0], limit1=limits[1]).rvs()

        lim_rel_breit_wigner = lim_rel_breit_wigner_gen(a=limits[0], b=limits[1], shapes='mass, width, limit1, limit2')
        virtual_mass = lim_rel_breit_wigner(mass=float(mass), width=float(width), limit1=limits[0], limit1=limits[1]).rvs()

        return virtual_mass

    def _set_channel_choice(self,decay,limits):

        import xml.etree.ElementTree as ET
        import os

        base = os.path.dirname(os.path.abspath(__file__))
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


        k = pythia.pdg_id(self._name)
        ids = [k]
        ids.append(pythia.pdg_id(self._decay[0]))
        ids.append(pythia.pdg_id(self._decay[1]))
        ids.append(pythia.pdg_id(self._decay[2]))

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
            if poss in ['Z0','W+','W-']:
                min1 = [poss, masses[poss]]
                break
            if poss == poss1[-1]:
                min1.append(min(mposs1))

        if len(min1)>2:
            n = random.randint(0,len(min1)-2)
            a = min1[n]
            min1 = [a,min(mposs1)]

        if len(min1)>0:
            min1.append(GeVfm/pythia.ctau(min1[0])*1e-15*100.0)
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

        if len(min2)>2:
            n = random.randint(0,len(min2)-2)
            a = min2[n]
            min2 = [a,min(mposs2)]

        if len(min2)>0:
            min2.append(GeVfm/pythia.ctau(min2[0])*1e-15*100.0)
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

        if len(min3)>2:
            n = random.randint(0,len(min3)-2)
            a = min3[n]
            min3 = [a,min(mposs3)]

        if len(min3)>0:
            min3.append(GeVfm/pythia.ctau(min3[0])*1e-15*100.0)
            min3.append(3)
            fp.append(min3)
            if min3[0] in ['W-','W+','Z0']:
                ew.append(min3)

        if len(ew)>0:
            n = random.randint(0,len(ew)-1)
            fd = ew[n]
        else:
            weights = self._set_weights(fp)
            fd = _weighted_choice(fp, weights)

        chnum = []
        for ind in range(len(self._decay)):
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
        virtual_mass = self._set_BW_mass(virtual_particle_mass, virtual_particle_width, limits[channel])

        # We set the threshold for no virtual decay if the virtual mass is on the lower end of our distribution
        # This way, it's more probable to see a virtual particle when we're close
        if (virtual_particle in ['W-','W+','Z0']) or self.virtual_mass >= (limits[channel][0]+limits[channel][1])/2.:
            self._virtualp['name'] = virtual_particle
            self._virtualp['mass'] = virtual_mass
            self._virtualp['realmass'] = virtual_particle_mass
            self._virtualp['channel'] = virtual_channel_freepart
        else:
            self._virtualp['name'] = []

    def _weighted_choice(self, seq, weights):
        assert len(weights) == len(seq)
        #assert abs(1. - sum(weights)) < 1e-6
        x = random.random()
        for i, elmt in enumerate(seq):
            if x <= weights[i]:
                return elmt
            x -= weights[i]


    def _set_mass(self,masses,virtual_mass):

        # We don't need the masses of the daughter particles, because they are looked up in DecayCalc
        # vrt_masses = []
        new_masses = []
        new_masses.append(masses[self._virtualp['channel']-1])
        new_masses.append(virtual_mass)
        # self._virtualp._masses = vrt_masses
        self._masses = new_masses


    def _set_virtual_decay(self,decay):
        vrt_decay = []
        new_decay = []
        for index in range(len(decay)):
            if index != self._virtualp['channel']-1:
                vrt_decay.append(decay[index])
            else:
                new_decay.append(decay[index])
        new_decay.append(self._virtualp['name'])
        self._virtualp['decay'] = vrt_decay
        self._decay = new_decay
