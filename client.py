##########################################################
# Client program that with request for temperature
# Shown (client socket)
# - Everything is implemented except opening client socket
# - Show Server example first
##########################################################

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

while True:
    try:
        # get user input
        inp = raw_input("Enter option:")
	#Convert message to string for sending through socket
        message = str(inp)
        print >>sys.stderr, 'sending "%s"' % message
        if(message == 'get-temperature'):
            sock.sendall(message)
            data = sock.recv(16) # here we say we receive a double number
            print("Temperature is: ", data)
        else:
            sock.sendall(message)
    finally:
        pass
sock.close()

