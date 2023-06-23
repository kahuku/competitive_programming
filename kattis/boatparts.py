p, n = map(int, input().split())
parts = set()
out = None
for i in range(n):
    parts.add(input())
    if not out and len(parts) == p:
        out = i + 1
print("paradox avoided" if not out else out)