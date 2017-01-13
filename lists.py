l = list([6,5,9,4])

m = ([1,4,6,8])

for i in range(0, 4):
  print (l[i])

print ("***")

for i in range(1, 5):
  print (l[-i])

print ("***")

for i in l:
  print (i)
  
l.append(5)
l.append(6)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.remove(5)
print(l)

l.insert(0, 5)
print(l)

print(l.count(5))

l.extend(m)
print(l)

x = l.pop(2)
print(x, "is removed from ", l)

y = l.index(6)
print(y)
