'''9 Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''
def palindrome(a):
    b = str(a[len(a)::-1])
    if a == b:
        print(f'the string {a} is palindrome')
    else:
        print(f'the string {a} is not palindrome')
palindrome('dad')
