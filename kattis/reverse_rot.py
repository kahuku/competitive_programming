def rotate(char, rot):
    return alphabet[(rot + alphabet.index(char)) % len(alphabet)]

def encrypt(plaintext, rot):
    ciphertext = ''
    for char in plaintext:
        ciphertext += rotate(char, rot)

    return ciphertext

alphabet = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.']
inp = input()
while inp != '0':
    rot, plaintext = int(inp.split()[0]), inp.split()[1][::-1]
    print(encrypt(plaintext, rot))
    inp = input()
