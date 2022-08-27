_ = input()
which_day = 1
temps = [int(i) for i in input().split()]
highest = [100, 100]
for i in range(len(temps) - 2):
    if temps[i] < max(highest) and temps[i + 2] < max(highest):
        which_day = i + 1
        highest = [temps[i], temps[i + 2]]

print(which_day, max(highest))