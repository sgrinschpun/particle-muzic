from __future__ import print_function, division
import sys
sys.path.append('../')
from context import phenomena

from phenomena.particles.models import BubbleChamberParticle, QuantumUniverseParticle, UndercoverParticle
from phenomena.particles.transformations.kinematics import ElasticKinematics, InelasticKinematics, DecayKinematics, LAB2BodyElastic, LAB2BodyInelastic
from phenomena.particles.transformations.kinematics import KinematicsController

from skhep import units as u
from skhep.math  import Kallen_function, Vector3D, LorentzVector

import math
import random



if __name__ == '__main__':

    initialparticle = QuantumUniverseParticle('pi-', p=1)
    target = UndercoverParticle('p+')
    Elasticfinalparticles= [UndercoverParticle('pi-'),UndercoverParticle('p+')]
    Inelasticfinalparticles=[UndercoverParticle('Delta0')]
    decay_particlelist= [UndercoverParticle('mu-'),UndercoverParticle('nu_mubar')]


    #calc = LAB2BodyElastic(initialparticle,target,Elasticfinalparticles)

    calc = LAB2BodyInelastic(initialparticle,target,Inelasticfinalparticles)
    print(calc.values)

    print ('E_i_LAB', initialparticle.fourMomentum.e + target.fourMomentum.e)
    print ('E_i_CM', calc._initialparticleCM.e + calc._targetCM.e)
    print ('E_f_LAB', calc.values[0].fourMomentum.e)
    print ('Pt_i_LAB', initialparticle.fourMomentum.pt + target.fourMomentum.pt)
    print ('Pt_f_LAB', calc.values[0].fourMomentum.pt)
    print (initialparticle.fourMomentum.p, calc.values[0].fourMomentum.p)



    #p = 1.
    # theta = random.uniform(0, math.pi)
    # phi = random.choice([-math.pi/2, -math.pi/2])
    # vector = Vector3D.fromsphericalcoords(p,theta,phi)
    # print ('x', vector.x)
    # print ('y', vector.y)
    # print ('z', vector.z)

    # z - y
    #phi 0, 0.5, 0.5, -0.5, -0.5,
    #theta 0, 0.5, 0.25, 0.5, 0.75, 1


    # A = target.mass/(pi.mass*pi.fourMomentum.gamma)
    # factor = 1/(A+1)
    # boostvector = pi.fourMomentum.boostvector*factor
    #
    # print (pi.fourMomentum.boost(boostvector))
    # print (target.fourMomentum.boost(boostvector))
    # s = (pi.fourMomentum.boost(boostvector).E+target.fourMomentum.boost(boostvector).E)**2




    # print(pi.transformation.selectedType)
    # print(pi.transformation.time)
    # print(pi.transformation.output)
    #
    # def callback():
    #     return print(pi.transformation.output)
    #
    # pi.start(callback)




    # dt = 1/60
    # time = 2
    # for i in range(int(time/dt)):
    #     print (pi.transformation.query(1./60.))
