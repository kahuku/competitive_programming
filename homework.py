inp = input().split(';')

for i in range(len(inp)):
    if '-' in inp[i]:
        inp[i] = inp[i].split('-')
        inp[i] = [int(j) for j in inp[i]]
    else:
        inp[i] = int(inp[i])

# print(inp)

count = 0

for i in range(len(inp)):
    entry = inp[i]
    if isinstance(entry, int):
        count += 1
    else:
        count += (entry[1] - entry[0] + 1)

print(count)
