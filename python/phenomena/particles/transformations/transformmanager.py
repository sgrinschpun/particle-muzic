from outputcalculation import TransCalculation

from phenomena.particles.transformations.selections import TransTypeSelect, TransChannelSelector
from phenomena.particles.sources import ParticleDataSource

class TransformManager(object):

    def __init__(self, particle, transformationlist):
        self._particle = particle
        self._buildAllTransformations(particle, transformationlist)
        self._selectTransfType()
        self._selectTransfChannel()

    @property
    def allTypes(self):
        return self._allTransformations

    @property
    def selectedType(self):
        return self._selTransfType['type']

    @property
    def target(self):
        return self._selTransfType['target']

    @property
    def selectedChannel(self):
        return self._selTransfChannel

    @property
    def outputValues(self):
        return self._buildOutputList(self._particle)

    def selectByType(self, type):
        return [element for element in self._allTransformations if element['type'] == type][0]['list']

    def _buildAllTransformations(self, particle, transformationlist):
        '''
        For each transformation possible for the particle, build list.
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
        From all the possible channels, choose one
        '''
        try:
            channel = TransChannelSelector(self._selTransfType['list']).value
        except:
            channel = []
        finally:
            self._selTransfChannel = channel

    def _buildOutputList(self,particle):
        '''
        Get de list of output particles boosted values
        '''
        return TransCalculation(particle, self.selectedType).getOutputValues() if self.selectedType != 'NoTransformation' else None
