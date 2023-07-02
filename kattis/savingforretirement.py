b, br, bs, a, as_ = map(int, input().split())
bob = (br - b) * bs
alice = 0
while alice <= bob:
    alice += as_
    a += 1
print(a)