import abc
import random

class MyShape(object):
    __metaclass__  = abc.ABCMeta
    
    @abc.abstractmethod
    def display(self):
        """Draws on screen every cicle, includes in and out"""
    
    @abc.abstractmethod
    def move(self):
        """Moves to next position on screen"""

#paramsWaveRing = { 'radius':, 'weight': ,'noiseScale': , 'ampFactor': ,'colors': }

class myWaveRing(MyShape):
    N=100

    def __init__(self,x,y,paramsWaveRing, currentCicle):
        self._x = x
        self._y = y
        self._currentCicle = currentCicle
        self._r0 = paramsWaveRing['radius']
        self._weight = paramsWaveRing['weight']
        self._noiseScale = paramsWaveRing['noiseScale']
        self._ampFactor = paramsWaveRing['ampFactor']
        self._myColors = paramsWaveRing['colors']
        self._noiseSeed = random.randint(1, 99)
    
    def display(self):
        noFill()
        self._currentCicle.update()
        self._myColors.update_color()
        self._set_r()
        stroke(self._myColors.color)
        strokeWeight(self._weight)
        
        beginShape()
        noiseSeed(self._noiseSeed)
        self._set_noiseAmount()
        self._set_vertex()
        endShape()
    
    def move(self):
        pass
    
    def _set_vertex(self):
        for i in range(0,myWaveRing.N+1):
            x = self._x  + self._r*cos(TWO_PI*i/myWaveRing.N)
            y = self._y + self._r*sin(TWO_PI*i/myWaveRing.N)
            x += map(noise(self._noiseScale*x,self._noiseScale*y,0),0,1,-self._noiseAmount,self._noiseAmount)
            y += map(noise(self._noiseScale*x,self._noiseScale*y,1),0,1,-self._noiseAmount,self._noiseAmount)
            vertex(x,y)
    
    def _set_r(self):
        if self._currentCicle.number == 0:
            self._r=self._r0*self._currentCicle.SextEaseOutRatio
        #elif self._currentCicle.number == 5:
        #    self.r=self.r0*(1-self._currentCicle.SextEaseOutRatio)
        else:
            self._r=self._r0
            
    def _set_noiseAmount(self):
        self._currentCicle.update()
        if self._currentCicle.ProgressRatio <= 0.5:
            self._noiseAmount = self._currentCicle.QuadEaseOutRatio*self._ampFactor
        if self._currentCicle.ProgressRatio > 0.5:
            self._noiseAmount = (1-self._currentCicle.QuadEaseInRatio)*self._ampFactor
            if self._currentCicle.ProgressRatio == self._currentCicle.ProgressRatioMax:
                self._noiseSeed = random.randint(1, 99)
            else:
                pass
   
