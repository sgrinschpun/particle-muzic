from __future__ import print_function

import path

from pynput.keyboard import Key, Listener
from pynput import keyboard

class MyException(Exception): pass

from pynput import keyboard

particle_keyboard = {
'p+':{keyboard.KeyCode(char='p')},
'p-':{keyboard.Key.shift.shift,keyboard.KeyCode(char='P')},
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

}


# The currently active modifiers
current = set()

def on_press(key):
    current.add(key)
    #print ('Current: ', current)
    for particle, combination in particle_keyboard.iteritems():
        if all(k in current for k in combination):
            print('Triggering particle', particle)
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


with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
