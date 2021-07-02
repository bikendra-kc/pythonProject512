'''3. Write a Python program to guess a number between 1 to 9.
 Note : User is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on successful guess, user will
get a "Well guessed!" message, and the program will exit.
'''
import random
random = random.randint(1,9)
for i in range (9):
    guess=int(input("enter the guess:"))
    if guess == random :
        print("well guessed")
        break

print("programme end")