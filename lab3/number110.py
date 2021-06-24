'''10.write a programme to find the factorial of a number using functions'''
def factorial(a):
    b = int(a)
    c = 1
    for i in range(a):
        c = b * c
        b -= 1
    print(f'the factorial of the number {a} is {c}')
factorial(5)