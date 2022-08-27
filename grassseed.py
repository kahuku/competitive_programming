cost = float(input())
num_lawns = int(input())

s = 0.0
for i in range(num_lawns):
    inp = input().split()
    l = float(inp[0])
    w = float(inp[1])
    s += l * w * cost
print(s)
