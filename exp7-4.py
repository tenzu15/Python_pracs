class Rect:
    def __init__(self):
        self.leng=0
        self.wid=0
    def set(self,leng,wid):
        if leng>0.0 and leng<20.0:
            self.leng=leng
        if wid>0.0 and wid<20.0:
            self.wid=wid
        print("set sucessful")
    def get(self):
        print("length=",self.leng)
        print("width=",self.wid)
    def area(self):
        return self.leng*self.wid
    def peri(self):
        return 2*(self.leng+self.wid)
r=Rect()

print("1.enter length and width\n2.show leng and wid\n3.find area\n4.find peri\n5.exit")
n=int(input("enter ur choice"))
while(n!=5):
    print("1.enter length and width\n2.show leng and wid\n3.find area\n4.find peri\n5.exit")
    n=int(input("enter ur choice"))
    if n==1:
        l,b=int(input("enter length")),int(input("enter breadth"))
        r.set(l,b)
    elif n==2:
         r.get()
    elif n==3:
          print("area=",r.area())

    elif n==4:
        print("perimeter=",r.peri())
    else:
        break
