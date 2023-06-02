n = int(input())
c = 0
for i in range(n):
    s = input().lower()
    if "rose" in s or "pink" in s:
        c += 1
print(c if c > 0 else "I must watch Star Wars with my daughter")