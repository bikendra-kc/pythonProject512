#If name is less than 3 characters long- name must be at least 3 characters
 # otherwise if it's more than 50 characters - name must be maximum of 50 characters
  # otherwise - name looks good!

a=input('enter the name ')
if len(a)<3:
    print(f"name must be atleast 3 character")
elif len(a)>50:
    print(f"the name must not be longer than 50 character")
else:
    print(f"name looks good")