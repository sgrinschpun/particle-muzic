import random
from phenomena.particles.sources import ParticleDataSource

class Decay(object):
    @staticmethod
    def buildWeights(decay_channels):
        seq = []
        weights=[]
        for index, item in enumerate(decay_channels):
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

    @staticmethod
    def set(decay_channels):
        list_decay = []
        buildWeights = Decay.buildWeights(decay_channels)
        if decay_channels != []:
            choice = Decay.weightedChoice(buildWeights[0],buildWeights[1])
            channel = decay_channels[choice][1]
            for pdgid in channel:
                list_decay.append(ParticleDataSource.getName(pdgid))
        return list_decay
