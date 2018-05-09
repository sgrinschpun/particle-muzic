from classes import myShape, myParticle

def setup():
  size(600,600)

p =myParticle(100,100,['u','u','d'])
pi =myParticle(300,100,['u','dbar'])
mu = myParticle(300,100,[])


def draw():
    background(0)
    
    p.display()
    pi.display()
    
    #if frameCount%4 == 0:
     #   saveFrame()
    #else:
    #    pass
