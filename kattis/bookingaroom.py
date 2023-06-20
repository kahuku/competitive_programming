r, n = map(int, input().split())
s = set([i for i in range(1, r + 1)])
for _ in range(n):
    s.remove(int(input()))
if len(s) == 0:
    print("too late")
else:
    print(list(s)[0])