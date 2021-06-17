'''6. Given an integer number, print its last digit.'''
'''
8. Given a three-digit number. Find the sum of its digits.
9. Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400
10. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''
a=str(input('enter the number:'))
c=int(a)
for i in (a):
    c=c%10
print(f'the last digit is',c)

