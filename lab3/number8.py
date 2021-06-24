'''o.8 Write a Python function that takes a number as a parameter and check the number is prime or not.'''
def prime(Number):
        count = 0
        for j in range(2, (Number // 2 + 1)):
            if (Number % j == 0):
                count = count + 1
                break

        if (count == 0 and Number != 1):
            print(f'the number {Number} is prime')
        else:
            print(f'the number {Number} is not prime')
prime(75)