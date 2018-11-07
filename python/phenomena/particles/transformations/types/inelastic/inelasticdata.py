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
from phenomena.particles.sources import ParticleDataSource, ParticleDataToolFetcher, ExtraInfoFetcher
#from phenomena.particles.models import UndercoverParticle

path = 'data/inelastic_2body_data.json'  # always use slash
JSON_PATH = pkg_resources.resource_filename(__name__, path)
DATA = json.load(open(JSON_PATH))

def load_file():
    with open('inelastic_1body_data.json') as infile:
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
    def listOriginParticles(target):
        return list(DATA[target].keys())
