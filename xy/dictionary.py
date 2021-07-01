d={1:'apple',2:'banana'}
e={'apple':1,'banana':2}
f={'first':'1','second':'2'}
print(e['apple'])
'or'
print(d.get(1))
'0r'
print(d[1])
'assigning new value'
d[10]='litchi'
print(d)
'removing element'
d.pop(2)
print(d)
d.popitem()
print(d)
'removing all'
d.clear()
print(d)
'for i '
e={1:'apple',2:'banana'}
for i in e:
    print(i)
for i,j in e.items():
    print(i,j)
