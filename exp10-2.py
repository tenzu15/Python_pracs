sf=input("enter source file")
df=input("enter dest file")
f1=open(sf,'r')
content=f1.read()
f1.close()
f2=open(df,'w')
f2.write(content)
f2.close()