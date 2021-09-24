import socket

# Create the "phone"
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Dial the phone
mysock.connect(('data.pr4e.org', 80)) 
# Prepare request
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive information and print. Message must be translated from UTF (web) to Unicode (python)
while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode(), end='')

# End phone call
mysock.close()
