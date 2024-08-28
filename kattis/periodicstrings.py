def valid(a, b):
    return a[-1] + a[:-1] == b

def periodic(s, n):
    broken = [s[i:i+n] for i in range(0, len(s), n)]
    prev = broken[0]
    for seq in broken[1:]:
        if not valid(prev, seq):
            return False
        prev = seq
    return True

s = input()
numsToTry = list(range(1, len(s)))
for num in numsToTry:
    if len(s) % num != 0:
        continue
    if periodic(s, num):
        print(num)
        exit(0)
print(len(s))