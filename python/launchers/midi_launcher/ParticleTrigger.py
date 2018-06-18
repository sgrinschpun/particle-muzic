import mido
import random
import time
import threading
from phenomena import Phenomena
from phenomena.utils.log import get_logger



class ParticleTrigger:
    TRIGGER_TIME = 15    
    def __init__(self, input_port_name, timer_trigger = False):
        self._log = get_logger()
        self._log.info("Starting Particle Trigger MIDI Launcher")
        self._input_port_name = input_port_name
        self._input_port = mido.open_input(self._input_port_name)
        self._phenomena = Phenomena()
        self._midi_to_particle = {36: ["p+", "p-"], 37: ["n0"], 38: ["pi-", "pi+", "pi0"], 39: ["K-", "K+", "K0"],
                                  40: ["e-", "e+"], 41: ["mu-", "mu+"], 42: ["tau-", "tau+"], 43: ["H0"], 44: ["Z0"],
                                  45: ["W+", "W-"], 48: ["u", "ubar"], 49: ["d","dbar"], 50: ["c", "cbar"], 51: ["s", "sbar"],
                                  52: ["t", "tbar"], 53: ["b", "bbar"], 54: ["gamma0", "g0"], 55: ["nu_e","nubar_e"], 56: ["pi0","pi+","pi-"],
                                  57: ["K0", "K+","K-"], 58: ["J/psi(1S)0"], 59: ["Lambda0"], 60: ["B0"], 61: ["B+","B-"], 62: ["D0"],
                                  63: ["D+","D-"], 64: ["Upsilon(1D)0"], 65: ["Xi0"], 66: ["Xi+","Xi-"], 67: ["Omega(c)0"],
                                  68: ["Sigma+","Sigma-"], 69: ["Sigma0"], 66: ["Xi+","Xi-"], 71: ["Omega+","Omega-"], 72: ["eta0"]}
        self._switching_note = 6
        self._last_triggering_note = 36
        self._msg = None
        self._is_note_on = None
        self._note = None
        self._switch_particle = 0
        self._last_trigger_time = time.time()
        if timer_trigger:
            self._timer = threading.Timer(2, self._timeTrigger)
            self._timer.start()

    def _timeTrigger(self):
        if (time.time() - self._last_trigger_time) > ParticleTrigger.TRIGGER_TIME:
            self._is_note_on = True
            self._note = random.choice(self._midi_to_particle.keys())
            self.send_particle_to_phenomena()
        self._timer = threading.Timer(2, self._timeTrigger)
        self._timer.start()

    def receive_midi_message(self):
        self._msg = self._input_port.receive()
        print "Received message ", self._msg.bytes(), " from ", self._input_port_name
        self._is_note_on = self._msg.bytes()[2] != 0
        if self._is_note_on:
            self._note = self._msg.bytes()[1]
            self._manage_antimatter_note()

    def _manage_antimatter_note(self):
        if self._note == self._switching_note and self._is_note_on:
            self._log.info("Is the anti-matter switch note!")
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
        if self.is_triggering_note:
            self._last_trigger_time = time.time()
            self._log.info("Is a triggering note!")
            self._last_triggering_note = self._note
            try:
                if self._switch_particle > len(self._midi_to_particle[self._note])-1:
                    self._switch_particle = len(self._midi_to_particle[self._note])-1
                particle_string = self._midi_to_particle[self._note][self._switch_particle]  # type: str
                self._phenomena.addParticle(particle_string)
                self._log.info("Sent " + str(particle_string) + " to Phenomena server.")
            except Exception, ex:
                print "Exception: ",  ex.message
                self._phenomena.addParticle("u")
                self._log.info("Sending quark         ")


def launch_teensy():
    lego_trigger = ParticleTrigger("Teensy MIDI", timer_trigger = True)
    while True:
        lego_trigger.receive_midi_message()
        lego_trigger.send_particle_to_phenomena()
    print "Total time: {0}".format(time.time() - begin_time)


def launch_keyboard():
    keyboard_trigger = ParticleTrigger("UMX 25")
    while True:
        keyboard_trigger.receive_midi_message()
        keyboard_trigger.send_particle_to_phenomena()
    print "Total time: {0}".format(time.time() - begin_time)

if __name__ == '__main__':
    p1 = threading.Thread(target = launch_keyboard)
    p2 = threading.Thread(target = launch_teensy)
    p1.start()
    p2.start()
    p1.join()
    p2.join()