import xml.etree.ElementTree as ET
import os

from phenomena.particles.sources import ParticleDataSource

# Finds all possible parents for a pair of particles. Works for getting the possible outcomes of a collision
# or the possible virtual particles in a decay if one of the particles is changed for its antiparticle
class InverseDecayList(object):

    def __init__(self,p1,p2):

        base = 'C:\Users\sergi\Anaconda2\Lib\site-packages\particletools'
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


        k1 = ParticleDataSource.getPDGId(p1)
        k2 = ParticleDataSource.getPDGId(p2)
        ids = [k1,k2]

        combs = []

        tags = [str(ids[0]),str(ids[1])]
        tagsR = [str(ids[1]),str(ids[0])]
        tagsbar = [str(-ids[0]), str(-ids[1])]
        tagsbarR = [str(-ids[1]), str(-ids[0])]
        for parent in root:
            if parent.tag == 'particle':
                for channel in parent:
                    if channel.attrib['products'] == ' '.join(tags) or channel.attrib['products'] == ' '.join(tagsR):
                        combs.append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tagsbar) or channel.attrib['products'] == ' '.join(tagsbarR):
                        try:
                            if parent.attrib['antiName'] not in combs:
                                combs.append(parent.attrib['antiName'])
                        except:
                            pass

        self._virtual_list = combs
