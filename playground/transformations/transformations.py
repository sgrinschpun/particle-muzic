from __future__ import print_function
import path

from phenomena.particles.transformations import ComptonEffect, PairProduction
from phenomena.particles.models import BubbleChamberParticle

part1 = BubbleChamberParticle('gamma', p=1)
print (ComptonEffect(part1).values)
print (PairProduction(part1).values)

part2 = BubbleChamberParticle('mu-')
print (ComptonEffect(part2).values)
print (PairProduction(part2).values)
