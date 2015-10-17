######################################################
# Server program for responding to get-temperature 
# Shown(sockets, arguments, try-except-finally, if-elif)
# 1. Create server with IP:PORT
# 2. Open connection
# 3. Show exception handling
# 3. Handle messaging (send/receive) 
######################################################

# Gain access from another module
# Search and bind to current scope
import socket
import sys
import Adafruit_DHT


# Create a TCP/IP socket
# Get the sock object by calling socket(x,y)
# AF_INET = IPv4 address families, SOCK_STREAM = socket types constant
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line

# sys.argv list of arguments passed
# sys.argv[0] is name of the script, and first real argument is argv[1] 
server_name = sys.argv[1]
# Tupple -> Immutable list
server_address = (server_name, 10000)
# Bind socket to given address	
sock.bind(server_address)
# Socket reuse when forced close
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Listen to connections made to socket (Maximum system dependent, minimum 0)
sock.listen(1)
print >> sys.stderr, 'Waiting for connection on ', server_address

while True:
    	#Returns pair(con, cl_addr)	
	#connection is new object ready to send/recieve data	
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address
        while True:
	    # Returns string while buffsize should be relatively small power of two
	    # Accepts number of bytes
            data = connection.recv(20)
            if data == 'get-temperature':
                # Messure temperature and send data to client
		humidity, temperature = Adafruit_DHT.read_retry(22, 4)
		# In python you must send string through socket
		# Send whole string or error occures
		connection.sendall(str(temperature))	        
		print("Temperature sensor activated")
            else:
		pass
    # Explicit exception allows Exception object acces, 
    # but doesnt catch SystemExit, KeyboardInterrupt and GeneratorExit  			
    except Exception as e:
        print("Error {}".format(e.message))
    finally:
	pass        	
connection.close()
sock.close()	
