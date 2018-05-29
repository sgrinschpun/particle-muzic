from __future__ import division
add_library('beads')

baseFrequency = 200.0
sineCount = 10
currentGain = 1.0

ac = AudioContext()

masterGain = Gain(ac, 1, 0.5);
ac.out.addInput(masterGain)

sineTone=[]
sineFrequency=[]
sineGain=[]

for i in range(0,sineCount+1):
    sineFrequency.append(Glide(ac, baseFrequency*(i + 1),30))
    sineTone.append(WavePlayer(ac, sineFrequency[i],Buffer.SINE))
    sineGain.append(Gain(ac, 1, currentGain))
    sineGain[i].addInput(sineTone[i])
    masterGain.addInput(sineGain[i])
    currentGain -= 1.0/sineCount
ac.start()


def setup():
    size(600, 600)
    background(0)

    
def draw():
    baseFrequency = 20.0 + mouseX
    for i in range(1,sineCount+1):
        sineFrequency[i].setValue(baseFrequency*(i+1))
    


def stop():
    ac.stop()
