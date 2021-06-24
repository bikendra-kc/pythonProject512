#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
# How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph;
# then run the next two at15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus?
a=float(input("enter the number of bus stop" ))
b=float(input("enter the time haulted"))
c=a*b
speed=float(input("enter the speed of bus in miles"))
distance=int(input("enter the ditance in  miles"))
time= (distance//speed) *60
total=c+time
print(f"time travelled by bus is",total)
x=int(input("enter the mile you jog in fist mile"))
y=int(input("enter  the mile you jog in second two miles "))
z=int(input("enter the mile you jog at last mile"))
p=(1/x)*60
q=(2/y)*60
r=(1/z)*60
jog=int(p+q+r)
print(f"the time taken by jogging",jog)
if (total > jog):
    print(f"trvelling by bus is faster",total)
else:
    print(f"travelling by jogging is faster",jog)
