n, nn = map(int, input().split())
s = set()
for _ in range(nn):
    s.add(int(input()))
for i in range(n):
    if i not in s:
        print(i)
print("Mario got", len(s), "of the dangerous obstacles.")