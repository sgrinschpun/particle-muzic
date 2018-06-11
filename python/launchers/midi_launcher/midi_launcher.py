import mido
from phenomena import Phenomena
import time


midiToPart = { 36 : "u", 37 : "d", 38 : "c", 39 : "s", 40 : "t",
               41 : "b", 42 : "mu+", 43 : "tau-e+", 44 : "nubar_e", 45 : "nubar_tau"}

inport = mido.open_input('Teensy MIDI')
phenomena = Phenomena()
begin_time = time.time()

while True:
    msg = inport.receive()
    print "Received message: ", msg.bytes()
    isNoteOn = msg.bytes()[2] == 100
    note = msg.bytes()[1]
    if isNoteOn:
        print midiToPart[note]
        phenomena.addParticle(midiToPart[note])


print "Total time: {0}".format(time.time() - begin_time)