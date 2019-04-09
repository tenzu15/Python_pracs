from tkinter import *
class Form:
    def __init__(self,root):
        self.f=Frame(root,height=1000,width=4000)
        #self.f.propogate(0)
        self.f.pack()
        fnt=('Times',-15)

        self.en1=StringVar()
        self.en2=StringVar()
        
        self.l1=Label(self.f,text="Login",height=4,width=10,font=fnt)
        self.l1.grid(row=1,column=0)
        self.e1=Entry(self.f,width=20,font=fnt,textvariable=self.en1)
        self.e1.grid(row=1,column=2)
        
        self.l2=Label(self.f,text="Password",height=4,width=10,font=fnt)
        self.l2.grid(row=1,column=4)
        self.e2=Entry(self.f,width=20,font=fnt,show='*',textvariable=self.en2)
        self.e2.grid(row=1,column=5)

        self.b1=Button(self.f,height=5,width=8,text="OK",font=fnt,command=self.display)
        self.b1.grid(row=2,column=2)

        
        self.b1=Button(self.f,height=5,width=8,text="RESET",font=fnt,command=self.reset)
        self.b1.grid(row=2,column=4)
    def display(self):
        e1=self.e1.get()
        e2=self.e2.get()
        
        self.l3=Label(self.f,text="name-"+e1,height=4,width=10,font=('Times',-15))
        self.l3.grid(row=4,column=2)
        
        self.l4=Label(self.f,text="passwrd-"+e2,height=4,width=10,font=('Times',-15))
        self.l4.grid(row=5,column=2)
    def reset(self):
        self.en1.set("")
        self.en2.set("")
root=Tk()        
        
f=Form(root)
root.mainloop()
