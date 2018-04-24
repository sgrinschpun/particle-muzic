import socket, sys, OSC, re, time, threading, math
sys.path.insert(0, '../')
from phenomena_client import Phenomena


receive_address = {
    'ifae_imac': ('172.16.4.21', 7000), #Mac Adress, Outgoing Port  IFAE
    'ifae_macbook': ('172.16.4.24', 7000),
    'home_macbook':('192.168.1.71', 7000)
}

send_address = {
    'phone_ifae': ('172.16.4.31', 9000), #iPhone Adress, Incoming Port  IFAE
    'phone_home': ('192.168.1.144', 9000)
}


class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

s = OSC.OSCServer(receive_address['ifae_macbook'])

s.addDefaultHandlers()

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print (txt)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % data

#phenomena = Phenomena()
def sendParticle(addr, tags, data, client_address):
	action = {'1':'add','0':'delete'}
	if data == [1.0]:
		print "%s particle : %s" % (action[addr.split('/')[-2]], addr.split('/')[-1])
		#phenomena.addParticle(addr.split('/')[-1])

s.addMsgHandler("/1/e-/", sendParticle)
s.addMsgHandler("/1/mu-/", sendParticle)
s.addMsgHandler("/1/pi-/", sendParticle)
s.addMsgHandler("/1/H0/", sendParticle)

# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
	print addr

# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever() )
st.start()

# Loop while threads are running.
try :
	while 1 :
		time.sleep(10)

except KeyboardInterrupt :
	print "\nClosing OSCServer."
	s.close()
	print "Waiting for Server-thread to finish"
	st.join()
	print "Done"
