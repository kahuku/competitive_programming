k = int(input())

a = [int(input()) for _ in range(k)]
b = [int(input()) for _ in range(k)]

dp_a = [0] * k
dp_b = [0] * k

dp_a[0] = a[0]
dp_b[0] = b[0]

dp_a[1] = a[0] + a[1]
dp_b[1] = b[0] + b[1]

for i in range(2, k):
    dp_a[i] = a[i] + max(dp_a[i - 1], dp_b[i - 2])
    dp_b[i] = b[i] + max(dp_b[i - 1], dp_a[i - 2])
print(max(dp_a[-1], dp_b[-1]))