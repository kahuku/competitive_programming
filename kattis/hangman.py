word, alphabet = input(), input()
rounds = 0
for letter in alphabet:
    if letter in word:
        word = word.replace(letter, '')
        if word == '':
            break
    else:
        rounds += 1
if rounds < 10:
    print("WIN")
else:
    print("LOSE")



    ## USE SETS