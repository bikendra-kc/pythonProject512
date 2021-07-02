'''4. Write a Python script to check if a given key already exists in a dictionary'''
a={1:10,2:20,3:30,4:40}
key=4
if key in a.keys():
    print(f'the key already exists:')
else:
    print(f'the key does not exists')