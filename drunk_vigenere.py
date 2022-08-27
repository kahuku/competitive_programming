import string
ciphertext, key = input(), input()
plaintext = ''
alphabet = list(string.ascii_uppercase)
for i in range(len(ciphertext)):
    if i % 2 == 0:
        index = alphabet.index(ciphertext[i]) - alphabet.index(key[i])
    else:
        index = alphabet.index(ciphertext[i]) + alphabet.index(key[i])
    plaintext += alphabet[index % len(alphabet)]
print(plaintext)