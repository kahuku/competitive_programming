# TLE
def solve(seq):
    dp = [1] * len(seq)
    # dpi = [[i] for i in range(len(seq))]
    dpi = [set([i]) for i in range(len(seq))]
    for i in range(len(seq)):
        for j in range(i):
            if seq[i] > seq[j]:
                a = dp[i]
                b = dp[j] + 1
                if a >= b:
                    dp[i] = a
                else:
                    dp[i] = b
                    # dpi[i] = dpi[j] + [i]
                    dpi[i] = dpi[j].copy()
                    dpi[i].add(i)
                
    i = 0
    for j, score in enumerate(dp):
        if score > dp[i]:
            i = j
    
    print(dp[i])
    print(' '.join(map(str, sorted(dpi[i]))))
        
from sys import stdin

i = 0
for i, line in enumerate(stdin.readlines()):
    if i % 2 == 0:
        pass
    else:
        seq = list(map(int, line.split()))
        solve(seq)
