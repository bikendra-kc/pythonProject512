
import random
random = random.randint(1,10)
k=3
for i in range (3):
    k-=1
    guess=int(input("enter the number:"))
    if guess == random :
        print("the number is matched")
        break
    else:
        print(f"number is incorrect you have {k} attempt left")
print("programme end")
