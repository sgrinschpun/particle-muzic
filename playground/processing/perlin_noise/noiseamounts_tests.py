    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        if myShape.cycle%2 == 0:
            self.noiseAmount = 40*myShape.currentCicleQuartEaseInRatio
        elif myShape.cycle%2 == 1:
            self.noiseAmount = 40*(1-myShape.currentCicleQuartEaseInRatio)
            if myShape.currentCicleProgressRatio > 0.98:
                self._noiseSeed = random.randint(1, 99)
            else:
                pass
                
    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        self.noiseAmount = 40 * 0.5 - 40 * 5 * myShape.currentCicleProgressRatio + 40 * 5 * myShape.currentCicleQuadEaseInRatio
        if myShape.currentCicleProgressRatio > 0.98:
            self._noiseSeed = random.randint(1, 99)
        else:
            pass
            
    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        self.noiseAmount = 40* 0.5
        if myShape.currentCicleProgressRatio < 0.1:
            self.noiseAmount += self.noiseAmount * myShape.currentCicleProgressRatio * 10
        elif myShape.currentCicleProgressRatio < 0.2:
            self.noiseAmount += self.noiseAmount * (1 - (myShape.currentCicleProgressRatio - 0.1) * 10)        
        
        if myShape.currentCicleProgressRatio > 0.98:
            self._noiseSeed = random.randint(1, 99)
        else:
            pass
    
    def _set_noiseAmount(self):
        myShape.updateCurrentCicleProgress()
        self.noiseAmount = 40*myShape.currentCicleQuadEaseInRatio
        self._noiseSeed = random.randint(1, 99)
