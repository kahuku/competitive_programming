def switch_2_5(s):
    return s.replace('2', '@').replace('5', '%').replace('@', '5').replace('%', '2')

a, b = map(switch_2_5, input().split())
a, b = a[::-1], b[::-1]
print(1 if int(a) > int(b) else 2)