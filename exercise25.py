"""
guesses=[]
def guessNumber(guess):
    print(guess)
    guesses.append(guess)
    accuracy = input('How close was I [y/h/l]: ')
    while (accuracy != 'y'):
        if (accuracy == 'h'):
            guessLower(guess)
        elif (accuracy == 'l'):
            guessHigher(guess)
        else:
            accuracy = input("Invalid input. Enter again: ")

def guessLower(start):
    guessNumber(int(start/2))

def guessHigher(start):
    newGuess = guesses[-1]/2
    newGuess = newGuess + start
    guessNumber(int(newGuess))
print("Think of a number between 1 and 100...")
print("Tell me when I guess it by entering y")
print("Tell me I'm too high by entering h")
print("Tell me I'm too low by entering l")
start = input("Ready to begin? [y/n]: ")


if start == 'y':
    guessNumber(50)
"""

def guess():
    low = 0
    high = 100
    mid = 50
    counter = 1
    correct = input("My guess is "+str(mid)+", am I right? y/h/l: ")
    while correct != 'y':
        if correct == 'h':
            low = mid

        elif correct == 'l':
            high = mid
            
        counter += 1
        mid = int((low+high)/2)
        correct = input("My guess is "+str(mid)+", am I right? y/h/l: ")
    print("It took",counter,"tries to guess your number!")


guess()
