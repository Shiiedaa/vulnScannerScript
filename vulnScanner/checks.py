import socket




#function to check if server allows anonymous login
'''
attempts to connect  to the FTP server on port 21 which is the default for FTP
'''
def check_ftp_anonymous(host, port=21):

try:

#create a TCP socket
	sock = socket.socket()

	sock.settimout(1)

#connect to the target host on the specified port
	sock.connect((host,port))

#Return the FTP server banner which gives either server version or software
	sock.recv(1024)

#send FTP "user" command with anonymous as username argument
	sock.sendall(b"USER anonymous\r\n")

#set response as the servers answer to the anonymous pass
	response = sock.recv(1024).decode()

	sock.close()

#if code retrieved = 230 , login was sucessfull
if "230" in response:
	return "Anonymous login allowed"
else:
	return "Requires credentials"
except Exception:
	return "Error occured"



#function to check telnet presence on host, port 23 is default 
def check_telnet(host, port=23):

return "telnet detected, insecure"



#function to retrieve HTTP server banner
def check_http_banner(host, port=80):

try:
	sock = socket.socket()
	sock.settimeout(1)
	sock.connect((host,port))
	sock.recv(1024)
	sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
	response = sock.recv(1024).decode()
	sock.close()

	return f"HTTP response banner:\n{banner}"
except ExceptionL
	return "HTTP service not accessible"

