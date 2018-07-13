from __future__ import division, print_function
import math, random

from particle_boosted import ParticleBoosted

from particletools.tables import PYTHIAParticleData
pythia = PYTHIAParticleData()

NO_PARENT = -1
class ParticleVirtual(ParticleBoosted):

    def __init__(self, virtualdata, parent = NO_PARENT, **kwargs):
        self._set_name(virtualdata._name)  # Name of the particle pypdt convention
        self._set_id() # Class Counter
        self._set_pdgid(virtualdata._name) # Id from PDG, taken from pypdt
        self._mass = virtualdata._mass # Mass of the particle in GeV
        self._set_charge() # Charge of the particle taken from pypdt
        self._set_virtual_lifetime() # Lifetime of the particle, taken from pypdt
        self._type = virtual # Particle Type will always be virtual
        self._set_composition() # Particle quark compsition in format [[q1,q2],[q3,q4],...] taken from json.
        self._set_lifetime_ren() #Renormalization of the lifetime THIS SHOULD BE DONE AT THE NODES and brought back with callback
        self.decay = virtualdata._decay # Particle decay channel chosen
        self._set_time_to_decay()  # Particle time lived before decay, renormalized
        self._setParent(parent)

        self._params = boostParams._build_from_p(p=kwargs.get('p',None))
        self._theta = kwargs.get('theta',0)
        self._p = self._params.p
        self._E = self._params.E
        self._gamma = self._params.gamma
        self._beta = self._params.beta
        self._T = self._params.T

        self.decayvalues = DecayCalc(self._mass,self._gamma,self._theta,self.decay).values # sets values for decay particles

