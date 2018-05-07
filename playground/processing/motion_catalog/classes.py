from __future__ import division

r = color(255,0,0) #color(193,39,45)
g = color(0,255,0) #color(38,117,60)
b = color(0,0,255) #color(42,53,110)
c = color(0,174,239)
m = color(236,0,140)
y = color(255,242,0)


class myCircle(object):
    currentCicleFrameCount = 0.
    currentCicleProgressRatio = 0.
    currentCicleQuadEaseInRatio = 0.
    currentCicleQuadEaseOutRatio = 0.
    currentCicleQuartEaseInRatio = 0.
    currentCicleQuartEaseOutRatio = 0.
    
    frameCountPerCicle = 120
    
    def __init__(self, radius, col):
        self.radius = radius
        self.col = col
        self.x = 320
        self.y = 320
        self.maxDisplacement = 0.
    
    @staticmethod
    def updateCurrentCicleProgress():
        myCircle.currentCicleFrameCount = frameCount%myCircle.frameCountPerCicle
        myCircle.currentCicleProgressRatio = myCircle.currentCicleFrameCount/myCircle.frameCountPerCicle
        myCircle.currentCicleQuadEaseInRatio = myCircle.currentCicleProgressRatio**2
        myCircle.currentCicleQuadEaseOutRatio = -(myCircle.currentCicleProgressRatio - 1)**2 + 1
        myCircle.currentCicleQuartEaseInRatio = myCircle.currentCicleProgressRatio**4
        myCircle.currentCicleQuartEaseOutRatio = -(myCircle.currentCicleProgressRatio - 1)**4 + 1
        
    
    def display(self):
        fill(self.col)
        noStroke() # Turn off stroke
        ellipse(self.x, self.y, self.radius, self.radius)
        
    def move(self):
        if frameCount % 1 == 0:
            myCircle.updateCurrentCicleProgress()
            self.maxDisplacement = 30*(1 - myCircle.currentCicleQuartEaseOutRatio)
            self.x = 320 + random(-self.maxDisplacement, self.maxDisplacement)
            self.y = 320 + random(-self.maxDisplacement, self.maxDisplacement)
        else:
            pass # Odd

        
class myParticle(object):
    def __init__(self): 
        self.circle1 = myCircle(80,r)
        self.circle2 = myCircle(80,g)
        self.circle3 = myCircle(80,b)
    
    def display(self):
        blendMode(ADD)
        self.circle1.display()
        self.circle2.display()
        self.circle3.display()
    
    def move(self):
        self.circle1.move()
        self.circle2.move()
        self.circle3.move()
    
