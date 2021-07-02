'''4. Write a Python program to construct the following pattern, using a nested for
loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range (2):
    if i==0:
        for j in range(6):
            print('*' * j)
    else:
        for j in range(4,0,-1):
            print('*'*j)
