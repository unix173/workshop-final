import socket
import sys
import Adafruit_DHT

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
sock.bind(server_address)
sock.listen(1)
print >> sys.stderr, 'Waiting for connection on ', server_address

while True:
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address
        while True:
            data = connection.recv(20)
            if data == 'get-temperature':
                # Messure temperature and send data to client
		humidity, temperature = Adafruit_DHT.read_retry(22, 4)
		connection.sendall(str(temperature))	        
		print("Temperature sensor activated")
            elif data == 'stream-start':
                # start video streamingx
                print("Stream started")
            elif data == 'stream-stop':
                # stop video streaming
                print("Streaming stopped")
            else:
		pass		
    except Exception as e:
        print("Error {}".format(e.message))
    finally:
	pass        
connection.close()
sock.close()	
