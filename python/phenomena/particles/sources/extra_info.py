import json
from collections import namedtuple

from datasources import DataSourceFetcher

import json
from os.path import expanduser, join

HOME = expanduser("~")
JSON_PATH = join(HOME, '.phenomena/conf/part_extra_info.json')
XTRA_INFO = json.load(open(JSON_PATH))

class ExtraInfoFetcher(DataSourceFetcher):

    def getComposition(self, pdgid):
        composition =[]
        if XTRA_INFO[pdgid]['composition'] != []:
            for quark in XTRA_INFO[pdgid]['composition'][0]: #only consider first superposition of quarks
                composition.append(quark.encode('utf-8'))

        return composition

    def getType(self, pdgid):
        return XTRA_INFO[str(pdgid)]['type'].encode('utf-8')
