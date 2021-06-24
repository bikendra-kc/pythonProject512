'''Q.No.7 Write a Python function that accepts a string and
calculate the number of upper case letters and lower case letters'''

def fun(a):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in a:
        if i.isupper():
           d["UPPER_CASE"]+=1
        elif i.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String is : ", a)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

fun('HokAge')