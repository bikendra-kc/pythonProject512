'''Q.No.1 Write a Python function to find the Max of three numbers'''
def max():
    a = int(input('enter the number:'))
    b = int(input('enter the number2:'))
    c = int(input('enter the number 3:'))
    if a > b and a > c:
        print(f'the maximum number is {a}')
    elif b > c and b > a:
        print(f'the maximum number is {b}')
    else:
        print(f'the maximum number is {c}')
max()