cals = [int(i) for i in input().split()]
squares = input()
total = 0
for square in squares:
    total += cals[int(square) - 1]
print(total)