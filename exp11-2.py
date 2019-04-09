from Tkinter import *
root=Tk()
class Form:
	ro=0
	def __init__(self,root):
		ro=root
		self.f=Frame(root,height=1000,width=1000)
		self.f.propagate(0)
		self.f.pack()
		self.l1=Label(self.f,text="enter your name:",height=4,width=20,font=('Times',-15,))
		self.l2=Label(self.f,text="enter your age:",height=4,width=20,font=('Times',-15))
		self.l3=Label(self.f,text="enter your city:",height=4,width=20,font=('Times',-15))
		self.l4=Label(self.f,text="enter your gender:",height=4,width=20,font=('Times',-15))
		self.l5=Label(self.f,text="enter your fav games:",height=4,width=20,font=('Times',-15))
		
		self.l1.grid(row=0,column=0)
		self.l2.grid(row=1,column=0)
		self.l3.grid(row=2,column=0)
		self.l4.grid(row=3,column=0)
		self.l5.grid(row=4,column=0)

		self.var1=IntVar()
		self.var2=IntVar()

		self.c1=Checkbutton(self.f,font=('Roman',-15,'bold'),text="Cricket",variable=self.var1)#,command=self.display1)
		self.c1.grid(row=4,column=2)
		self.c2=Checkbutton(self.f,font=('Roman',-15,'bold'),text="Football",variable=self.var2)#,command=self.display1)
		self.c2.grid(row=4,column=4)

		self.var=IntVar()
		
		self.r1=Radiobutton(self.f,font=('Roman',-15,'bold'),text="male",variable=self.var,value=1)#,command=self.display2)
		self.r1.grid(row=3,column=2)
		self.r2=Radiobutton(self.f,font=('Roman',-15,'bold'),text="female",variable=self.var,value=2)#,command=self.display2)
		self.r2.grid(row=3,column=4)

		self.b1=Button(self.f,text="PRINT",font=('Times',-30,'bold'),height=2,width=8,command=self.display1)
		self.b1.grid(row=5,column=3)

		self.e1=Entry(self.f,font=('Times',-15,'bold'),width=25)
		self.e2=Entry(self.f,font=('Times',-15,'bold'),width=25)
		self.e1.grid(row=0,column=2)
		self.e2.grid(row=1,column=2)

		self.val=StringVar()
		self.s1=Spinbox(self.f,values=('Mumbai','Chennai','Kolkata','Delhi'),textvariable=self.val,font=('Times',-15,'bold'),width=25)
		self.s1.grid(row=2,column=2)

	def display1(self):
		c1=self.var1.get()
		c2=self.var2.get()
		str=''
		if c1==1:
			str+='Cricket'
		if c2==1:
			str+='Football'
		
		r=self.var.get()
		str1=''
		if r==1:
			str1+="your gender is: male"
		if r==2:
			str1+="your gender is: female"
		
		e1=self.e1.get()
		e2=self.e2.get()

		s1=self.val.get()

		self.t=Text(Form.ro,width=100,height=100,font=('Verdana',-20,'bold'),wrap='word')
		self.t.insert(END,'\nyour name is:'+e1)
		self.t.insert(END,'\nyour age is:'+e2)
		self.t.insert(END,'\nyour city is:'+s1)
		self.t.insert(END,'\n'+str1)
		self.t.insert(END,'\nyour fav games are:'+str)
		
		
		self.t.pack()
		self.t.pack(side=LEFT)
		


mb=Form(root)
root.mainloop()