w1, w2 = input().lower(), input().lower()
if w1 == w2:
    print(0)
elif w1 < w2:
    print(-1)
else:
    print(1)