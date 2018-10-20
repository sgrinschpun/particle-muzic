from __future__ import print_function, division
import math
import path

from skhep.math import Point3D, Line3D, Plane3D, Vector3D, LorentzVector, Kallen_function, lifetime_to_width, width_to_lifetime
from skhep.constants import half_pi, two_pi


def ro(x,y,z):
    return math.sqrt(x**2+y**2+z**2)

def theta(x,y,z):
    return math.atan2(math.sqrt(x**2+y**2)/z)

def phi(x,y,z):
    return math.atan2(y/x)

def transform(x,y,z):
    return [ro(x,y,z),theta(x,y,z),phi(x,y,z)]


def check(r,theta,phi):
    vector = Vector3D.fromsphericalcoords(r,theta,phi)
    return [round(vector.x,6),round(vector.y,6),round(vector.z,6)]



if __name__ == '__main__':

    print (check(1,0,0))
    print (check(1,math.pi/4,0))
    print (check(1,half_pi,0))
    print (check(1,math.pi,0))
    print (check(1,0,math.pi/4))
    print (check(1,half_pi,half_pi))
    print (check(1,half_pi,math.pi))
    print (check(1,half_pi,3*math.pi/2))


    #test = LorentzVector(1,1,1,3)
    #test2 = Vector3D.fromsphericalcoords(2,half_pi,0 )
    #test4 = Vector3D.fromsphericalcoords(2,2*math.pi,0 )
    #test = LorentzVector.from3vector(test2, 10)
    #test3 = LorentzVector()
    #test3.setpxpypzm(test2.x,test2.y,round(test2.z,6),70)

    #print("test4:", test4.x)
    #print("test4:", test4.y)
    #print("test4:", test4.z)
    #print("test3:", test3.e)

    #print(test.beta)
    #print(test.e)
    #print(test.et)
    #print(test.eta)
    #print(test.gamma)
    #print(test.m)
    #print("p:", test.p)
