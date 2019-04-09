class Invalid(Exception):
	def __init__(self):
		print("invalid mks")
try:

	n=int(input("enter ur marks"))
	if n<0 or n>100:
		raise Invalid()
	print("valid mks")
except Invalid as i:
	print(i)


