def getComplement(original):
    R = (original >> 16) & 0xFF
    G = (original >> 8) & 0xFF
    B = original & 0xFF
    minRGB = min(R,min(G,B))
    maxRGB = max(R,max(G,B))
    minPlusMax = minRGB + maxRGB
    complement = color(minPlusMax-R, minPlusMax-G, minPlusMax-B)
    return complement

class MyColors(object):
    
    r = color(255,0,0)
    g = color(0,255,0)
    b = color(0,0,255)
    matterColors = [r,g,b]
    
    c = getComplement(r)
    m = getComplement(g)
    y = getComplement(b)
    
    antimatterColors = [c,m,y]
    
    allColors = [r,g,b,c,m,y]
    
    w = r+g+b
    b =color(0)
    
    def __init__(self,currentCicle, quark=0,i=0):
        self._set_colorSet(quark)
        self._set_color(i)  
        
        self._currentCicle=currentCicle
  
    def _set_colorSet(self,quark):
        if quark == 0:
            self._colorSet = []
        else:
            self._colorSet= myQuarkParams.getColorSet(quark)
    
    @property
    def color(self):
        return self._color

    def _set_color(self,i):
        if self._colorSet == []:
            self._color = MyColors.w
        else:
            self._color = self._colorSet[i]

    def update_color(self):
        if self._colorSet == []:
            pass
        else:
            if self._currentCicle.ProgressRatio == 0.0 and self._currentCicle.number>0:
                prevColorIndex=self._colorSet.index(self._color)
                nextColorIndex=MyColors.next(prevColorIndex)
                self._color = self._colorSet[nextColorIndex]      
    
    @staticmethod
    def next(item):
        if item in [0,1]:
            return item +1
        elif item == 2:
            return 0
        else:
            return 0

class myQuarkParams(object):
    quarkParams = {
        'u' : { 'type' : '0', 'gen' : '1', 'q3' : '2', 'mass':0.0022 },
        'd' : { 'type' : '0', 'gen' : '1', 'q3' : '-1', 'mass':0.0047},
        'c' : { 'type' : '0', 'gen' : '2', 'q3' : '2', 'mass':1.27 },
        's' : { 'type' : '0', 'gen' : '2', 'q3' : '-1', 'mass':0.096},
        't' : { 'type' : '0', 'gen' : '3', 'q3' : '2', 'mass':173.21},
        'b' : { 'type' : '0', 'gen' : '3', 'q3' : '-1', 'mass':4.18},
        'ubar' : { 'type' : '1', 'gen' : '1', 'q3' : '-2', 'mass':0.0022 },
        'dbar' : { 'type' : '1', 'gen' : '1', 'q3' : '1', 'mass':0.0047},
        'cbar' : { 'type' : '1', 'gen' : '2', 'q3' : '-2', 'mass':1.27 },
        'sbar' : { 'type' : '1', 'gen' : '2', 'q3' : '1', 'mass':0.096},
        'tbar' : { 'type' : '1', 'gen' : '3', 'q3' : '-2', 'mass':173.21},
        'bbar' : { 'type' : '1', 'gen' : '3', 'q3' : '1', 'mass':4.18}
        }

    quarkParamsValues={
        'colors':{'0': MyColors.matterColors, '1' : MyColors.antimatterColors},
        'wgt':{'2': 3, '1' : 2, '-1' : 1,'-2' : 2},
        'amp':{'1': 40, '2' : 60, '3' : 80},
        'speed':{'1': 50, '2' : 30, '3' : 10},
    }

    def __init__(self):
        pass
        
    @staticmethod
    def getnoiseScale(quark):
        #return map(myQuarkParams.quarkParams[quark]['mass'],0.0022,4.18,0.01,1)
        return 0.008
    
    
    @staticmethod
    def getColorSet(quark):
        return myQuarkParams.quarkParamsValues['colors'][myQuarkParams.quarkParams[quark]['type']]
    
    @staticmethod
    def getAmpFactor(quark):
        #return myQuarkParams.quarkParamsValues['amp'][myQuarkParams.quarkParams[quark]['gen']]
        return 80
    
    @staticmethod
    def getWeight(quark):
        return myQuarkParams.quarkParamsValues['wgt'][myQuarkParams.quarkParams[quark]['q3']]

    @staticmethod
    def getSpeed(quark):
        #return myQuarkParams.quarkParamsValues['speed'][myQuarkParams.quarkParams[quark]['gen']]
        return 70
