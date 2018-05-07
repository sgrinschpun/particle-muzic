from __future__ import division
import math, random

w = 640
h = 640

class myPolygon(object):
    currentCicleFrameCount = 0.
    currentCicleProgressRatio = 0.
    currentCicleQuadEaseInRatio = 0.
    currentCicleQuadEaseOutRatio = 0.
    currentCicleQuartEaseInRatio = 0.
    currentCicleQuartEaseOutRatio = 0.
    
    def __init__(self, n, col, weight):
        self.n = n +1
        self.col = col
        self.weight = weight
        self._set_poly(n+1)
        self.vert = random.randint(0,self.n)
    
    @staticmethod
    def updateCurrentCicleProgress():
        myPolygon.currentCicleFrameCount = frameCount%myPolygon.frameCountPerCicle
        myPolygon.currentCicleProgressRatio = myPolygon.currentCicleFrameCount/myPolygon.frameCountPerCicle
        myPolygon.currentCicleQuadEaseInRatio = myPolygon.currentCicleProgressRatio**2
        myPolygon.currentCicleQuadEaseOutRatio = -(myPolygon.currentCicleProgressRatio - 1)**2 + 1
        myPolygon.currentCicleQuartEaseInRatio = myPolygon.currentCicleProgressRatio**4
        myPolygon.currentCicleQuartEaseOutRatio = -(myPolygon.currentCicleProgressRatio - 1)**4 + 1
    
    frameCountPerCicle = 120
    

    @staticmethod
    def renormalize(value,start1,end1,start2,end2):
        delta1 = end1 - start1
        delta2 = end2 - start2
        return (delta2*(value - start1)/delta1)+start2
    
    @staticmethod
    def logRenormalize(value, start1, stop1, start2, stop2):
        start2 = math.log(start2)
        stop2 = math.log(stop2)
        return math.exp(start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1)))
    
    @property
    def poly(self):
        return self._poly
    
    def _set_poly(self,n):
        poly = []
        for i in range(0,n):
            a = {}
            a['x']= w/2 + 100*math.sin(myPolygon.renormalize(i, 0, n-1, 0, 2*math.pi))
            a['y']= h/2 + 100*math.cos(myPolygon.renormalize(i, 0, n-1, 0, 2*math.pi))
            poly.append(a)
        self._poly = poly
    
    def _drawPoly(self,dx,dy):
        myPolygon.updateCurrentCicleProgress()
        beginShape()
        for i in range(0,self.n):
            self.bias = dist(self._poly[self.vert]['x'], self._poly[self.vert]['y'], self._poly[i]['x'], self._poly[i]['y'])*(1 - myPolygon.currentCicleQuadEaseInRatio)
            #self.maxDisplacement = self.bias*(1 - myPolygon.currentCicleQuadEaseInRatio)
            #self.changex= random.uniform(-self.maxDisplacement, self.maxDisplacement)
            #self.changey= random.uniform(-self.maxDisplacement, self.maxDisplacement)
            vertex(self._poly[i]['x']+dx/myPolygon.logRenormalize(self.bias, w, 0, dx, 45) , self._poly[i]['y']+dy/myPolygon.logRenormalize(self.bias, h, 0, dy, 45))
        endShape()
    
    def display(self):
        stroke(self.col)
        strokeWeight(self.weight)
        noFill()
        self._drawPoly(3000,3000)
