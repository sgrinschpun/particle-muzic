import abc
from MyParams import MyColors, myQuarkParams
from CurrentCicle import CurrentCicle
from myShapes import myWaveRing

class MyParticle(object):
    def __init__(self,x,y,params):
        self._x = x
        self._y = y
        self._params = params
        self.build_particle()
    
    def build_particle(self):
        if self._params['type'] == 'lepton':
            self._particle = MyLepton(self._x,self._y,self._params)
        
        if self._params['type'] == 'meson':
            self._particle = MyMeson(self._x,self._y,self._params)
        
        if self._params['type'] == 'baryon':
            self._particle = MyBaryon(self._x,self._y,self._params)
        
        if self._params['type'] == 'boson':
            pass
    
    def display(self):
        self._particle.display()
    
    def move(self):
        self._particle.move()

class MyParticleFamily(object):
    __metaclass__  = abc.ABCMeta
    
    def __init__(self,x,y,params):
        self._x = x
        self._y = y
        self._params = params
    
    @abc.abstractmethod
    def display(self):
        """Draws on screen every cicle, includes in and out"""
    
    @abc.abstractmethod
    def move(self):
        """Moves to next position on screen"""
    
        
class MyLepton(MyParticleFamily):
    def __init__(self,x,y,params):
        super(MyLepton, self).__init__(x,y,params)
        self.paramsWaveRing = {'radius':40, 
                               'weight': 4,
                               'noiseScale': 0.01,
                               'ampFactor': 70,
                               'speed':60
                                }
        self.currentCicle = CurrentCicle(self.paramsWaveRing['speed'])
        self.myColors = MyColors(self.currentCicle)
        self.paramsWaveRing['colors']=self.myColors
        self.add_myShapes()
    
    def add_myShapes(self):
        self._myShapes = []
        self._myShapes.append(myWaveRing(self._x,self._y,self.paramsWaveRing, self.currentCicle))
        
    def display(self):
        text(self._params['name'], self._x, self._y)
        for shape in self._myShapes:
            shape.display()
    
    def move(self):
        pass

class MyMeson(MyParticleFamily):
    def __init__(self,x,y,params):
        super(MyMeson, self).__init__(x,y,params)
        
        self.paramsWaveRing = []
        self.currentCicle = []
        self.myColors = []
        
        self._myShapes = []
        
        self.add_myShapes()
    
    def add_myShapes(self):
        for index, quark in enumerate(self._params['composition']):
            quarkParams = {
                    'radius':40, 
                    'weight': myQuarkParams.getWeight(quark),
                    'noiseScale': 0.01,
                    'ampFactor': myQuarkParams.getAmpFactor(quark),
                    'speed':myQuarkParams.getSpeed(quark)
            }
            self.paramsWaveRing.append(quarkParams)
            
            self.currentCicle.append(CurrentCicle(self.paramsWaveRing[index]['speed']))
            self.myColors.append(MyColors(self.currentCicle[index],quark))
            self.paramsWaveRing[index]['colors']=self.myColors[index]
            
            self._myShapes.append(myWaveRing(self._x,self._y,self.paramsWaveRing[index], self.currentCicle[index]))
            
    def display(self):
        text(self._params['name'], self._x, self._y)
        for shape in self._myShapes:
            blendMode(ADD)
            shape.display()
    
    def move(self):
        pass
        
class MyBaryon(MyParticleFamily):
    def __init__(self,x,y,params):
        super(MyBaryon, self).__init__(x,y,params)
        
        self.paramsWaveRing = []
        self.currentCicle = []
        self.myColors = []
        
        self._myShapes = []
        
        self.add_myShapes()
    
    def add_myShapes(self):
        for index, quark in enumerate(self._params['composition']):
            quarkParams = {
                    'radius':40, 
                    'weight': myQuarkParams.getWeight(quark),
                    'noiseScale': 0.01,
                    'ampFactor': myQuarkParams.getAmpFactor(quark),
                    'speed':myQuarkParams.getSpeed(quark)
            }
            self.paramsWaveRing.append(quarkParams)
            
            self.currentCicle.append(CurrentCicle(self.paramsWaveRing[index]['speed']))
            self.myColors.append(MyColors(self.currentCicle[index],quark,index))
            self.paramsWaveRing[index]['colors']=self.myColors[index]
            
            self._myShapes.append(myWaveRing(self._x,self._y,self.paramsWaveRing[index], self.currentCicle[index]))
            
    def display(self):
        text(self._params['name'], self._x, self._y)
        for shape in self._myShapes:
            blendMode(ADD)
            shape.display()
    
    def move(self):
        pass
