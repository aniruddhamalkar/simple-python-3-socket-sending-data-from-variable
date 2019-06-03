import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # in here we created the socket & we notified the socket
# library that the socket is AF_INET means IPv4 address with SOCK_STREAM with TCP protocol
sock.bind((socket.gethostname(), 5555))  # here we bind the socket with local host and port number
# in here we could have put the IP address and port number. ,gethostname() retrieves the host name of the machine
# where the port indicates which service type you want to use. Port indicates the application level service that you
# want to use such as http, https for further port to application level mapping please visit
# https://www.cram.com/flashcards/application-layer-protocols-and-port-numbers-643487,
# https://vincenttechblog.com/40-network-protocols-with-port-numbers-transport-protocols-and-meanings/

sock.listen(5)  # this command listens the connections on the server IP and port number
# the number 5 inside the method indicates that we have 5 queues mean for simultaneous connection and heavy load
# it can have upto 5 connection in queue

# then after we want to listen to the connection for ever
while True:
    client_socket, ip_address = sock.accept()  # here storing client socket object in client_socket variables
# IP address of client is stored in ip_address variable
    print("Connection from {0} has been establish!".format(ip_address))
    client_socket.send(bytes("Welcome to the server!", "utf-8"))  # this line sent the infromation to client using
    # client_socket object, we are sending in terms of bytes in utf-8 format
    client_socket.close()
