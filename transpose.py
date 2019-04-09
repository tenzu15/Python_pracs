'''X=[[1,2,3],
   [5,6,7]]
T=[[0,0],
   [0,0],
   [0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        T[j][i]=X[i][j]
for r in T:
    print(r)



m1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
m2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])
res=np.dot(m1,m2)
print(res)

import numpy as np
m1=np.matrix([[1,2],[3,4]])
m2=np.matrix([[1,2],[3,4]])
print(m1+m2)

punct=''!@#$%^&*(){}[]:;'",./?~`''
st1="hello...$#@ world!!:"
st=""
for char in st1:
    if char not in punct:
        st=st+char
print(st)

st="zoobie hello i m pritu"
l1=st.split()
l1.sort()
for i in l1:
    print(i)

st=str(input("enter a string"))
st1=st[::-1]
print(st1)
if st1==st:
    print("pali")
else:
    print("not")

print("value:{0:4.2X}".format(16.344))

print(bin(16))
print(oct(16))
print(hex(16))

print(ord('c'))

n=int(input("enter a no"))
print("factors are:")
for i in range(1,n):
    if(n%i==0):
        print(i)

def gcd(x,y):
    while(y!=0):
        p=x%y
        x=y
        y=p
    return x

x=int(input("enter a no"))
y=int(input("enter a no"))
g=gcd(x,y)
lcm=(x*y)/g
print(g,lcm)

def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))

n=int(input("enter a no"))
#y=int(input("enter a no"))
for i in range(n):
    print(fib(i))


def summ(n):
    if n==0:
        return 0
    else:
        return (n+summ(n-1))

n=int(input("enter a no"))
print(summ(n))

    
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

n=int(input("enter a no"))
print(fact(n))

def bina(n):
    if n>1:
        bina(n//2)
    print(n%2,end='')
n=int(input("enter a no"))
bina(n)
'''
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

def rev(n):
    revn=n[::-1]
    print(revn)
    return

def testarm(n):
    num=n
    arm=0
    while(num!=0):
        p=num%10
        num=num//10
        arm=arm+(p*p*p)
    if(arm==n):
        print("armstrong")
    else:
        print("not")

def palin(n):
    revn=n[::-1]
    if(n==revn):
        print("pali")
    else:
        print("not")
    
def primet(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")

def fibo(n):
    a=0
    b=1
    while(n!=0):
        print(a)
        c=a+b
        a=b
        b=c
        n=n-1
        
fibo(10)

        
            


    





















































































         

