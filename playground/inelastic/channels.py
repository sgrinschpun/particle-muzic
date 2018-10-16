from __future__ import print_function, division
import path

from phenomena.particles.interactions.inelastic import InelasticData

if __name__ == '__main__':
    print (InelasticData.allParticles('pi-','p+'))
    print (InelasticData.energyCutParticles('pi-','p+',0.5))
    print (InelasticData.ProbabilitySum('pi-','p+',0.5))
    print (InelasticData.ProbabilityChannel('pi-','p+','Lambda0'))
    #print (InelasticInteraction.listOriginParticles())
