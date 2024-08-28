n = int(input())
aa, ab = map(int, input().split())
ba, bb = map(int, input().split())
a = 0
b = 0
for i in range(n):
    a += (aa + ab * i)
    b += (ba + bb * i)
if a == b:
    print("=")
elif a < b:
    print("Alice")
else:
    print("Bob")