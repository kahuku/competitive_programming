num_pipes = int(input())
s = 0
for i in range(num_pipes):
    s += int(input())

s += 1
s -= num_pipes
print(s)
