'''Q.No.2 Write a function calledfizz_buzzthat takes a number.If the number is divisible by 3,
 it should return “Fizz”.If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, it should return the same number.'''
def calledfizzBuzz():
    a=int(input('enter the number:'))
    if a%3==0 and a%5==0:
        print('fizzbuzz')
    elif a%3==0:
        print('fizz')
    elif a%5==0:
        print('buzz')
    else:
        print(a)
calledfizzBuzz()