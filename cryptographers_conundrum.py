ciphertext = input()
changes = 0
for i, letter in enumerate(ciphertext):
    if i % 3 == 0 and letter != 'P' or i % 3 == 1 and letter != 'E' or i % 3 == 2 and letter != 'R':
        changes += 1
print(changes)