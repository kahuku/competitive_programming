num = int(input())
h = num // (60 * 60)
m = num // 60 - 60 * h
s = num - (60 * 60) * h - 60 * m
print(f"{h} : {m} : {s}")