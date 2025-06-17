import socket

#define a function called scan_ports that takes in two parameters
def scan_ports(host, ports):

    #initialize an empty list called open_ports
    open_ports = []

    #start a for loop that goes over every port in ports
    for port in ports:
        try:
            '''create a socket object from the socket module
            socket.AF_INET specifies the address family as IPV4, meaning we'll only use
            socket.SOCK_STREAM specifies the socket type as TCP, this is necessary to s
            for UDP use : SOCK_DGRAM
            a new socket object is created for each port
            '''
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #set a response expectancy of 0.5 seconds before moving on to the next port
            sock.settimeout(0.5)

            #store the result after attempting a TCP connection
            result = sock.connect_ex((host, port))

            #if the result is 0, then the connection attempt was sucessful aka port is >
            #indicates that a service is listening on that port
            if result == 0:
                #add all open ports to the open_ports liste we declared earlier
                open_ports.append(port)

            sock.close()

        #invalid hostname exception
        except socket.gaierror as e:
            print(f"Error scanning port {port}: Hostname resolution failed > {e}")

        #connection took too long
        except socket.timeout as e:
            print(f"Error scanning port {port}: connection timed out - {e}")

        #permission issues or other problems
        except OSError as e:
            print(f"Error scanning port {port}: Other issues prevailed - {e}")

    if open_ports:
    	return open_ports
    return[]
