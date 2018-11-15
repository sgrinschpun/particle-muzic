from __future__ import division
import random, math

class myQuarkParams(object):
    quarkParams = {
        'u' : { 'type' : '0', 'gen' : '1', 'q3' : '2' },
        'd' : { 'type' : '0', 'gen' : '1', 'q3' : '-1'},
        'c' : { 'type' : '0', 'gen' : '2', 'q3' : '2' },
        's' : { 'type' : '0', 'gen' : '2', 'q3' : '-1'},
        't' : { 'type' : '0', 'gen' : '3', 'q3' : '2'},
        'b' : { 'type' : '0', 'gen' : '3', 'q3' : '-1'},
        'ubar' : { 'type' : '1', 'gen' : '1', 'q3' : '-2' },
        'dbar' : { 'type' : '1', 'gen' : '1', 'q3' : '1'},
        'cbar' : { 'type' : '1', 'gen' : '2', 'q3' : '-2' },
        'sbar' : { 'type' : '1', 'gen' : '2', 'q3' : '1'},
        'tbar' : { 'type' : '1', 'gen' : '3', 'q3' : '-2'},
        'bbar' : { 'type' : '1', 'gen' : '3', 'q3' : '1'}
        }

    quarkParamsValues={
        'colors':{'0': matterColors, '1' : antimatterColors},
        'wgt':{'2': 6, '1' : 3, '-1' : 3,'-2' : 3},
        'amp':{'1': 1, '2' : 4, '3' : 1}
    }

    def __init__(self,quark):
        self.colorSet = myQuarkParams.quarkParamsValues['color'][myQuarkParams.quarkParams[quark]['type']]

class myParticle(object):
    def __init__(self,x,y,particle):
        self.x = x
        self.y = y
        self._createParticle()

    def _createParticle(self):
        if self.composition == []:
            if self.particle.type == 'boson': # bosons
                self._createdParticle=myBoson(self.x,self.y,self.particle).display()
            if self..particle.type == 'lepton':  # leptons
                self._createdParticle=myLepton(self.x,self.y,self.particle).display()
            else
                pass   #add exception
        elif self.composition != []:
            if len(self.composition)==3:  # baryons
                self._createdParticle=myBaryon(self.x,self.y,self.name,self.mass,self.charge,self.timealive,self.composition)
            if len(self.composition)==2:  #mesons
                self._createdParticle=self._createdParticle=myMeson(self.x,self.y,self.name,self.mass,self.charge,self.timealive,self.composition)

    def display(self):
        self._createdParticle.display()

class currentCicle(object):
    def __init__(self,frameCountPerCicle): #50
        self.frameCountPerCicle = frameCountPerCicle
        def.update()

    def update():
        self.number = frameCount//self.frameCountPerCicle
        self.FrameCount = frameCount%self.frameCountPerCicle
        self.ProgressRatio = self.FrameCount/self.frameCountPerCicle
        self.QuadEaseInRatio = self.ProgressRatio**2
        self.QuadEaseOutRatio = -(self.ProgressRatio - 1)**2 + 1
        self.QuartEaseInRatio = self.ProgressRatio**4
        self.QuartEaseOutRatio = -(self.ProgressRatio - 1)**4 + 1
        self.SextEaseOutRatio = -(self.ProgressRatio - 1)**6 + 1

class myColors(object):
        r = color(255,0,0)
        g = color(0,255,0)
        b = color(0,0,255)
        matterColors = [r,g,b]
        c = myColors.getComplement(self.r)
        m = myColors.getComplement(self.g)
        y = myColors.getComplement(self.b)
        antimatterColors = [c,m,y]
        w = color(r+g+b)
        b = myColors.getComplement(self.w)

    def __init__(self,quark=0,i=0,currentCicle):
        self._set_colorSet(quark)
        self._set_color(i)
        self._currentCicle = currentCicle

    def _set_colorSet(self,quark):
        if quark == 0:
            self._colorSet = []
        else:
            self._colorSet=  myQuarkParams(quark).colorSet

    @property
    def color(self):
        return self._color

    def _set_color(self,i):
        if self._colorSet == []:
            self._color = myColors.w
        else:
            self._color = self._colorSet[i]

    def update_color(self):
        if self._colorSet == []:
            pass
        else:
            if self._currentCicle.ProgressRatio == 0.0 and self._currentCicle.number>0:
                prevColorIndex=self._colorSet.index(self._color)
                nextColorIndex=myColors.next(prevColorIndex)
                self._color = self._colorSet[nextColorIndex]

    @staticmethod
    def getComplement(original):
        R = red(original)
        G = green(original)
        B = blue(original)
        minRGB = min(R,min(G,B))
        maxRGB = max(R,max(G,B))
        minPlusMax = minRGB + maxRGB
        complement = color(minPlusMax-R, minPlusMax-G, minPlusMax-B)
        return complement

    @staticmethod
    def next(item):
        if item in [0,1]:
            return item +1
        elif item == 2:
            return 0
        else:
            return 0

    @staticmethod
    def randomChoice(list):
        return random.choice(list)


class myShape(object):
    noiseScale = .006
    noiseAmount = 80
    N = 100


    def display(self):
        noFill()





class Lepton(myParticle):

    color = MyColor


    def __init__(self, x, y,particle):
        self.x = x
        self.y = y

    def display(self):
        noFill()
        self._set_color()
        self._set_r()
        stroke(self.col)
        strokeWeight(self.weight)
        beginShape()
        noiseSeed(self._noiseSeed)
        self._set_noiseAmount()
        self.testarray=[]

        for i in range(0,myShape.N+1):
            x = self.x  + self.r*cos(TWO_PI*i/myShape.N) #width/2
            y = self.y + self.r*sin(TWO_PI*i/myShape.N) #height/2
            x += self.map(noise(myShape.noiseScale*x,myShape.noiseScale*y,0),0,1,-self.noiseAmount,self.noiseAmount)
            y += self.map(noise(myShape.noiseScale*x,myShape.noiseScale*y,1),0,1,-self.noiseAmount,self.noiseAmount)
            vertex(x,y)
            self.testarray.append([x,y])
        endShape()
