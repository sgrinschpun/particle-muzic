from __future__ import division
import random

class myShape(object):
    cicle = 0
    currentCicleFrameCount = 0.
    currentCicleProgressRatio = 0.
    currentCicleQuadEaseInRatio = 0.
    currentCicleQuadEaseOutRatio = 0.
    currentCicleQuartEaseInRatio = 0.
    currentCicleQuartEaseOutRatio = 0.
    currentCicleSextEaseOutRatio = 0.

    frameCountPerCicle = 50

    r = color(255,0,0)
    g = color(0,255,0)
    b = color(0,0,255)
    matterColors = [r,g,b]
    c = color(0,255,255)
    m = color(255,0,255)
    y = color(255,255,0)
    antimatterColors = [c,m,y]

    noiseScale = .006
    noiseAmount = 80
    N = 100

    quarkParamsValues={
        'colors':{'0': matterColors, '1' : antimatterColors},
        'wgt':{'2': 6, '1' : 3, '-1' : 3,'-2' : 3},
        'amp':{'1': 1, '2' : 4, '3' : 1}
    }

    def __init__(self,x,y,radius, color0, type,gen,q3):
        self.x = x
        self.y = y
        self.r0 = radius
        self.colors = myShape.quarkParamsValues['colors'][type]
        self.col = self.colors[color0]
        self._set_color()
        self.ampFactor=myShape.quarkParamsValues['amp'][gen]
        self.weight =myShape.quarkParamsValues['wgt'][q3]
        self._noiseSeed = random.randint(1, 99)
        self.testarray=[]
        self.p1=[]
        self.p2=[]
        self.xoff = 0;
        self.yoff = 1000;

    @staticmethod
    def updateCurrentCicleProgress():
        myShape.cicle = frameCount//myShape.frameCountPerCicle
        myShape.currentCicleFrameCount = frameCount%myShape.frameCountPerCicle
        myShape.currentCicleProgressRatio = myShape.currentCicleFrameCount/myShape.frameCountPerCicle
        myShape.currentCicleQuadEaseInRatio = myShape.currentCicleProgressRatio**2
        myShape.currentCicleQuadEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**2 + 1
        myShape.currentCicleQuartEaseInRatio = myShape.currentCicleProgressRatio**4
        myShape.currentCicleQuartEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**4 + 1
        myShape.currentCicleSextEaseOutRatio = -(myShape.currentCicleProgressRatio - 1)**6 + 1

    @staticmethod
    def p3map(value,start1,end1,start2,end2):
        delta1 = end1 - start1
        delta2 = end2 - start2
        return (delta2*(value - start1)/delta1)+start2

    @staticmethod
    def randomChoice(list):
        return random.choice(list)

    @staticmethod
    def next(item):
        if item in [0,1]:
            return item +1
        elif item == 2:
            return 0
        else:
            return 0

    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        if myShape.currentCicleProgressRatio <= 0.5:
            self.noiseAmount = 40*myShape.currentCicleQuadEaseOutRatio*self.ampFactor
        if myShape.currentCicleProgressRatio > 0.5:
            self.noiseAmount = 40*(1-myShape.currentCicleQuadEaseInRatio)*self.ampFactor
            if myShape.currentCicleProgressRatio > 0.97:
                self._noiseSeed = random.randint(1, 99)
            else:
                pass

    def _set_color_ex(self):
        if myShape.currentCicleProgressRatio == 0.0:
            self.col = self.colors[int(myShape.cicle)%3]
        else:
            pass

    def _set_r(self):
        if myShape.cicle == 0:
            self.r=self.r0*myShape.currentCicleSextEaseOutRatio
        elif myShape.cicle == 5:
            self.r=self.r0*(1-myShape.currentCicleSextEaseOutRatio)
        else:
            self.r=self.r0


    def _set_color(self):
        if myShape.currentCicleProgressRatio == 0.0 and myShape.cicle>0:
            self.col = self.colors[myShape.next(self.colors.index(self.col))]
        else:
            pass

    def _set_gluon(self):
        #if myShape.currentCicleProgressRatio == 0.0:
        self.p1 = random.choice(self.testarray)
        self.p2 = random.choice(self.testarray)
        strokeWeight(6)
        beginShape()
        for i in range(0,5):
            x = self.p1[0] + i*(self.p2[0]-self.p1[0])/5
            y = self.p1[1] + i*(self.p2[1]-self.p1[1])/5
           # x += self.p3map(noise(myShape.noiseScale*x,myShape.noiseScale*y,0),0,1,-self.noiseAmount,self.noiseAmount)
            #y += self.p3map(noise(myShape.noiseScale*x,myShape.noiseScale*y,1),0,1,-self.noiseAmount,self.noiseAmount)
            vertex(x,y)
        endShape()


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
            x += map(noise(myShape.noiseScale*x,myShape.noiseScale*y,0),0,1,-self.noiseAmount,self.noiseAmount)
            y += map(noise(myShape.noiseScale*x,myShape.noiseScale*y,1),0,1,-self.noiseAmount,self.noiseAmount)
            vertex(x,y)
            self.testarray.append([x,y])
        endShape()

        #self._set_gluon()


class myMeson(myShape):
    def __init__(self, x, y,radius, color0, type,gen,q3):
        super(myMeson, self).__init__(x,y, radius, color0, type,gen,q3)

class myBaryon(myShape):
    def __init__(self, x,y,radius, color0, type,gen,q3):
        super(myBaryon, self).__init__(x,y,radius, color0, type,gen,q3)

class myLepton(myShape):
    w = color(255,255,255)

    def __init__(self,x, y,radius, q3):
        self.x = x
        self.y = y
        self.r0 = radius
        self.col = myLepton.w
        self.colors = []
        self.ampFactor=myShape.quarkParamsValues['amp']['1']
        self.weight =myShape.quarkParamsValues['wgt']['1']
        self.testarray=[]
        self._noiseSeed = random.randint(1, 99)

    def _set_color(self):
        pass

class myParticle(object):
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

    def __init__(self,x,y,composition):
        self.x = x
        self.y = y
        self.composition = composition # array
        self._componentsObjects=[]
        self._addComponents()

    def _addComponents(self):
        if self.composition == []: # lepton also check boson!
            self._componentsObjects.append(myLepton(self.x,self.y,80,1))
        elif self.composition != []:
            for i, q in enumerate(self.composition):
                type = myParticle.quarkParams[q]['type']
                gen = myParticle.quarkParams[q]['gen']
                q3 = myParticle.quarkParams[q]['q3']
                if len(self.composition)==3:  # baryons
                    self._componentsObjects.append(myBaryon(self.x,self.y,160,i,type,gen,q3))
                if len(self.composition)==2:  #mesons
                    self._componentsObjects.append(myMeson(self.x,self.y,80,0,type,gen,q3))

    def display(self):
        for i, val in enumerate(self._componentsObjects):
            blendMode(ADD)
            self._componentsObjects[i].display()

class myMeson(myShape):
    def __init__(self, x, y,radius, color0, type,gen,q3):
        super(myMeson, self).__init__(x,y, radius, color0, type,gen,q3)
