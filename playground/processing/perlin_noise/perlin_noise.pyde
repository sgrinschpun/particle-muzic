from classes import myShape, myParticle



def setup():
  size(600,600)

allParticles=[]
p =myParticle(300,300,['u','u','d'])
allParticles.append(p)
#pi =myParticle(300,100,['u','dbar'])
#allParticles.append(pi)
#mu = myParticle(500,100,[])
#allParticles.append(mu)


def draw():

    background(0)
    
    for particle in allParticles:
        particle.display()
