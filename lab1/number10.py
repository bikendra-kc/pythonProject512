#10. Write a Python program to convert seconds to day, hour, minutes and seconds.
a=int(input("enter the time in seconds"))
days=a//86400
c=a%86400
hours=c//3600
e=c%3600
minutes=e//60
seconds=e%60
print(f"the time is {days} days, {hours}hours, {minutes}minutes and {seconds}seconds")

