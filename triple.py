def find(arr):
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            return arr[i]
    return -1

cases = int(input())
for i in range(cases):
    _, arr = input(), [int(i) for i in input().split()]
    arr.sort()
    print(find(arr))