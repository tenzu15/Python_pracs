class Dnz(Exception):
	def __init__(self):
		print("denominator cannot be zero")



a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=int(input("enter d"))
try:
	bd=b*d
	if bd<=0:
		raise Dnz()
	else:
		ans=((a+d)(b*c)/bd)
		print(ans)
except Dnz as d:
	print(d)	