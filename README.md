# Encrypted-Tcp-Network
This program only works one way where the client can only send one message. Messages are sent to each other encrypted using 128 AES bit encryption. Key must be 16 bytes when passed in. This program ensures confidentiality when messages are being sent from Client to Server. 

## How to run
Within the tcp folder contains the server and client. User must specify what port they want their server to run on, including what key that want to use. Run server first, the command will be structured as: 
> `python3 server.py <port number> <key>` 
> 
The server will then bind to the given port address and store the key value. Next run client side to connect to the server, by running command in another terminal. Client must be specified with the server IP and port, plus the same key used for the server: 
> `python3 server.py <server IP> <server port number> <key>` 
>
Now the program should work. 

## Functionality 
Both client and server share a 16 bytes key, so thus the message sent to client and server must also be 16 bytes long. Both programs include *Cryptodome* libraries to add and remove paddings. No error handlings in the program, it expects the user to know better. Client program prompts user to enter a message, the program will then take that message and add the neccessary paddings if needed, then encrypt the message using the key the user passed in. Once the ciphertext is compiled, the client will then send the encrypted message over, rather than just plaintext. Once the server accepts the message, it will first be in ciphertext. But since the server has the special key, the server will then decrypt the message and unpad the message if nescessary. Then the server will display the original text. 
