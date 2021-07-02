'''6. Write a Python program to count the number of even and odd numbers from a
series of numbers.'''
a=(input('enter the number: '))
for i in (a):
    i=int(i)
    if i==0:
        print('the number 0 is odd')
    elif i%2==0:
        print(f'the number {i} is even')
    else:
        print(f'the number {i} is odd')