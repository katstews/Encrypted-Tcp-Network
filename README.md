# Encrypted-Tcp-Network
This program only works one way where the client can only send one message. Messages are sent to each other encrypted using 128 AES bit encryption. Key must be 16 bytes when passed in. This program ensures confidentiality when messages are being sent from Client to Server. 

## How to run
Within the tcp folder contains the server and client. User must specify what port they want their server to run on, including what key that want to use. Run server first, the command will be structured as: 
> `python3 server.py <port number> <key>` 
