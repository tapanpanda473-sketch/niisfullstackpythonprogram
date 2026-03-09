#wap to take a number from the keyboard check the no is sd dd td od +ve number
print("enter a number ")
no=int(input())
if no<0:
	n0=-no
if no<10:
   print("sd")
elif no<100:
     print("dd")
elif no<1000:
     print("td")
else:
    print("od")          

