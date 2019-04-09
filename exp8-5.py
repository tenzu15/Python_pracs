def recu(n):
    if n==0:
        return 0 
    else:
       return (n%10) + (recu(n//10))
n=int(input("ente a no"))
ans=recu(n)
print(ans)
