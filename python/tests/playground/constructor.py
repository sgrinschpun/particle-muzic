from __future__ import print_function, division
import sys, math
sys.path.append('../')
from context import phenomena

from skhep.math import Point3D, Line3D, Plane3D, Vector3D, LorentzVector, Kallen_function, lifetime_to_width, width_to_lifetime
from skhep.constants import half_pi, two_pi
from skhep.units import MeV, GeV

from phenomena.particles.particle_boosted import ParticleBoosted

if __name__ == '__main__':
    pi = ParticleBoosted('pi+', theta = 1., p=2.)
    vector = Vector3D.fromsphericalcoords(2,half_pi,3*half_pi)
    fourmomenta = LorentzVector()
    fourmomenta.setpxpypzm(vector.x,vector.y,vector.z,pi.mass)  #accepts mass in GeV

    #0,0 -> 0,0,1
    #half_pi, 0 ->1,0,0
    #pi,0 -> 0,0,-1
    #half_pi, half_pi -> 0,1,0
    #half_pi, pi -> -1,0,0
    #half_pi,3*pi/2 -> 0,-1,0


    #print (pi.mass, pi.p, pi.E, pi.gamma, pi.theta)
    #print (fourmomenta.mass,fourmomenta.p,fourmomenta.t,fourmomenta.gamma)
    print (vector.x, vector.y, vector.z)
