'''10. Write a Python program to sum all the items in a dictionary'''
s={1:10,2:10,3:30,4:40,5:50}
k=0
a=0
b=0
for i,j in s.items():
    k=i+j+k
    a=i+a
    b=j+b
print(f'the sum of the keys and items only are',a,b)
print(f'the total of the items as well as keys is',k)