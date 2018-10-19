#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

import json
import pkg_resources
from phenomena.particles.sources import ParticleDataSource

path = 'inelastic_data.json'  # always use slash
JSON_PATH = pkg_resources.resource_filename(__name__, path)
DATA = json.load(open(JSON_PATH))

def load_file():
    with open('inelastic_data.json') as infile:
        data = json.load(infile, encoding='utf-8')
    return data

class InelasticData(object):
    @staticmethod
    def energyCutParticles(part, target, energy):
        part_list = InelasticData.allParticles(part,target)
        selection = [item[1] for item in part_list if item[0] < energy]
        return selection

    @staticmethod
    def allParticles(part,target):
        try:
            product = DATA[target][part]
        except:
            product = []
        finally:
            return InelasticData.listToTuple(product)

    @staticmethod
    def listToTuple(part_list):
        new_part_list = []
        for n, i in enumerate(part_list):
            a = [i[0], (i[1][0],map(ParticleDataSource.getPDGId, i[1][1]))]
            new_part_list.append(a)
        return new_part_list



    @staticmethod
    def ProbabilitySum(part,target,energy):
        probability = 0.
        part_list = InelasticData.energyCutParticles(part,target,energy)
        for part in part_list:
            probability += part[1][0]
        return probability

    @staticmethod
    def ProbabilityChannel(part, target, channel):
        return InelasticData.allParticles(part,target)[channel][0]

    @staticmethod
    def listOriginParticles(target):
        return list(DATA[target].keys())

class InelasticFile(object):

    @staticmethod
    def save_json():
        with open('./inelastic_data.json', 'w') as f:
            f.write(json.dumps(InelasticFile.build_json(),indent=2, sort_keys=True, ensure_ascii=False))

    @staticmethod
    def get_particles(part,target='p+'):
        part_list = []
        partid = ParticleDataSource.getPDGId(part)
        targetid = ParticleDataSource.getPDGId(target)

        for item in ParticleDataSource.getParticleList():
            channels = ParticleDataSource.getDecayChannels(item[0])
            for channel in channels:
                if set([partid,targetid]).issubset(channel[1]):
                    energythreshold = ParticleDataSource.getMass(item[1].name)-ParticleDataSource.getMass(target)
                    tuple = (channel[0],[item[1].name])
                    list = [energythreshold,tuple]
                    part_list.append(list)
        return part_list

    @staticmethod
    def build_json():
        part_dict = {}
        for target in ['p+', 'n0', 'e-']:
            part_dict[target]={}
            for item in ParticleDataSource.getParticleList():
                particles = InelasticFile.get_particles(item[1].name,target)
                if particles != []:
                    part_dict[target][item[1].name]=particles
        return part_dict


if __name__ == '__main__':
    save_json()
