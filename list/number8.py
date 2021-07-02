'''8. Write a Python program to print a specified list after removing the 0th, 4th and 5th
elements'''
x = [0,1,2,3,4,5,6,7,8,9]
x= [a for (i,a) in enumerate(x) if i  not in (0,4,5)]
print(x)