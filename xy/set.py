s={100,2,4,25,50,100}
print(s)
'''do not allow duplicate ,indexing [0:1], unordered or print randomly 
supports set operations like union intersection'''
s={12,2,3,4,(2,3,4,5)}
print(s)
'''cannot put list but tuple can be taken inside set'''
'''changing values of set'''
'add'
s={1,2,3}
s.add(10)
print(s)
'update'
s.update([5,6,7],{9,8,10})
print(s)
'removing element'
s={1,2,3,4,5}
s.remove(1)
'discard can remove the values that is not in set'
s.discard(6)
print(s)
'to remove one element '
t={3,4,5,6}
t.pop()
print(t)
'to clear all the values'
t.clear()
print(t)
