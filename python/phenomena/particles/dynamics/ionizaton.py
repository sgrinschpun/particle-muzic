import math
from skhep.constants import c_light
from skhep.math import Vector3D, LorentzVector
from phenomena.particles.models import BubbleChamberMedium

class Ionization(object):

    @staticmethod
    def BetheBlock(beta):
        return -2.1*BubbleChamberMedium.DENSITY/beta**2

    @staticmethod
    def EnergyLoss(fourmoment,timeinterval):
        return Ionization.BetheBlock(fourmoment.beta)

    @staticmethod
    def p_from_E(beta, E):
        return beta*E

    @staticmethod
    def New4momentum(oldfourmomentum):
        newEnergy = oldfourmomentum.e - Ionization.EnergyLoss(oldfourmomentum)
        newP = oldfourmomentum.beta*newEnergy
        newfourmomentum = LorentzVector.from3vector(newP*(oldfourmomentum.vector.unit()),newEnergy)
        return newfourmomentum
