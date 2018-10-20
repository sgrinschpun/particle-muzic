from __future__ import division
import random, math, json

from myParticle import MyParticle
from particle_list import *


#n0 = MyParticle(300,300,particle_json('n0'))


e= MyParticle(100,100,e_params)
#mu = MyParticle(100,200,mu_params)
#tau = MyParticle(100,300,tau_params)
pi=MyParticle(200,100,pi_params)

Z0 = MyParticle(400,100,Z0_params)
#Wplus = MyParticle(400,300,Wplus_params)
#Wminus = MyParticle(400,400,Wminus_params)
#H0 = MyParticle(400,200,H0_params)

allParticles=[pi]

def setup():
  size(600,600)

def draw():
    background(0)

    for particle in allParticles:
        particle.display()
