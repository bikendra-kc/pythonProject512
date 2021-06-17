'''4. Given three integers, print the smallest one. (Three integers should be user input'''
a=int(input('enter the number 1:'))
b=int(input('enter the number 2:'))
c=int(input('enter the number 3:'))
if a>b and a>c:
    print(f'the number {a} is the greatest')
elif b>a and b>c:
    print(f'the number {b} is the greatest')
else:
    print(f'the number {c} is the greatest')