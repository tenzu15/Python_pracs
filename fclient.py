import socket
host='localhost'
port=1000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
fname=input("enter a filename")
s.send(fname.encode())
msg=s.recv(1024)
while msg:
	print(msg.decode())
	msg=s.recv(1024)
s.close()