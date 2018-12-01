from __future__ import division
class CurrentCicle(object):
    
    def __init__(self,frameCountPerCicle): #50
        self.frameCountPerCicle = frameCountPerCicle
        self.ProgressRatioMax = (frameCountPerCicle-1)/frameCountPerCicle

    def update(self):
        self.number = frameCount//self.frameCountPerCicle
        self.FrameCount = frameCount%self.frameCountPerCicle
        self.ProgressRatio = self.FrameCount/self.frameCountPerCicle
        self.QuadEaseInRatio = self.ProgressRatio**2
        self.QuadEaseOutRatio = -(self.ProgressRatio - 1)**2 + 1
        self.QuartEaseInRatio = self.ProgressRatio**4
        self.QuartEaseOutRatio = -(self.ProgressRatio - 1)**4 + 1
        self.SextEaseOutRatio = -(self.ProgressRatio - 1)**6 + 1
