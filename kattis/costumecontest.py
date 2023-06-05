n = int(input())
t = {}
for i in range(n):
    costume = input()
    if costume in t:
        t[costume] += 1
    else:
        t[costume] = 1    
s = sorted([key for key, value in t.items() if value == min(t.values())])
for costume in s:
    print(costume)