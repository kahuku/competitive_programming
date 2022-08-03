target = int(input())
high, low = 10, 0
x = (high + low) / 2
diff = x ** x - target
while abs(diff) > .000001:
    if diff < 0:
        low = x
    else:
        high = x
    x = (high + low) / 2
    diff = x ** x - target
print(x)