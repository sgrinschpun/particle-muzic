from classes import myShape, myParticle

def setup():
  size(500,500)

particle =myParticle(['ubar','ubar','dbar'])

def draw():
    background(0)
    
    particle.display()
    
    #if frameCount%4 == 0:
     #   saveFrame()
    #else:
    #    pass
