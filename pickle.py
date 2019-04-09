class Employee:
	def __init__(self,ename,eno):
		self.ename=ename
		self.eno=eno
	def display(self):
		print(self.ename,self.eno)

import pickle
f=open('pqr.txt','wb')
name=input("enter emp name")
no=input("enter emp no")
e=Employee(name,no)
pickle.dump(e,f)
obj=pickle.load(f)
print(obj)
f.close()