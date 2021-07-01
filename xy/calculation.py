def add():
    a=int(input("enter the first number"))
    b=int(input("enter the number "))
    c=a+b
    print(f"sum of number is ",c)
def sub(a,b):
    c = a-b
    print(f"defference of number is ", c)
def mul():
    a=int(input("enter the first number"))
    b=int(input("enter the number "))
    c=a*b
    return c
def divide(a,b):

    d=a/b
    return d
add()
sub(5,3)
c=mul()
print(f"multiplication of the numbers is",c)
d=divide(6,3)
print(f"division of the numbers is",d)

