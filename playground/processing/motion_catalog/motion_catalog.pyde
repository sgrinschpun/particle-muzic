from classes import myParticle
#from classes import *

backgroundColor = 0 #240

particle = myParticle()

def setup():
    size(640, 640)

def draw():
    blendMode(BLEND)
    background(backgroundColor)
    particle.display()
    particle.move()
    
    
