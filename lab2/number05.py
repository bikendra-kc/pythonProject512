'''5. For given integer x, print ‘True’ if it is positive,
 print ‘False’ if it is negative and print ‘zero’ if it is 0.'''
x=int(input("enter the integer x:")
if x=='0':
    print('the number {x} is negative')
elif x>'0':
    print(f'the number {x} is positive')
else:
    print(f"the number {x} is neutral")
