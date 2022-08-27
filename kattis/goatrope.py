#goatrope

inp = [int(i) for i in input().split()]
x, y, x1, y1, x2, y2 = inp[0], inp[1], inp[2], inp[3], inp[4], inp[5]

d = float(0)

if x > x1 and x < x2:
    #in between x
    #print("in between x")
    if y > y2:
        #above rect
        d = y - y2
    elif y < y1:
        #below rect
        d = y1 - y
elif x < x1:
    #left of rect
    if y > y1 and y < y2:
        #in between y
        d = x1 - x
    elif y > y2:
        #above rect
        d = (((x1 - x) ** 2) + ((y2 - y) ** 2)) ** 0.5
    elif y < y1:
        #below rect
        d = (((x1 - x) ** 2) + ((y1 - y) ** 2)) ** 0.5
elif x > x2:
    #right of rect
    if y > y1 and y < y2:
        #in between y
        d = x - x2
    elif y > y2:
        #above rect
        d = (((x2 - x) ** 2) + ((y2 - y) ** 2)) ** 0.5
    elif y < y1:
        #below rect
        d = (((x2 - x) ** 2) + ((y1 - y) ** 2)) ** 0.5
#else:
    #print("Didn't trigger")
print(d)
