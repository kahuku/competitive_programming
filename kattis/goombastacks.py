running = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    running += a
    if running < b:
        print('impossible')
        exit()
print('possible')