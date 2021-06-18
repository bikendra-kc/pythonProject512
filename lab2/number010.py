'''10. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''
a=int(input('enter the number:'))
remainder1=a%10
x=a//10
remainder2=x%10
y=x//10
remainder3=y%10
sum=remainder1+remainder2+remainder3
if remainder1==remainder2 or remainder1==remainder3 or remainder2==remainder3:
    print(f'the sum of the integers is zero')
else:
    print(f'the sum of three digits are',sum)