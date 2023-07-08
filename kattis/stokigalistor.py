input(); arr = list(map(int, input().split()))
s_arr = sorted(arr)
x = sum(1 for i in range(len(arr)) if arr[i] != s_arr[i])
print(x)