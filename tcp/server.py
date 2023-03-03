import socket
import sys 
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
####### A SIMPLE ILLUSTRATION OF THE TCP SERVER #######
# The port number on which to listen for incoming
# connections.
PORT_NUMBER = int(sys.argv[1])
KEY = sys.argv[2]

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Associate the socket with the port
serverSock.bind(('', PORT_NUMBER)) 

# Start listening for incoming connections (we can have
# at most 100 connections waiting to be accepted before
# the server starts rejecting new connections)
serverSock.listen(100)

# Keep accepting connections forever
while True:
    print("Waiting for clients to connect...")

    # Accept a waiting connection
    cliSock, cliInfo = serverSock.accept()
    print("Client connected from: " + str(cliInfo))

    # Receive the data the client has to send.
    # This will receive at most 1024 bytes
    cliMsg = cliSock.recv(1024)
    print("Recieved:",cliMsg)
    
    deCrypt = AES.new(KEY.encode("utf-8"), AES.MODE_ECB)
    cliMsg = deCrypt.decrypt(cliMsg)
    cliMsg = unpad(cliMsg,16)
    print("Client sent: " + str(cliMsg))

    # Hang up the client's connection
    cliSock.close()