memo = [0] * 10001
memo[0] = 2
memo[1] = 3
for i in range(2, 10001):
    memo[i] = (memo[i-1] + memo[i-2]) % 1000000007

n = int(input())
for _ in range(n):
    print(memo[int(input())-1])