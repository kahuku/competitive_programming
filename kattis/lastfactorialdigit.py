n = int(input())
for i in range(n):
    num = int(input())
    prod = num
    counter = num
    while counter > 1:
        counter -= 1
        prod *= counter
    prod = str(prod)
    p = int(prod[len(prod)-1])
    print(p)
