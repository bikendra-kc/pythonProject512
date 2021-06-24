'''Q.No.3 Write a function calledshowNumbersthat takes a parameter calledlimit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
 For example, if the limit is 3, it should print:0 EVEN1 ODD2 EVEN'''
def calledshowNumbers(calledlimit):
    a=int(input('enter the number:'))
    b=a+1
    print(0)
    for i in range(1,b):
        if i%2==0:
            print(f'even:',i)
        else:
            print(f'odd:',i)
calledshowNumbers(5)