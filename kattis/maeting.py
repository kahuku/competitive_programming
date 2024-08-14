input()
a = input().split()
b = set(input().split())
out = []
for num in a:
    if num in b:
        out.append(num)
print(' '.join(out))