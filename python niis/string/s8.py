#wap to initiliaze a string line by line
s = "welcome"
for i in range(len(s)):
    print(s[i:i+1])

s = "welcome"
for i in range(0,len(s),1):
	print(s[i])


s = "welcome"
for i in range(-len(s),0,1):
    print(s[i])	

#backward
# s ="welcome"
 #for i in range(len(s)-1,-len(s),-1):
    # print(s[i])





s="welcome"
for i in s:
    print(i)  




s = "welcome"
s=s[::-1]
for i in s:
    print(i)          
