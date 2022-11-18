_, pieces = input(), [int(i) for i in input().split()]
pieces = sorted(pieces, reverse=True)
print(pieces)
print(sum(pieces[::2]), sum(pieces[1::2]))