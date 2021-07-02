'''10.Write a Python program that accepts a string and calculate the number of
digits and letters'''
a=input('enter the string: ')
c=0
d=0
e=0
for j in (a):
    if j.isdigit():
        d=d+1
    elif j.isalpha():
        c=c+1
    else:
        e=e+1
print(f'the numbers of letters is {c}')
print(f'the numbers of digits is {d}')
print(f'the numbers of space is {e}')