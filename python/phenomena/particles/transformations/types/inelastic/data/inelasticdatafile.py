#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"


from itertools import product
import json
import pkg_resources
from phenomena.particles.models import UndercoverParticle
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, ExtraInfoFetcher

class Inelastic2BodyFile(object):
    quarks = ['u','d','c','s','t','b','ubar','dbar','cbar','sbar','tbar','bbar']
    bosons = [['W+','W-'],['W-','W+']]
    quarkorder = {'u':1,'d':3,'c':5,'s':7,'t':9,'b':11,'ubar':2,'dbar':4,'cbar':6,'sbar':8,'tbar':10,'bbar':12}

    def __init__(self, part1, part2):
        self._build_quarkcharge()
        self._build_quarktransformation()
        self._part1 = UndercoverParticle(part1)
        self._comp1 = self._setUnderCoverList(self._part1.composition)
        self._part2 = UndercoverParticle(part2)
        self._comp2 = self._setUnderCoverList(self._part2.composition)
        self._build_all_options()
        self._build_all_outputs()
        self._build_all_particles()

    def _quarkOrder(self,quark):
        return Inelastic2BodyFile.quarkorder[quark]

    def _orderQuarks(self,listofquarks):
        listofquarks.sort(key=self._quarkOrder)
        return listofquarks

    @staticmethod
    def quarkOrder(quark):
        return Inelastic2BodyFile.quarkorder[quark]

    @staticmethod
    def orderQuarks(listofquarks):
        listofquarks.sort(key=Inelastic2BodyFile.quarkOrder)
        return listofquarks

    def _setUnderCoverList(self, complist):
        newlist = []
        for item in complist:
            newlist.append(UndercoverParticle(item))
        return newlist

    def _build_all_options(self):
        options1= {}
        options2= {}
        for charge in Inelastic2BodyFile.bosons:
            for quark1 in set(self._part1.composition):
                try:
                    newquarks1 = self._quarktransformation[charge[0]][quark1]
                    for quark2 in set(self._part2.composition):
                        try:
                            newquarks2 =self._quarktransformation[charge[1]][quark2]
                            options1[quark1]=self._orderQuarks(newquarks1)
                            options2[quark2]=self._orderQuarks(newquarks2)
                        except:
                            continue
                except:
                    continue
        self._options1 = options1
        self._options2 = options2

    def _build_all_outputs(self):
        outputs=[]
        for oldquark1, options1 in self._options1.iteritems():
            for id, newquark1 in enumerate(options1):
                newcomposition1 = self.replacequark(self._part1.composition,oldquark1,newquark1)
                for oldquark2, options2 in self._options2.iteritems():
                    for id, newquark2 in enumerate(options2):
                        thisoutput=[]
                        thisoutput.append(tuple(self._orderQuarks(newcomposition1)))
                        newcomposition2 = self.replacequark(self._part2.composition,oldquark2,newquark2)
                        thisoutput.append(tuple(self._orderQuarks(newcomposition2)))
                        outputs.append(thisoutput)
        self._outputs = outputs

    def _build_all_particles(self):
        particles_list = []
        for output in self._outputs:
            thispart=[]
            possibleparts = (part for part in output[1] if 't' not in part)
            for part in possibleparts:
                try:
                    partarray = ExtraInfoFetcher.getParticleByComposition(part)
                    thispart.append(partarray)
                except:
                    print ('Not found', part)
                    thispart.append(None)
            if [] not in thispart and len(thispart)>1:
                particles_list.append([output[0],thispart])
        new_particle_list = []
        for item in particles_list:
            [new_particle_list.append([item[0],[x,y]]) for (x,y) in product(item[1][0],item[1][1])]

        newer_particle_list = []
        init_charge = self._part1.charge + self._part2.charge
        for item in new_particle_list:
            final_charge = ParticleDataSource.getCharge(item[1][0]) + ParticleDataSource.getCharge(item[1][1])
            if final_charge ==  init_charge:
                newer_particle_list .append(item)

        self._particle_list = newer_particle_list



    def replacequark(self,quarklist,q1,q2):
        newquarklist = list(quarklist)
        for idx, quark in enumerate(newquarklist):
            if quark == q1:
                newquarklist[idx]=q2
                break
        return self._orderQuarks(newquarklist)


    def _build_quarkcharge(self):
        quark_charge = {}
        for q in Inelastic2BodyFile.quarks:
            quark_charge[q] = UndercoverParticle(q).charge
        self._quarkcharge = quark_charge

    def _build_quarktransformation(self):
        quark_list = self._setUnderCoverList(Inelastic2BodyFile.quarks)
        quark_transformation= {}
        for type in Inelastic2BodyFile.bosons[0]:
            quark_transformation[type]={}
            charge = ParticleDataSource.getCharge(type)
            for q in quark_list:
                newcharge = q.charge + charge
                if newcharge < 1 and newcharge > -1:
                    quark_transformation[type][q.name]=self.search_by_charge(newcharge)
        self._quarktransformation = quark_transformation

    def search_by_charge(self, charge):
        newlist = [key for key, value in self._quarkcharge.iteritems() if round(value,4) == round(charge,4)]
        return newlist

    @staticmethod
    def build_2body_file():
        particle_array = ['pi+','pi-','pi0','K+','K-','K0','J/psi','phi','Upsilon','B0','B+','B-','B_s0','B_c+','D+','D-','D0','D_s+','n0','p+','pbar-','Omega-','Omegabar+','Omega_c0','Omega_b-','Omega_bbar+','Xi0','Xi-','Xibar+','Xi_b0','Xi_b-','Xi_bbar+','Xi_cbar0','Xi_cbar-','Xi_c+','Sigma-','Sigma+','Sigma_b-','Sigma_b+','Sigma_cbar-','Sigma_cbar--','Sigma_c+','Sigma_c++','Delta++','Delta-','Deltabar--']
        inelastic_2body_data={}
        for target in ['p+','n0']:
            inelastic_2body_data[target] = {}
            for particle in particle_array:

                inelastic_output =Inelastic2BodyFile(particle,target)._particle_list
                if inelastic_output != []:
                    inelastic_2body_data[target][particle] = []
                    for output in inelastic_output:
                        mass = round(ParticleDataSource.getMass(output[0]) + ParticleDataSource.getMass(output[1]) - ParticleDataSource.getMass(target),4)
                        inelastic_2body_data[target][particle].append([mass,output])
        print (inelastic_2body_data)
        with open('./inelastic_2body_data.json', 'w') as f:
            f.write(json.dumps(inelastic_2body_data,indent=2, sort_keys=True, ensure_ascii=False))



class Inelastic1BodyFile(object):

    @staticmethod
    def save_json():
        with open('./inelastic_1body_data.json', 'w') as f:
            f.write(json.dumps(InelasticFile._build_json(),indent=2, sort_keys=True, ensure_ascii=False))

    @staticmethod
    def get_particles(part,target='p+'):
        finalstate = [part,target]
        part_list = []
        for item in ParticleDataToolFetcher.getOriginParticles(finalstate):
            energythreshold = ParticleDataSource.getMass(item[1][0])-ParticleDataSource.getMass(target)
            part_list.append([energythreshold,item])
        return part_list

    @staticmethod
    def _build_json():
        part_dict = {}
        for target in ['p+', 'n0']:
            part_dict[target]={}
            for item in ParticleDataSource.getParticleList():
                particles = InelasticFile.get_particles(item[1].name,target)
                if particles != []:
                    part_dict[target][item[1].name]=particles
        return part_dict
