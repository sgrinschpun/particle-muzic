#from phenomena import Phenomena
import mido
import rtmidi

#
# class MidiLauncher:
#
#     def __init__(self):
#         self._phenomena = Phenomena()
#
#     def send_particle(self):
#         particle = str()  # self._ui.particle_select_cbox.currentText()
#         number = 3  # self._ui.particles_number_spinbox.value()
#         print "Sending: {0} {1} ".format(particle, number)
#         self._phenomena.addParticle("K-")
#
#
# if __name__ == '__main__':
with mido.open_input('Teensy MIDI') as inport:
    for message in inport:
        print(message)
#midiLauncher = MidiLauncher