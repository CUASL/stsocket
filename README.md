# stsocket

TCP/IP connection (python) 

The primary socket API functions and methods in this module are:
-	socket()
-	bind()
-	listen()
-	accept()
-	connect()
-	connect_ex()
-	send()
-	recv()
-	close()
Why should you use TCP? The Transmission Control Protocol (TCP):
-	Is reliable: packets dropped in the network are detected and retransmitted by the sender.
-	Has in-order data delivery: data is read by your application in the order it was written by the sender.
In contrast, User Datagram Protocol (UDP) sockets created with socket.SOCK_DGRAM aren’t reliable, and data read by the receiver can be out-of-order from the sender’s writes.

