#If temperature is greater than 30, it's a hot day other wise if it's less than 10; it's a cold day; otherwise, it's neither hot nor cold.
tem=int(input("enter the tempeature"))
if tem>30:
    print("the weather is hot",tem)
elif tem<10:
    print("the weather is cold",tem)
else:
    print("the weather is neither hot nor cold")
