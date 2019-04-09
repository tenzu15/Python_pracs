import sys,os
fname=input("enter file name")
if os.path.isfile(fname):
	f=open(fname,'r')
else:
	print(fname+'file doesnt exist')
	sys.exit()
print("file contents")
print(f.read())
f.close()