#7. Given a positive real number, print its fractional part.
a=int(input('enter the number:'))
b=int(a)
c=1
for i in range(a):
    c=b*c
    b-=1
print(f'the factorial of the number {a} is {c}')
#fractional
x=float(input('enter the number:' ))
y=int(x)
z=x-y
print(f'the fractional part of {x} is: ',z)