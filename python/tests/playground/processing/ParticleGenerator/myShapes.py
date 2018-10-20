from __future__ import division
import abc, math
import random

from MyParams import MyColors

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

class myWaveCircle(MyShape):
    
    def __init__(self,x,y,paramsWaveCircle, currentCicle):
        self._x = x
        self._y = y
        self._strokeWeight = 6
        self._strokeColor = 240
        self._N = 2
        self._xoff = 0.
        self._yoff = 1000.
        self._deltaxoff = 0.01
        self._deltayoff = 0.01
        self._r0 = paramsWaveCircle['radius']
        self._magnitude = 1
        self._build_shape()
        
        
        self._currentCicle = currentCicle
    
    def _set_line(self,i,y):
        for x in range(int(self._limits[i][1][0]), int(self._limits[i][1][1])):
            ypos=map(noise(x/100 + self._xoff, y/100 + self._yoff), 0, 1, -100, 100)
            #magnitude = map(x, width*0.5, width*0.9, 1, 0) 
            #ypos *= magnitude
            #if ypos > 0: ypos = 0
            vertex(x, ypos)    
    
    def _set_lines(self):
        for i in range(0,self._N+1):
            y= self._limits[i][0]
            #strokeWeight(int(y*0.005))
            strokeWeight(self._strokeWeight)
            #stroke(map(y,height*0.1,height*0.9,50,255))
            stroke(random.choice(MyColors.allColors))
            #stroke(self._strokeColor)
            pushMatrix()
            translate(0, y)
            noFill()
            beginShape()
            self._set_line(i,y)
            endShape()
            popMatrix()
        
    
    def display(self):
        
        self._set_lines()
        self._xoff += self._deltaxoff
        self._yoff += self._deltayoff
  
    def move(self):
        pass  
    
    def _build_shape(self):
        limits=[0 for x in range(self._N+1)]
        for i in range(0,self._N+1):
            limits[i]=[]
            limits[i].append(self._y+ self._r0*math.sin(2*math.pi*i/self._N))
            limits[i].append([self._x- self._r0*math.cos(2*math.pi*i/self._N),self._x + self._r0*math.cos(2*math.pi*i/self._N)])
        self._limits=limits
