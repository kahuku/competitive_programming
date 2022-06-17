v1, v2, v3 = [input().split() for i in range(3)]

xs = [v1[0], v2[0], v3[0]]
ys = [v1[1], v2[1], v3[1]]

x_dict = dict()
for x in xs:
    x_dict[x] = x_dict.get(x, 0) + 1

y_dict = dict()
for y in ys:
    y_dict[y] = y_dict.get(y, 0) + 1

sorted_xs = dict(sorted(x_dict.items(), key=lambda item: item[1]))
sorted_ys = dict(sorted(y_dict.items(), key=lambda item: item[1]))

print(list(sorted_xs.keys())[0], list(sorted_ys.keys())[0])
