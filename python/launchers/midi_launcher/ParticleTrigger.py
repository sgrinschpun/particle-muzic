import mido
from phenomena import Phenomena
from phenomena.utils.log import get_logger


class ParticleTrigger:

    def __init__(self, input_port_name):
        self._log = get_logger()
        self._log.info("Starting Particle Trigger MIDI Launcher")
        self._input_port_name = input_port_name
        self._input_port = mido.open_input(self._input_port_name)
        self._phenomena = Phenomena()
        self._midi_to_particle = {36: ["p+", "p-"], 37: ["n0"], 38: ["pi-", "pi+", "pi0"], 39: ["K-", "K+", "K0"],
                                  40: ["e-", "e+"], 41: ["mu-", "mu+"], 42: ["tau-", "tau+"], 43: ["H0"], 44: ["Z0"],
                                  45: ["W+", "W-"]}
        self._switching_note = 46
        self._last_triggering_note = 36
        self._msg = None
        self._is_note_on = None
        self._note = None
        self._switch_particle = 0

    def receive_midi_message(self):
        self._msg = self._input_port.receive()
        self._log.info("Received message " + str(self._msg.bytes()) + " from " + str(self._input_port_name))
        self._is_note_on = self._msg.bytes()[2] != 0
        self._note = self._msg.bytes()[1]
        self._manage_antimatter_note()

    def _manage_antimatter_note(self):
        if self._note == self._switching_note and self._is_note_on:
            self._log.info( "Is the anti-matter switch note!")
            if self._switch_particle < len(self._midi_to_particle[self._last_triggering_note])-1:
                self._switch_particle += 1
                self._log.info("Incrementing dictionary list position by one")
            elif self._switch_particle >= len(self._midi_to_particle[self._last_triggering_note])-1:
                self._switch_particle = 0
                self._log.info("Resetting dictionary list position to zero")

    @property
    def is_triggering_note(self):
        return self._is_note_on and self._note != self._switching_note

    def send_particle_to_phenomena(self):
        if particle_trigger.is_triggering_note:
            self._log.info("Is a triggering note!")
            self._last_triggering_note = self._note
            if self._switch_particle > len(self._midi_to_particle[self._note])-1:
                self._switch_particle = len(self._midi_to_particle[self._note])-1
            particle_string = self._midi_to_particle[self._note][self._switch_particle]  # type: str
            self._phenomena.addParticle(particle_string)
            self._log.info("Sent " + str(particle_string) + " to Phenomena server.")


if __name__ == '__main__':
    import time
    begin_time = time.time()
    particle_trigger = ParticleTrigger("Teensy MIDI")
    while True:
        particle_trigger.receive_midi_message()
        particle_trigger.send_particle_to_phenomena()
    print "Total time: {0}".format(time.time() - begin_time)