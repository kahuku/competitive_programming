mins, secs = 0, 0
for _ in range(int(input())):
    m, s = map(int, input().split())
    mins += m
    secs += s
print(secs / (mins * 60) if secs / (mins * 60) > 1 else "measurement error")