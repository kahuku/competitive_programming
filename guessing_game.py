guesses = []
responses = []
truth = [True for i in range(10)]

while True:
    guess = int(input())
    if guess == 0:
        break
    guesses.append(guess)
    responses.append(input())

for guess, response in zip(guesses, responses):
    guess -= 1
    if response == "too low":
        for i in range(guess + 1):
            truth[i] = False
    elif response == "too high":
        for i in range(guess, 10):
            truth[i] = False
    else:
        if truth[guess]:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        truth = [True for i in range(10)]