class VirtualChannel(object):

    def __init__(self,decay,mass,masses):

        self._load_xml()

        limits = self._set_limits(mass,masses)
        self._set_channel_choice(limits)
        if self._virtualp._name != []:
            self._set_mass(masses,self._virtualp._mass)
            self._set_virtual_decay(decay)


    def _load_xml(self):
        """Reads the xml and pics out particle data only. If no decay length
        is given, it will calculated from the width."""

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
        ids.append(pythia.pdg_id(self.decay[0]))
        ids.append(pythia.pdg_id(self.decay[1]))
        ids.append(pythia.pdg_id(self.decay[2]))

        #if k < 0:
        #    ids *= -1
        tags = [[str(ids[0]),str(ids[1])],
            [str(ids[0]),str(-ids[2])],
            [str(ids[0]),str(-ids[3])],
            [str(ids[1]),str(ids[2])],
            [str(ids[1]),str(ids[3])],
            [str(ids[2]),str(ids[3])]]
        tagsR = [[str(ids[1]),str(ids[0])],
            [str(-ids[2]),str(ids[0])],
            [str(-ids[3]),str(ids[0])],
            [str(ids[2]),str(ids[1])],
            [str(ids[3]),str(ids[1])],
            [str(ids[3]),str(ids[2])]]
        tagsbar = [[str(-ids[0]), str(-ids[1])],
            [str(-ids[0]),str(ids[2])],
            [str(-ids[0]),str(ids[3])],
            [str(-ids[1]),str(-ids[2])],
            [str(-ids[1]),str(-ids[3])],
            [str(-ids[2]),str(-ids[3])]]
        tagsbarR = [[str(-ids[0]), str(-ids[1])],
            [str(ids[2]),str(-ids[0])],
            [str(ids[3]),str(-ids[0])],
            [str(-ids[2]),str(-ids[1])],
            [str(-ids[3]),str(-ids[1])],
            [str(-ids[3]),str(-ids[2])]]
        combs = {'01':[], '02':[], '03':[], '12':[], '13':[], '23':[]}

        for parent in root:
            if parent.tag == 'particle':
                for channel in parent:
                    if channel.attrib['products'] == ' '.join(tags[0]) or channel.attrib['products'] == ' '.join(tagsR[0]):
                        combs['01'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[1]) or channel.attrib['products'] == ' '.join(tagsR[1]):
                        combs['02'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[2]) or channel.attrib['products'] == ' '.join(tagsR[2]):
                        combs['03'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[3]) or channel.attrib['products'] == ' '.join(tagsR[3]):
                        combs['12'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[4]) or channel.attrib['products'] == ' '.join(tagsR[4]):
                        combs['13'].append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tags[5]) or channel.attrib['products'] == ' '.join(tagsR[5]):
                        combs['23'].append(parent.attrib['name'])

                    if channel.attrib['products'] == ' '.join(tagsbar[0]) or channel.attrib['products'] == ' '.join(tagsbarR[0]):
                        combs['01'].append(pythia.pdg_id(parent.attrib['antiName']))
                    if channel.attrib['products'] == ' '.join(tagsbar[1]) or channel.attrib['products'] == ' '.join(tagsbarR[1]):
                        combs['02'].append(parent.attrib['antiName'])
                    if channel.attrib['products'] == ' '.join(tagsbar[2]) or channel.attrib['products'] == ' '.join(tagsbarR[2]):
                        combs['03'].append(parent.attrib['antiName'])
                    if channel.attrib['products'] == ' '.join(tagsbar[3]) or channel.attrib['products'] == ' '.join(tagsbarR[3]):
                        combs['12'].append(parent.attrib['antiName'])
                    if channel.attrib['products'] == ' '.join(tagsbar[4]) or channel.attrib['products'] == ' '.join(tagsbarR[4]):
                        combs['13'].append(parent.attrib['antiName'])
                    if channel.attrib['products'] == ' '.join(tagsbar[5]) or channel.attrib['products'] == ' '.join(tagsbarR[5]):
                        combs['23'].append(parent.attrib['antiName'])

        print(combs)
        print('\n')
        print(set(combs['01']).intersection(combs['23']))
        print(set(combs['02']).intersection(combs['13']))
        print(set(combs['03']).intersection(combs['12']))

        print('\n')
        print(self.decay)

        print('Fiesta!')

    def _set_mass_limits(mass,masses):
        return {
                    '12' : [masses[0]+masses[1],mass-masses[2]],
                    '13' : [masses[0]+masses[2],mass-masses[1]],
                    '23' : [masses[1]+masses[2],mass-masses[0]],
                }

    def _set_BW_mass(self,mass,limits):
        # Use self._virtualp._name
        # Mass
        virtual_mass =

        self._virtualp._mass = virtual_mass

    def _set_channel_choice(self,decay,limits):

        #Choose channel
        self._is_virtual = []
        # In general we can use
        chnum = []
        for particle in self._is_virtual
            if self._is_virtual(particle) == 1:
                chnum.append(str(self._is_virtual(paticle+1)))
        channel = ''.join(chnum)
        # For this specific 3 particle case, it might be simpler to use:
        # if self._is_virtual(0)==0:
        #     channel = '23'
        # elif self._is_virtual(1)==0:
        #     channel = '13'
        # else:
        #     channel = '12'

        virtual_particle = []
        # We must set the virtual particle name (could be empty) and then flag which masses will come from the virtual particle

        virtual_mass = self._set_BW_mass(virtual_particle_mass)

        # We set the threshold for no virtual decay if the virtual mass is on the lower end of our distribution
        # This way, it's more probable to see a virtual particle when we're close
        if (virtual_particle in ['W-','W+','Z0']) or self.virtual_mass => (limits[channel][0]+limits[channel][1])/2
            self._virtualp._name = virtual_particle
            self._virtualp._mass = virtual_mass
            self._virtualp._realmass = virtual_particle_mass
        else:
            self._virtualp._name = []


    def _set_mass(self,masses,virtual_mass):

        # We don't need the masses of the daughter particles, because they are looked up in DecayCalc
        # vrt_masses = []
        new_masses = []
        for particle in self._is_virtual
            # if self._is_virtual[particle] == 1:
            #     vrt_masses.append(masses[particle])
            # else:
            new_masses.append(masses[particle])
        new_masses.append(virtual_mass)
        # self._virtualp._masses = vrt_masses
        self._masses = new_masses


    def _set_virtual_decay(self,decay):
        vrt_decay = []
        new_decay = []
        for particle in self._is_virtual
            if self._is_virtual[particle] == 1:
                vrt_decay.append(decay[particle])
            else:
                new_decay.append(decay[particle])
        new_decay.append(self._virtualp._name)
        self._virtualp._vrtdecay = vrt_decay
        self._decay = new_decay
