from __future__ import print_function
import path
import math

from phenomena.particles.particle_boosted import ParticleBoosted
from phenomena.particles.particle import ParticleDT

particle_decay_values = [{'E': 0.5812153828657481, 'name': 'mu+', 'p': 0.5715306515662815, 'theta': 0.003503180202956259}, {'E': 0.42847753327261906, 'name': 'nu_mu', 'p': 0.428477533272619, 'theta': -0.004672772548050403}]

if __name__ == '__main__':
    theta1 = particle_decay_values[0]["theta"]
    p1 = particle_decay_values[0]["p"]
    theta2 = particle_decay_values[1]["theta"]
    p2 = particle_decay_values[1]["p"]

    print ("pt1:", p1*math.sin(theta1))
    print ("pt2:", p2*math.sin(theta2))
    print ("pt:", round(p1*math.sin(theta1) + p2*math.sin(theta2),6))
    print ("=======")
    print ("pl1:", p1*math.cos(theta1))
    print ("pl2:", p2*math.cos(theta2))
    print ("pl:", round(p1*math.cos(theta1) + p2*math.cos(theta2),6))
