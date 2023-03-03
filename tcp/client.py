import socket
import sys
from Cryptodome.Cipher import AES 
from Cryptodome.Util.Padding import pad
# Server's IP address
SERVER_IP = sys.argv[1]

# The server's port number
SERVER_PORT = int(sys.argv[2])
KEY = sys.argv[3]

# The client's socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
cliSock.connect((SERVER_IP, SERVER_PORT))

# Send the message to the server
msg = input("Please enter a message to send to the server: ")

# Send the message to the server
# NOTE: the user input is of type string
# Sending data over the socket requires.
# First converting the string into bytes.
# encode() function achieves this. msg in string rn 
msg = pad(msg.encode(), 16)
# print(msg)

enCipher = AES.new(KEY.encode("utf-8"), AES.MODE_ECB)
cipherText = enCipher.encrypt(msg)
print("sent:",cipherText)

cliSock.send(cipherText)