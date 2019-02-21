#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pkg_resources

path = 'data/hadronization_data.json'  # always use slash
JSON_PATH = pkg_resources.resource_filename(__name__, path)
DATA = json.load(open(JSON_PATH))

class HadronizationData(object):

    @staticmethod
    def allParticles(part):
        try:
            channels = DATA[part]
        except:
            channels = []
        finally:
            return channels

    @staticmethod
    def listOriginParticles():
        return list(DATA.keys())
