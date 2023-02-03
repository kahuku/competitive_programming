n = int(input())
for x in range(n):
    _ = input()
    v1, v2 = sorted([int(i) for i in input().split()]), sorted([int(i) for i in input().split()], reverse=True)
    a = sum([b * c for b, c in zip(v1, v2)])
    print(f"Case #{x + 1}: {a}")