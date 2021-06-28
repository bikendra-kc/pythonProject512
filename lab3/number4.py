'''Q.No.4 Write a function that returns the sum of multiples of 3 and 5 between 0 andlimit(parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, '''
def limited(a):
    b=0
    for i in range (a):
        if i%3==0 or i%5==0:
            b=i+b
    k=b
    return k

k=limited(20)
print(f'the sum of multiples of 5 and 3 between 0 and limit (parameter) is {k}')

