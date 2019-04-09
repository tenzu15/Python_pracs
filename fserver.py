import socket
host='localhost'
port=1000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("connection from",str(addr))
fn=c.recv(1024)
fname=str(fn.decode())
f=open(fname,'rb+')
content=f.read()
c.send(content)
f.close()
s.close()