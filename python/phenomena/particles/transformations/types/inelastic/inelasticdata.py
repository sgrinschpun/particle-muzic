#!/usr/bin/env python

__author__ = "Sebastian Grinschpun"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "sgrinschpun@ifae.es"
__status__ = "Development"

import json
import pkg_resources
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher

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
            return product

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
