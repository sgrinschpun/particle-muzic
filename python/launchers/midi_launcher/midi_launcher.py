import mido
from phenomena import Phenomena
import time

midiToPart = {36: "u", 37: "d", 38: "c", 39: "s", 40: "t", 41: "b",
              42: "mu+", 43: "tau-e+", 44: "nubar_e", 45: "nubar_tau"}

input_port = mido.open_input('Teensy MIDI')
phenomena = Phenomena()
begin_time = time.time()
try:
    while True:
        msg = input_port.receive()
        print "Received message ", msg.bytes(), " from Teensy MIDI device."
        isNoteOn = msg.bytes()[2] == 100
        note = msg.bytes()[1]
        if isNoteOn:
            print "Sending ", midiToPart[note], " to Phenomena server."
            phenomena.addParticle(midiToPart[note])
except KeyboardInterrupt:
    pass

print "Total time: {0}".format(time.time() - begin_time)