import socket, OSC, re, time, threading, math

receive_address = '172.16.4.21', 7000 #Mac Adress, Outgoing Port  IFAE
send_address = '172.16.4.31', 9000 #iPhone Adress, Incoming Port  IFAE

class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


s = OSC.OSCServer(receive_address)

s.addDefaultHandlers()

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print (txt)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % data

s.addMsgHandler("/1/push1", handler)
s.addMsgHandler("/1/push2", handler)
s.addMsgHandler("/1/push3", handler)
s.addMsgHandler("/1/push4", handler)

# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
	print addr

# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
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
