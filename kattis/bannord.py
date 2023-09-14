bad_letters = set(list(input()))
sen = input().split()
for i in range(len(sen)):
    word = sen[i]
    bad = False
    for letter in word:
        if letter in bad_letters:
            bad = True
            break
    if i != len(sen) - 1:
        if bad:
            print('*' * len(word), end=' ')
        else:
            print(word, end=' ')
    else:
        if bad:
            print('*' * len(word))
        else:
            print(word)