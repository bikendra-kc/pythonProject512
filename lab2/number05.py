'''5. For given integer x, print ‘True’ if it is positive,
 print ‘False’ if it is negative and print ‘zero’ if it is 0.'''
a=int(input('enter the number:'))
if a>0:
    print(f'the number {a} is positive')
elif a<0:
    print(f'the number {a} is negative')
else:
    print(f'the number {a} is neutral')
