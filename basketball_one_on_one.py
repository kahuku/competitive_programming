record = input()
a, b = 0, 0
for i in range(len(record) - 1):
    if i % 2 == 0:
        if record[i] == 'A':
            a += 1
        else:
            b += 1
print("A") if a > b else print("B")
