#swapping two number  using third variable
a=10
b=20
print("before swapping a=",a,"b=",b)
t=a
a=b
b=t
print("after swapping a=",a,"b=",b)
#swapping two numbers without using third variable
a=10
b=20
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping a=",a,"b=",b)
a=10
b=2.5
c="hi"
print(a,b,c)
print(type(a))
print(id(a))
a=10
b=20
a,b=b,a
print(a,b)
#swapping three number left to right using fourth variable 
a=20
b=40
c=50
print(a,b,c)
t=c
c=b
b=a
a=t
print(a,b,c)
#add two number without using +operator
a=10
b=20
c=a- -b
print(c)
print("e"in "hello")
print("x" in "hello")
print("x"not in "hello")
print(10 in [10,20,30,10])
print(40 in[10,20,30,10])
print(40 not in [10,20,30,40])
a=10
b=10
c=20
print(a is b)
print(a is c)
print(a is not c)
print(a==b)
