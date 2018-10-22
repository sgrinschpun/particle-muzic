from typeselection import TransTypeSelect
from channelselection import TransChannelSelector

from phenomena.particles.sources import ParticleDataSource

class TransformManager(object):

    def __init__(self, particle, transformationlist):
        #self._transformations = particle.__class__.TRANSFORMATIONS
        self._buildAllTransformations(particle, transformationlist)
        self._selectTransfType()
        self._selectTransfChannel()

    @property
    def allTypes(self):
        return self._allTransformations

    @property
    def selectedValues(self):
        return self._selTransfValues

    @property
    def selectedType(self):
        return self._selTransfType

    @property
    def selectedChannel(self):
        return self._selTransfChannel

    def selectByType(self, type):
        return [element for element in self._allTransformations if element['type'] == type][0]['list']

    def outputParticles(self, type):
        output_list =[]
        for element in self.selectByType(type):
            output_list.append(element[1][0])
        return output_list

    def _buildAllTransformations(self, particle, transformationlist):
        '''
        For each transformation possible for the particle, select the transformation channel and calculate the time of transformation. Store in a list
        self._allTransformations =
        [
            {
                'type': 'decay',
                'list': ['part1','part2'],
                'time': xxx
            },
            ...
        ]
        '''
        allTransformations = []
        for transf in transformationlist:
            item = transf(particle).values
            if item != {}:
                allTransformations.append(item)

        #spaghetti
        if not any('Decay2' in item['type'] for item in allTransformations):
            allTransformations.append({'type':'NoTransformation'})

        self._allTransformations = allTransformations

    def _selectTransfType(self):
        '''
        From all the possible transformations, choose one
        '''
        self._selTransfType = TransTypeSelect(self._allTransformations).value

    def _selectTransfChannel(self):
        '''
        From all the possible transformations, choose one
        '''
        try:
            channel = TransChannelSelector(self._selTransfType['list']).value
        except:
            channel = []
        finally:
            self._selTransfChannel = channel
