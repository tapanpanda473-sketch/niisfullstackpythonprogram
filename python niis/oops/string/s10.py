s="    ram"
print(len(s))
s=s.lstrip()
print(len(s))

s="ram   "
print(len(s))
s=s.rstrip()
print(len(s))

s="    ram"
print(len(s))
s=s.strip()
print(len(s))

s="welcome"
print(s.center(11,"*"))
print(s.ljust(11,"*"))
print(s.rjust(11,"*"))

s="welcome"
print(s.count("e"))

s="welcome"
print(s.index("e"))

s="welcome"
print(s.rindex("e"))

s="welcome"
print(s.find("e"))

s="welcome"
print(s.rfind("e"))

s="ram is a good boy"
print(s.startswith("ram"))

s="ram is a good boy"
print(s.startswith("is",4,6))

s="ram is a good boy"
print(s.endswith("boy"))

s="ram is a good boy"
l=s.split()
s1=" ".join(l)
print(s1)

s="ram is a good boy"
s=s.replace("good","x")
print(s)

s="ram"
b=s.encode()
print(b)
s1=b.decode()
print(s1)





