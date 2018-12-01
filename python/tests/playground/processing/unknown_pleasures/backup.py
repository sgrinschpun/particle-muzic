from __future__ import division
import math
bg = 20
s = 255

xoff = 0
yoff = 1000

r=180
limits=[]

N=100

magnitude=1

def u(n):
  return int((width/90)*n)

def build_shape(N):
    limits=[0 for x in range(N+1)]
    for i in range(0,N+1):
        limits[i]=[]
        limits[i].append(height/2+ r*math.sin(2*math.pi*i/N))
        limits[i].append([width/2 - r*math.cos(2*math.pi*i/N),width/2 + r*math.cos(2*math.pi*i/N)])
    return limits

def setup():
    global N
    global limits
    size(800,1000)
    background(bg)
    strokeWeight(2)
    stroke(s)
    smooth()
    

def draw():
    global xoff
    global yoff
    global magnitude
    limits = build_shape(N)
    print('1')
    background(bg)
    for i in range(0,N+1):
        y= limits[i][0]
        strokeWeight(int(y*0.005))
        stroke(map(y,height*0.1,height*0.9,50,255))
        pushMatrix()
        translate(0, y)
        noFill()
        beginShape()
        for x in range(int(limits[i][1][0]), int(limits[i][1][1])):
            ypos=map(noise(x/100 + xoff, y/100 + yoff), 0, 1, -100, 100)
            if x< width*0.5:
                magnitude= map(x, width*0.1, width*0.5, 0,1)
            else:
                magnitude = map(x, width*0.5, width*0.9, 1, 0) 
            ypos *= magnitude
            if ypos > 0: ypos = 0
            vertex(x, ypos)
        endShape()
        popMatrix()
    xoff += 0.01
    yoff += -0.01
