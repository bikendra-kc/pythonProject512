""". WAP which accepts marks of four subjects and display total marks,
 percentage and grade.
 Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail"""
subject1=int(input("enter the marks of subject 1:"))
subject2=int(input("enter the marks of subject 2:"))
subject3=int(input("enter the marks of subject 3:"))
subject4=int(input("enter the marks of subject 4:"))
total=subject1+subject2+subject3+subject4
print(f'the total marks of all subject is',total)
div=(total)*0.25
print(f'the total percent of all subjects is {div}% ')
if div>=70:
    print('you have got distinction')
elif div>60:
    print('you got first division')
elif div>40:
    print('you got passed')
else:
    print('you failed')