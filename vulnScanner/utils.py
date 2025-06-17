# import socket
import socket

def is_ip_valid(ip):
        try:
                socket.inet_aton(ip)
                return True
        except socket.error:
                return False

