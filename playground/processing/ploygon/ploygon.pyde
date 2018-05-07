
from classes import myPolygon

backgroundColor = 0

w = 640
h = 640

polygon1 = myPolygon(200, color(255,0,0),12)

def setup():
    size(w, h)
    
def draw():
    blendMode(BLEND)
    background(backgroundColor)

    polygon1.display()
