n = int(input())
h = 1
used = 0
last_layer_width = 1
while used < n:
    last_layer_width += 2
    used += last_layer_width ** 2
    h += 1
print(h - 1)