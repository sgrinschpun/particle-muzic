import random
from phenomena.particles.sources import ParticleDataSource

class ChannelSelector(object):

    def __init__(self, allChannels):
        self._allChannels = allChannels
        self._selectChannel()

    @property
    def value(self):
        return self._selectedChannel

    def _selectChannel(self):
        buildWeights = ChannelSelector.buildWeights(self._allChannels)
        if self._allChannels != [{'type':'NoTransformation'}]:
            choice = ChannelSelector.weightedChoice(buildWeights[0],buildWeights[1])
            if choice == None:
                channel = random.choice(self._allChannels)
            else:
                channel = self._allChannels[choice]
        self._selectedChannel = channel

    @staticmethod
    def buildWeights(transformation_channels):
        seq = []
        weights=[]
        for index, item in enumerate(transformation_channels):
            if item[0] != 0.0:           # do not use channels with prob = 0.0
                seq.append(index)
                weights.append(item[0])
        return seq, weights

    @staticmethod
    def weightedChoice(seq, weights):
        assert len(weights) == len(seq)
        #assert abs(1. - sum(weights)) < 1e-6
        x = random.random()
        for i, elmt in enumerate(seq):
            if x <= weights[i]:
                return elmt
            x -= weights[i]
