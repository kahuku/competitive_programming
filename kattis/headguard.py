from sys import stdin
for line in stdin.readlines():
    letters, counts = [], []
    for letter in line:
        if letters and letters[-1] == letter:
            counts[-1] += 1
        else:
            letters.append(letter)
            counts.append(1)
    print(''.join([str(count) + letter for letter, count in zip(letters, counts[:-1])]))