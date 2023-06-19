l, x = map(int, input().split())
peeps = 0
count = 0
for _ in range(x):
    event, n = input().split()
    n = int(n)
    if event == 'enter':
        if peeps + n > l:
            count += 1
        else:
            peeps += n
    else:
        peeps -= n
print(count)