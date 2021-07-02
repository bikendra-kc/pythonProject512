'''8. Write a Python program to get the Fibonacci series between 0 to 50.
 Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it'''
a=0
b=1
d=[]
while a<50 and b<50:
    d.append(a)
    d.append(b)
    a=a+b
    b=a+b
print(d)
