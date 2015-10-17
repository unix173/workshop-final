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
        # Send data
        inp = raw_input("Enter option:")
        message = str(inp)
        # print >>sys.stderr, 'sending "%s"' % message
        if(message == 'get-temperature'):
            sock.send(message)
            data = sock.recv(16)
            print("Temperature is: ", data)
        else:
            sock.sendall(message)
    finally:
        pass
sock.close()

