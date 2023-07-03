# TLE
input(); l = list(map(int, input().split()))
dp = [l[0]]
for i in range(1, len(l)):
    if l[i] > dp[-1]:
        dp = dp + [l[i]]
print(len(dp))
print(' '.join(map(str, dp)))