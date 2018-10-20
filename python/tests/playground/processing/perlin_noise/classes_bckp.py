from __future__ import division
import random
class myShape(object):
    currentCicleFrameCount = 0.
    currentCicleProgressRatio = 0.
    currentCicleQuadEaseInRatio = 0.
    currentCicleQuadEaseOutRatio = 0.
    currentCicleQuartEaseInRatio = 0.
    currentCicleQuartEaseOutRatio = 0.
    
    frameCountPerCicle = 50
    
    r = color(255,0,0)
    g = color(0,255,0)
    b = color(0,0,255)
    matterColors = [r,g,b]
    c = color(0,255,255)
    m = color(255,0,255)
    y = color(255,255,0)
    antimatterColors = [c,m,y]

    def __init__(self, radius, color):
        self.r = radius
        self.col = color
        self.weight = 6
        self.noiseScale = .006
        self.noiseAmount = 80
        self.N = 100
        self._noiseSeed = random.randint(1, 99)
        
    @staticmethod
    def updateCurrentCicleProgress():
        myShape.cycle = frameCount//myShape.frameCountPerCicle
        myShape.currentCicleFrameCount = frameCount%myShape.frameCountPerCicle
        myShape.currentCicleProgressRatio = myShape.currentCicleFrameCount/myShape.frameCountPerCicle
        myShape.currentCicleQuadEaseInRatio = myShape.currentCicleProgressRatio**2
        myShape.currentCicleQuadEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**2 + 1
        myShape.currentCicleQuartEaseInRatio = myShape.currentCicleProgressRatio**4
        myShape.currentCicleQuartEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**4 + 1
    
    @staticmethod
    def p3map(value,start1,end1,start2,end2):
        delta1 = end1 - start1
        delta2 = end2 - start2
        return (delta2*(value - start1)/delta1)+start2
    
    @staticmethod
    def randomChoice(list):
        return random.choice(list)
    
    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        if myShape.currentCicleProgressRatio <= 0.5:
            self.noiseAmount = 40*myShape.currentCicleQuadEaseOutRatio
        if myShape.currentCicleProgressRatio > 0.5:
            self.noiseAmount = 40*(1-myShape.currentCicleQuadEaseInRatio)
            if myShape.currentCicleProgressRatio > 0.97:
                self._noiseSeed = random.randint(1, 99)
            else:
                pass
    def _set_color(self):
        if myShape.currentCicleProgressRatio == 0.0:
            self.col = self.randomChoice(myShape.matterColors)
        else:
            pass
            
    def display(self):
        noFill()
        #self._set_color()
        stroke(self.col)
        strokeWeight(self.weight)
        print(myShape.currentCicleProgressRatio)
        beginShape()
        noiseSeed(self._noiseSeed)
        self._set_noiseAmount()
        for i in range(0,self.N+1):
            x = width/2 + self.r*cos(TWO_PI*i/self.N)
            y = height/2 + self.r*sin(TWO_PI*i/self.N)
            x += self.p3map(noise(self.noiseScale*x,self.noiseScale*y,0),0,1,-self.noiseAmount,self.noiseAmount)
            y += self.p3map(noise(self.noiseScale*x,self.noiseScale*y,1),0,1,-self.noiseAmount,self.noiseAmount)
            vertex(x,y)
        endShape()

class myParticle(object):
    def __init__(self,number): 
        self._quarks=[]
        #self._colors=[color(255,0,0),color(0,255,0),color(0,0,255)]
        self._colors=[color(255,0,0),color(0,255,255)]
        self._addQuarks(number)
    
    def _addQuarks(self, number):
        for n in range(0,number):
            self._quarks.append(myShape(80,self._colors[n%3]))
   
    def display(self):
        for item in range(0,len(self._quarks)):
            blendMode(ADD)
            self._quarks[item].display()
