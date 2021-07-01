'''Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]'''
def armstrong(var):
    a=str(var)
    b=0
    c=0
    for i in (a):
        k=int(i)
        b=(k**3)
        c=b+c
    if c==var:
        print(f'the number {var} is armstrong ')
    else:
        print(f'the number {var} is not armstrong')
armstrong(1634)