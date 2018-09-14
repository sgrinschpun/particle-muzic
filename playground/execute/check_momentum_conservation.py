from __future__ import print_function
import path
import math

from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    mypart = ParticleBoosted('mu+', p=1)
    print ("=====Transverse momentum=====")
    print ("pt_in:", mypart.p*math.sin(mypart.theta))
    pt_out = 0.
    for part in mypart.decayvalues:
        pt_out += part["p"]*math.sin(part["theta"])
        print ("pt_out", part["name"],":",part["p"]*math.sin(part["theta"]))
    print ("pt_out_all:", pt_out)
    print ("=====Long momentum=====")
    print ("pl_in:", mypart.p*math.cos(mypart.theta))
    pl_out = 0.
    for part in mypart.decayvalues:
        pl_out += part["p"]*math.cos(part["theta"])
        print ("pl_out", part["name"],":",part["p"]*math.cos(part["theta"]))
    print ("pl_out_all:", pl_out)
