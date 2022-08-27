inp = [int(i) for i in input().split()]
num_buttons, num_bulbs = inp[0], inp[1]

lit = set()
for i in range(num_buttons):
    line = [int(i) for i in input().split()][1:]
    lit.update(line)

if len(lit) == num_bulbs:
    print("YES")
else:
    print("NO")

