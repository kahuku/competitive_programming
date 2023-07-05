# decrypt is broken

alphabet = list(' abcdefghijklmnopqrstuvwxyz')

def encrypt(plaintext):
    prev = 0
    ciphertext = ''
    for char in plaintext:
        index = alphabet.index(char)
        ciphertext += alphabet[(prev + index) % 27]
        prev = (prev + index) % 27
    return ciphertext

def decrypt(ciphertext):
    prev = 0
    plaintext = ''
    for char in ciphertext:
        index = alphabet.index(char)
        print(char, index, prev)
        x = (index - prev) % 27
        letter = alphabet[x]
        plaintext += letter
        prev = x
    return plaintext

commands = [input() for _ in range(int(input()))]
for command in commands:
    if command[0] == 'e':
        print(encrypt(command[2:]))
    else:
        print(decrypt(command[2:]))