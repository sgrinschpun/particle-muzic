from __future__ import print_function

import path

from pynput import keyboard
from phenomena.phenomena_client import Phenomena

particle_keyboard = {
'p+':{keyboard.KeyCode(char='p')},
#'p-':{keyboard.Key.shift.shift,keyboard.KeyCode(char='P')},   what happens with p-?
'n0':{keyboard.KeyCode(char='n')},
'e-':{keyboard.KeyCode(char='e')},
'e+':{keyboard.Key.shift, keyboard.KeyCode(char='E')},
'pi-':{keyboard.KeyCode(char='i')},
'pi+':{keyboard.Key.shift, keyboard.KeyCode(char='I')},
'pi0':{keyboard.Key.alt, keyboard.KeyCode(char='I')},
'K-':{keyboard.KeyCode(char='k')},
'K+':{keyboard.Key.shift, keyboard.KeyCode(char='K')},
'K0':{keyboard.Key.alt, keyboard.KeyCode(char='K')},
'mu-':{keyboard.KeyCode(char='m')},
'mu+':{keyboard.Key.shift, keyboard.KeyCode(char='M')},
'tau-':{keyboard.KeyCode(char='t')},
'tau+':{keyboard.Key.shift, keyboard.KeyCode(char='T')},
'W-':{keyboard.KeyCode(char='w')},
'W+':{keyboard.Key.shift, keyboard.KeyCode(char='W')},
'Z0':{keyboard.KeyCode(char='z')},
'h0(H_1)':{keyboard.KeyCode(char='h')},
'B-':{keyboard.KeyCode(char='b')},
'B+':{keyboard.Key.shift, keyboard.KeyCode(char='B')},
'B0':{keyboard.Key.alt, keyboard.KeyCode(char='B')},
'D-':{keyboard.KeyCode(char='d')},
'D+':{keyboard.Key.shift, keyboard.KeyCode(char='D')},
'D0':{keyboard.Key.alt, keyboard.KeyCode(char='D')},
'J/psi':{keyboard.KeyCode(char='j')},
'Lambda0':{keyboard.KeyCode(char='l')},
'Sigma+':{keyboard.Key.shift, keyboard.KeyCode(char='S')},
'Sigma-':{keyboard.KeyCode(char='s')},
'Sigma0':{keyboard.Key.alt, keyboard.KeyCode(char='S')},
'Upsilon':{keyboard.KeyCode(char='u')},
'Xi-':{keyboard.KeyCode(char='x')},
'Xi0':{keyboard.Key.alt, keyboard.KeyCode(char='X')},
'gamma':{keyboard.KeyCode(char='g')},
'rho+':{keyboard.Key.shift, keyboard.KeyCode(char='R')},
'rho-':{keyboard.KeyCode(char='r')},
'rho0':{keyboard.Key.alt, keyboard.KeyCode(char='R')},
"eta\'":{keyboard.Key.alt, keyboard.KeyCode(char='V')},
'eta':{keyboard.KeyCode(char='v')},
'u':{keyboard.KeyCode(char='1')},
'ubar':{keyboard.Key.shift, keyboard.KeyCode(char='!')},
's':{keyboard.KeyCode(char='4')},
'sbar':{keyboard.Key.shift, keyboard.KeyCode(char='$')},
't':{keyboard.KeyCode(char='6')},
'tbar':{keyboard.Key.shift, keyboard.KeyCode(char='&')},
'b':{keyboard.KeyCode(char='5')},
'bbar':{keyboard.Key.shift, keyboard.KeyCode(char='%')},
'c':{keyboard.KeyCode(char='3')},
'cbar':{keyboard.Key.shift, keyboard.KeyCode(char='3')}, # not working
'd':{keyboard.KeyCode(char='2')},
'dbar':{keyboard.Key.shift, keyboard.KeyCode(char='\"')},
'K*-':{keyboard.KeyCode(char='a')},
'K*+':{keyboard.Key.shift, keyboard.KeyCode(char='A')},
'K*0':{keyboard.Key.alt, keyboard.KeyCode(char='A')},
'phi':{keyboard.KeyCode(char='f')},
'omega':{keyboard.KeyCode(char='o')},
'nu_e':{keyboard.KeyCode(char='q')},
'nubar_e':{keyboard.Key.shift, keyboard.KeyCode(char='Q')}
}

# The currently active modifiers
current = set()

phenomena = Phenomena()

def trigger_particle(particle):
    print (phenomena.addParticle(particle))

def on_press(key):
    current.add(key)
    #print ('Current: ', current)
    for particle, combination in particle_keyboard.iteritems():
        if all(k in current for k in combination):
            print('Triggering particle', particle)
            trigger_particle(particle)
            print('-----------')
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    try:
        current.remove(key)
        #print ('Current: ', current)
        #print('===========')
    except KeyError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
