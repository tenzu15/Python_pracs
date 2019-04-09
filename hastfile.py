import hashlib

h=hashlib.sha1()
with open("names.txt",'rb')as f1:
    chunk=0
    while chunk!=b'':
        chunk=f1.read(1024)
        h.update(chunk)

print("sha-1:{0}".format(h.hexdigest()))
