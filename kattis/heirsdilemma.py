def valid (n):
    if '0' in n:
        return False
    if len(set(n)) != len(n):
        return False
    for i in n:
        if int(n) % int(i) != 0:
            return False
    return True

l, h = map(int, input().split())
count = 0
for i in range(l, h+1):
    if valid(str(i)):
        count += 1
print(count)