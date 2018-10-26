from phenomena.particles.transformations.selections import TypeSelector, ChannelSelector
from phenomena.particles.transformations.kinematics import KinematicsController
from phenomena.particles.transformations.time import TimeController

class TransformController(object):

    def __init__(self, particle, transformationlist):
        self._particle = particle
        self._buildTransformations(particle, transformationlist)
        self._selectType()
        self._selectChannel()
        self._setTime()

    @property
    def allTypes(self):
        return self._allTransformations

    @property
    def selectedType(self):
        return self._selectedType['type']

    @property
    def target(self):
        try:
            target = self._selectedType['target']
        except:
            target = ''
        finally:
            return target

    @property
    def selectedChannel(self):
        return self._selectedChannel[1]

    @property
    def output(self):
        return self._buildOutput(self._particle)

    @property
    def time(self):
        return self._time

    def _selectByType(self, type):
        return [element for element in self._allTransformations if element['type'] == type][0]['list']

    def _buildTransformations(self, particle, transformationlist):
        '''
        For each transformation possible for the particle, build list.
        '''
        allTransformations = []
        for transf in transformationlist:
            item = transf(particle).values
            if item != {}:
                allTransformations.append(item)

        #spaghetti
        if not any('Decay' in item['type'] for item in allTransformations):
            allTransformations.append({'type':'NoTransformation'})

        self._allTransformations = allTransformations

    def _selectType(self):
        '''
        From all the possible transformations, choose one
        '''
        self._selectedType = TypeSelector(self._allTransformations).value

    def _selectChannel(self):
        '''
        From all the possible channels, choose one
        '''
        try:
            channel = ChannelSelector(self._selectedType['list']).value
        except:
            channel = []
        finally:
            self._selectedChannel = channel

    def _buildOutput(self,particle):
        '''
        Get de list of output particles boosted values
        '''
        return KinematicsController(particle).getFinalState() if self.selectedType != 'NoTransformation' else None

    def _setTime(self):
        self._time = TimeController.getTime()
