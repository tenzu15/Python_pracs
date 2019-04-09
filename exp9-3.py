try:
	a=input("enter a")
	b=input("enter b")
	assert a==b,"not equal"
	print("equal")
except AssertionError as ae:
	print(ae)
