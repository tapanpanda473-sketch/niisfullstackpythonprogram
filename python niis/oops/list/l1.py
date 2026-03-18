l=[10,2.5,"hi"]
l.append(30)
print(l)

l=[10,2.5,"hi"]
l.insert(2,30)
print(l)

l=[10,2.5,"hi"]
l.extend([4,5,6])
print(l)

l=[4,5,10,7,10,8,9,]
l.insert(2,30)
print(l)

l=[4,5,8,9]
l.pop()
print(l)

l=[4,5,8,9]
l.clear()
print(l)

l=[7,5,9,8]
l.sort()
print(l)

l=[4,5,8,9]
l.reverse()
print(l)

l=[4,5,8,9]
l.sort(reverse=True)
print(l)

l=[4,5,8,9,5]
print(l.count(5))

l=[7,5,9]
l1=l.copy()
l1.append(40)
print(l)
print(l1)

