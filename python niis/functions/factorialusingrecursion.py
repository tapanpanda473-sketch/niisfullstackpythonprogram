f=1
def facttest(no):
	f=1
	if no>0:
		f=f*no
		n0=no-1
		facttest(no)
	 return f
print(facttest(3))	     	