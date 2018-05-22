from __future__ import division
import random, math

from myParticle import MyParticle
from particle_list import *


e= MyParticle(100,100,e_params)
mu = MyParticle(100,200,mu_params)
tau = MyParticle(100,300,tau_params)
pi=MyParticle(200,100,pi_params)
n0 = MyParticle(300,100,n0_params)

allParticles=[e,pi,n0,mu,tau]

def setup():
  size(600,600)

def draw():
    background(0)
    
    for particle in allParticles:
        particle.display()
    
