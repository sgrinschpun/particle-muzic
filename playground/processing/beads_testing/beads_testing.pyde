from __future__ import division
add_library('beads')

def setup():
    global modulatorFrequency
    global ac

    size(400, 300)
    ac = AudioContext()
    
    modulatorFrequency = Glide(ac, 20, 30)
    modulator = WavePlayer(ac, modulatorFrequency, Buffer.SINE)
    
    class myFrequencyModulation(Function):
        def __init__(self, input):
            super(myFrequencyModulation, self).__init__(input)
            self.module=input
        
        def calculate(self):
            return self.module*200. + mouseY
        
    frequencyModulation = myFrequencyModulation(modulator)
    
    
    carrier = WavePlayer(ac, frequencyModulation,Buffer.SINE)
    
    g = Gain(ac, 1, 0.5)
    g.addInput(carrier)
    g.addInput(modulator)
    
    ac.out.addInput(g)
    
    ac.start()




    

def draw():
    background(0)
    modulatorFrequency.setValue(mouseX)
    
    
def stop():
    ac.stop()
