'''5. Write a Python program to remove an item from a set if it is present in the set.'''
s={1,2,3,4,5,6}
a=int(input('enter the number you wanna remove: '))
if a in s:
    s.remove(a)
    print(s)
else:
    print(f'the number is not present in set')