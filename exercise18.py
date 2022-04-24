import random

def genNum():
    num = random.randint(1000,9999)
    num = str(num)
    return num
def findCows(g, n):
    c = 0
    for i in range(len(n)):
        if n[i] == g[i]:
            c = c+1
    return c

def findBulls(g, n):
    b = 0
    for i in range(len(n)):
        if g[i] in n:
            if g[i] != n[i]:
                b = b+1
    return b

while 1==1:
    num = genNum()
    guess = input("Guess a number: ")
    while guess != num:
        cows = findCows(guess, num)
        bulls = findBulls(guess, num)
        print(cows,"cows,",bulls,"bulls")
        guess = input('')
    print("Correct!")
    again = input("Play again? Y/n:")
    if again != 'Y':
        break
