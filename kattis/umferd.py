c, r = int(input()), int(input())
grid = [input() for _ in range(r)]
ca = sum([row.count('#') for row in grid])
print (1 - (ca / (c * r)))