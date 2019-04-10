# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('', 81))  # my port 80 is always used by MySQL server, so I choose port 81 here instead
serverSocket.listen(1)  # only 1 connection can go through port 81 at a time
# Fill in end
while True:
    # Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()  # the method to establish a new connection for the client
    try:
        message = connectionSocket.recv(1024)  # the method to receive the request from the client, 1024 is the size
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # store all the code in XXX.html to variable outputdata
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")  # this method ia to send the HTTP header to Socket
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")  # header for the 404 Not Found
        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>")  # a html code that prints 404 Not Found in the browser
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
