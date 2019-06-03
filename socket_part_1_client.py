import socket
import sys
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# instead of binding this socket want to connect
sock.connect((socket.gethostname(), 5555))  # here instead of getsockethost name we must enter the ip of server
# but as we are doing it on same machine we will be using host name & remember the port number must match in both
# sockets
complete_messge = ""
while True: # this while loop makes sure that all the buffer data got recovered
    message = sock.recv( 4) # here we put the received message on to the buffer here we had 1024 buffer size
    if len(message) <= 0:
        break
# if you want to send and receive massive files the you can increase the buffer size
#     print(message.decode("utf-8")) # here we are printing the received message and decoding it with utf-8 standards
    else:
        complete_messge += message.decode("utf-8")
print(complete_messge)
