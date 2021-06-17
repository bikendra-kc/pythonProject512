a=int(input("if the credit score is good enter 1 if the credit score is bad enter 0:"))
if a==1:
    price=1-(0.2*1)
    print(f"the price of the house in millions is ",price)
elif a==0:
    price=1-(0.1*1)
    print(f"the price of the house in millions is",price)