#10. Write a Python program to convert seconds to day, hour, minutes and seconds.
a=int(input("enter the time in seconds"))
b=a//86400
c=a%86400
d=c//3600
e=c%3600
f=e//60
g=e%60
print(f"the time is {b} days, {d}hours, {f}minutes and {g}seconds")

