#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

import json

from phenomena.particles.sources import ParticleDataSource

def load_file():
    with open('inelastic_data.json') as infile:
        data = json.load(infile, encoding='utf-8')
    return data

DATA = load_file()

class InelasticData(object):
    @staticmethod
    def energyCutParticles(part, target, energy):
        part_dict = InelasticData.allParticles(part,target)
        selection = []
        for particle in list(part_dict.keys()):
            if part_dict[particle][1] < energy:
                selection.append(particle)
        cut_dict = {k: v for k, v in part_dict.items() if k in selection}
        return cut_dict

    @staticmethod
    def allParticles(part,target):
        try:
            product = DATA[part][target]
        except:
            product = {}
        finally:
            return product

    @staticmethod
    def ProbabilitySum(part,target,energy):
        probability = 0.
        part_dict = InelasticData.energyCutParticles(part,target,energy)
        for part in part_dict:
            probability += part_dict[part][0]
        return probability

    @staticmethod
    def ProbabilityChannel(part, target, channel):
        return InelasticData.allParticles(part,target)[channel][0]

    @staticmethod
    def listOriginParticles():
        return list(DATA.keys())




def save_json():
    with open('./inelastic_data.json', 'w') as f:
        f.write(json.dumps(build_json(),indent=2, sort_keys=True, ensure_ascii=False))

def get_particles(part,target='p+'):
    part_dict = {}
    values = []
    partid = ParticleDataSource.getPDGId(part)
    targetid = ParticleDataSource.getPDGId(target)

    for item in ParticleDataSource.getParticleList():
        channels = ParticleDataSource.getDecayChannels(item[0])
        for channel in channels:
            if set([partid,targetid]).issubset(channel[1]):
                part_dict[item[1].name] = [channel[0],ParticleDataSource.getMass(item[1].name)-ParticleDataSource.getMass(target)]
    return part_dict

def build_json():
    part_dict = {}
    for item in ParticleDataSource.getParticleList():
        for target in ['p+', 'n0']:
            particles = get_particles(item[1].name,target)
            if particles != {}:
                if not part_dict.has_key(item[1].name):
                    part_dict[item[1].name]={}
                part_dict[item[1].name][target]=particles
    return part_dict
