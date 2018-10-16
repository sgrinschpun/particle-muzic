import json
#from os.path import expanduser, join

import pkg_resources
#HOME = expanduser("~")
#JSON_PATH = join(HOME, '.phenomena/conf/part_extra_info.json')
path = 'particle_extra_info/part_extra_info.json'  # always use slash
JSON_PATH = pkg_resources.resource_filename(__name__, path)
XTRA_INFO = json.load(open(JSON_PATH))

class ExtraInfoFetcher(object):

    @staticmethod
    def getComposition(pdgid):
        composition =[]
        try:
            if XTRA_INFO[str(pdgid)]['composition'] != []:
                for quark in XTRA_INFO[str(pdgid)]['composition'][0]: #only consider first superposition of quarks
                    composition.append(quark.encode('utf-8'))
        except KeyError:
            composition =[]
        finally:
            return composition

    @staticmethod
    def getType(pdgid):
        try:
            type = XTRA_INFO[str(pdgid)]['type'].encode('utf-8')
        except KeyError:
            type = 'quark'
        finally:
            return type
