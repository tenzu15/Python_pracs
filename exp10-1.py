def accept():
	name=input("enter student name")
	rno=input("enter rollno")
	f=open('student.txt','a')
	f.write('\nname-'+name+' rno'+rno)
	f.close()
def read():
	f1=open('student.txt','r')
	content=f1.read()
	print(content)
	f1.close()







n=int(input("1.Accept data\n 2.Read data"))
if n==1:
	accept()
else:
	read()
