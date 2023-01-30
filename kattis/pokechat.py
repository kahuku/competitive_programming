s, x = input(), input()
indeces = [int(''.join(x[i:i+3])) for i in range(0, len(x), 3)]
print(''.join([s[index - 1] for index in indeces]))