'''2. Write a Python program to convert temperatures to and from celsius,
fahrenheit.
 C = (5/9) * (F - 32)'''
c='n'
a=float(input('enter the temperature : '))

while c=='n':
    b = input('enter wheather the temperature is in celsius or fahrenheit: ')
    if b == "celsius":
        f = (a / (5 / 9)) + 32
        print(f'the temperature in fahrenheit is : ', f)
        c = 'k'
    elif b == "fahrenheit":
        f = (5 / 9) * (a - 32)
        print(f'the temperature in celsius is : ', f)
        c = 'h'
    else:
        print('invalid input : please input wheather the temperature is in  celsius or fahrenheit')


