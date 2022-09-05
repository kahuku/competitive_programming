import random

num = random.randint(1,9)
counter = 1
guess = int(input("Try to guess the number I'm thinking of... "))
while (guess != num):
    if guess > num:
        print("too high, try again")
        guess = int(input())
    elif guess < num:
        print("too low, try again")
        guess = int(input())
    counter += 1
    

print("YOU GUESSED IT!")
print("Took you ", counter, "tries!")
