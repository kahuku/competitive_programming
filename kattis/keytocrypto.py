ciphertext, key = input(), input()
plaintext = ""
for i in range(len(ciphertext)):
    c = ord(ciphertext[i]) - ord(key[i])
    if c < 0:
        c += 26
    plaintext += chr(c + ord('A'))
    key += chr(c + ord('A'))
print(plaintext)