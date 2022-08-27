year = int(input()) + 1
while len(set([i for i in str(year)])) < 4:
    year += 1
print(year)
