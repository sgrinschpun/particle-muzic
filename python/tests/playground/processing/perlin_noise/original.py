
def setup():
  size(500,500)
  noFill()
  stroke(32)
  strokeWeight(4)
  
r= 80
noiseScale = .002
noiseAmount = 50
N = 100;

def p3map(value,start1,end1,start2,end2):
    delta1 = end1 - start1
    delta2 = end2 - start2
    return (delta2*(value - start1)/delta1)+start2

def draw():
    background(248)

    beginShape()
    for i in range(0,N+1):
        x = width/2 + r*cos(TWO_PI*i/N)
        y = height/2 + r*sin(TWO_PI*i/N)
        x += p3map(noise(noiseScale*x,noiseScale*y,0),0,1,-noiseAmount,noiseAmount)
        y += p3map(noise(noiseScale*x,noiseScale*y,1),0,1,-noiseAmount,noiseAmount)
        vertex(x,y)
    endShape()
